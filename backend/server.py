from flask import Flask, request, jsonify
from flask_cors import CORS
import heapq
import random

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

# Populate Tries
categories = {
    "nouns": [
        ("persona", "person"), 
        ("hombre", "man"), 
        ("mujer", "woman"), 
        ("niño", "boy"), 
        ("niña", "girl"), 
        ("amigo/a", "friend"), 
        ("familia", "family"), 
        ("casa", "house"), 
        ("calle", "street"), 
        ("escuela", "school")
    ],
    "verbs": [
        ("ser", "to be"), 
        ("estar", "to be"), 
        ("tener", "to have"), 
        ("hacer", "to do, to make"), 
        ("poder", "to be able to"), 
        ("ir", "to go"), 
        ("ver", "to see"), 
        ("comer", "to eat"), 
        ("beber", "to drink"), 
        ("vivir", "to live")
    ],
    "pronouns": [
        ("yo", "I"), 
        ("tú", "you"), 
        ("él", "he"), 
        ("ella", "she"), 
        ("nosotros/as", "we"), 
        ("vosotros/as", "you all"), 
        ("ellos/as", "they"), 
        ("usted", "you"), 
        ("nosotros/as", "we"), 
        ("ustedes", "you all")
    ],
    "adjectives": [
        ("grande", "big"), 
        ("pequeño/a", "small"), 
        ("bueno/a", "good"), 
        ("malo/a", "bad"), 
        ("nuevo/a", "new"), 
        ("viejo/a", "old"), 
        ("bonito/a", "pretty, beautiful"), 
        ("feo/a", "ugly"), 
        ("feliz", "happy"), 
        ("triste", "sad")
    ],
    "interrogatives": [
        ("qué", "what"), 
        ("quién", "who"), 
        ("cuándo", "when"), 
        ("dónde", "where"), 
        ("por qué", "why"), 
        ("cómo", "how"), 
        ("cuanto", "how many"), 
        ("cual", "what"), 
        ("que hora es", "what time is it"), 
        ("de quien", "whose")
    ],
    "prepositions": [
        ("en", "in"), 
        ("sobre", "on, about"), 
        ("bajo", "under"), 
        ("cerca de", "near"), 
        ("lejos de", "far from"), 
        ("entre", "between"), 
        ("a", "to, at"), 
        ("con", "with"), 
        ("sin", "without"), 
        ("ante", "before, in front of")
    ],
    "phrases": [
        ("hola", "hello, hi"), 
        ("gracias", "thank you"), 
        ("por favor", "please"), 
        ("como estas", "how are you"), 
        ("estoy bien", "I'm good"), 
        ("mucho gusto", "nice to meet you"), 
        ("adios", "goodbye"), 
        ("perdon", "excuse me"), 
        ("lo siento", "sorry"), 
        ("me llama", "my name is")
    ]
}

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
    word = request.args.get('word', '').lower()

    if word == "next":
        if pq.pq:
            next_word = pq.pop()  # Get the next word in priority order
            translation = pq.get_translation(next_word)
            return jsonify({"translation": {"word": next_word, "translation": translation}})
        return jsonify({"error": "No more words available"}), 404

    translation = pq.get_translation(word)
    if translation:
        return jsonify({"translation": {"word": word, "translation": translation}})
    return jsonify({"error": "Translation not found"}), 404

@app.route("/category")
def get_category():
    category_name = request.args.get("name", "").lower()
    if category_name in categories:
        return jsonify({"words": categories[category_name]})
    return jsonify({"words": []}), 404

if __name__ == '__main__':
    app.run(port=5001, debug=True)
