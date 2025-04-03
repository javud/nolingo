from flask import Flask, request, jsonify
from flask_cors import CORS
import heapq
import json
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for frontend communication

# Priority Queue Implementation
class PriorityQueue:
    def __init__(self):
        self.pq = []
        self.index = 0
        self.entry_finder = {}

    def push(self, item, priority, translation):
        heapq.heappush(self.pq, (priority, self.index, item))
        self.entry_finder[item] = translation
        self.index += 1

    def pop(self):
        return heapq.heappop(self.pq)[-1]

    def get_translation(self, item):
        return self.entry_finder.get(item, None)

# Trie Implementation
class TrieNode:
    def __init__(self):
        self.children = {}
        self.translation = None
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, spanish_word, english_translation):
        node = self.root
        for char in spanish_word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.translation = english_translation

    def search(self, spanish_word):
        node = self.root
        for char in spanish_word:
            if char not in node.children:
                return None
            node = node.children[char]
        return node.translation if node.is_end_of_word else None

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        return self.collect_words(node, prefix)

    def collect_words(self, node, prefix):
        words = []
        if node.is_end_of_word:
            words.append((prefix, node.translation))

        for char, child in node.children.items():
            words.extend(self.collect_words(child, prefix + char))

        return words

    def exists(self, spanish_word):
        node = self.root
        for char in spanish_word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

# Load categories.json
with open("data/categories.json", "r", encoding="utf-8") as file:
    categories_data = json.load(file)

# Extract the 'categories' dictionary and convert lists to tuples
categories = {
    category: [tuple(pair) for pair in words] 
    for category, words in categories_data["categories"].items()
}

# Extract words from categories
sentences = {}

for category, word_list in categories_data["categories"].items():
    for word, _ in word_list:
        normalized_word = word.lower()
        sentences[normalized_word] = []

# Load sentences for each category
for category in categories_data["categories"]:
    file_path = f"data/sentences/{category}.json"

    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            category_sentences = json.load(file)

            for key in category_sentences:
                normalized_key = key.lower()

                # Try direct match
                if normalized_key in sentences:
                    sentences[normalized_key] = category_sentences[key]
                else:
                    # Fuzzy matching for slight variations (e.g., "me llama" vs. "me llamo")
                    for word in sentences:
                        if normalized_key.startswith(word) or word.startswith(normalized_key):
                            sentences[word] = category_sentences[key]
                            break

tries = {category: Trie() for category in categories}

for category, words in categories.items():
    for spanish, english in words:
        tries[category].insert(spanish, english)

# Priority Queue
pq = PriorityQueue()
for category, words in categories.items():
    priority = list(categories.keys()).index(category) + 1  # Assign priority based on category order
    for spanish, english in words:
        pq.push(spanish, priority, english)

# Flask Endpoints
@app.route('/search', methods=['GET'])
def search():
    word = request.args.get('word', '').lower()
    for category, trie in tries.items():
        translation = trie.search(word)
        if translation:
            return jsonify({"category": category, "translation": translation})
    return jsonify({"error": "Word not found"}), 404

@app.route('/exists', methods=['GET'])
def exists():
    word = request.args.get('word', '').lower()
    for category, trie in tries.items():
        if trie.exists(word):
            return jsonify({"exists": True, "category": category})
    return jsonify({"exists": False})

@app.route('/suggestions', methods=['GET'])
def suggestions():
    prefix = request.args.get('prefix', '').lower()
    suggestions = []
    for category, trie in tries.items():
        suggestions.extend(trie.starts_with(prefix))
    return jsonify({"suggestions": suggestions})

@app.route('/get_translation', methods=['GET'])
def get_translation():
    word_param = request.args.get('word', '')
    index = int(request.args.get('i', -1))  # Get the index from the request

    # Check if 'word' is "next", and fetch the word at the provided index
    if word_param == "next" and 0 <= index < len(pq.pq):
        spanish_word = pq.pq[index][-1]  # Get the word at the given index from the priority queue
        english_translation = pq.get_translation(spanish_word)
        return jsonify({"translation": {"word": spanish_word, "translation": english_translation}})
    
    return jsonify({"error": "Invalid word or index"}), 404

@app.route('/get_sentences', methods=['GET'])
def get_sentences():
    word = request.args.get('word', '').lower()
    for category, trie in tries.items():
        if trie.exists(word):
            word_sentences = sentences.get(word, [])
            if word_sentences:
                return jsonify({"sentences": word_sentences})
    return jsonify({"error": "No sentences found for the word"}), 404

@app.route("/category")
def get_category():
    category_name = request.args.get("name", "").lower()
    if category_name in categories:
        return jsonify({"words": categories[category_name]})
    return jsonify({"words": []}), 404

if __name__ == '__main__':
    app.run(port=5001, debug=True)
