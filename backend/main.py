import heapq

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
        return self.entry_finder[item]

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


pronouns =  [("yo", "i"), ("tú", "you"), ("él", "he"), ("ella", "she"), ("nosotros/as", "we"), 
                 ("vosotros/as", "you all"), ("ellos/as", "they"), ("usted", "you"), 
                 ("nosotros/as", "we"), ("ustedes", "you all")]
verbs = [("ser", "to be"), ("estar", "to be"), ("tener", "to have"), 
              ("hacer", "to do, to make"), ("poder", "to be able to"), ("ir", "to go"), 
              ("ver", "to see"), ("comer", "to eat"), ("beber", "to drink"), ("vivir", "to live")]
nouns = [("persona", "person"), ("hombre", "man"), ("mujer", "woman"), ("niño", "boy"), ("niña", "girl"), 
              ("amigo/a", "friend"), ("familia", "family"), ("casa", "house"), ("calle", "street"), ("escuela", "school")]
adjectives = [("grande", "big"), ("pequeño/a", "small"), ("bueno/a", "good"), ("malo/a", "bad"), 
                   ("nuevo/a", "new"), ("viejo/a", "old"), ("bonito/a", "pretty, beautiful"), ("feo/a", "ugly"), 
                   ("feliz", "happy"), ("triste", "sad") ]
interrogatives = [("qué", "what"), ("quién", "who"), ("cuándo", "when"), ("dónde", "where"), 
                       ("por qué", "why"), ("cómo", "how"), ("cuanto", "how many"), ("cual", "what"), ("que hora es", "what time is it"), ("de quien", "whose")]
prepositions = [("en", "in"), ("sobre", "on, about"), ("bajo", "under"), ("cerca de", "near"), 
                     ("lejos de", "far from"), ("entre", "between"), ("a", "to, at"), ("con", "with"), 
                     ("sin", "without"), ("ante", "before, in front of")]
phrases = [("hola", "hello"), ("gracias", "thank you"), ("por favor", "please"), ("como estas", "how are you"), ("estoy bien", "im good"), ("mucho gusto", "nice to meet you"), ("adios", "goodbye"), ("perdon", "excuse me"), ("lo siento", "sorry"), ("me llama", "my name is")]

# set up all tries for each category
noun_trie = Trie()
for spanish, english in nouns:
    noun_trie.insert(spanish, english)

verbs_trie = Trie()
for spanish, english in verbs:
    verbs_trie.insert(spanish, english)

pronouns_trie = Trie()
for spanish, english in pronouns:
    pronouns_trie.insert(spanish, english)

adj_trie = Trie()
for spanish, english in adjectives:
    adj_trie.insert(spanish, english)

inter_trie = Trie()
for spanish, english in interrogatives:
    inter_trie.insert(spanish, english)

prep_trie = Trie()
for spanish, english in prepositions:
    prep_trie.insert(spanish, english)

phrase_trie = Trie()
for spanish, english in phrases:
    phrase_trie.insert(spanish, english)


# examples
print(noun_trie.search("niña"))  # output: "girl"
print(noun_trie.search("casa"))  # output: "house"
print(noun_trie.search("perro"))  # output: None (not in the Trie)

# get words that start with "ca"
print(noun_trie.starts_with("ca"))  # output: [('casa', 'house'), ('calle', 'street')]
print(verbs_trie.exists("comer")) # check if it exists to know which trie it belongs to

# pq set up with each list in order of priority
pq = PriorityQueue()
for phrase, translation in phrases:
    pq.push(phrase, 1, translation)

for noun in nouns:
    pq.push(noun, 2, translation)

for pronoun in pronouns:
    pq.push(pronoun, 3, translation)

for interrogative in interrogatives:
    pq.push(interrogative, 4, translation)

for adjective in adjectives:
    pq.push(adjective, 5, translation)

for verb in verbs:
    pq.push(verb, 6, translation)

for preposition in prepositions:
    pq.push(preposition, 7, translation)

print(pq.get_translation("hola"))