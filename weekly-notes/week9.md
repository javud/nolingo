# Sample Weekly Meeting Notes:
Please note that this is the required layout for the weekly notes.

## Overview:
**When**: 03/17 - Third meeting
**Duration**: 1 hr 30 min
**Where**: At syeds apartment

## Attendance
**Late**: N/A
**Missing**: N/A

## Recent Progress:
- Determined layout of application
1. Figma layout created
2. Agreed on data structures for each layout component

## Meeting Notes: 
- Data structure/storage agreement
1. Priority queue - set of words to be taught to player in order of highest priority = most basic word to be taught first. Optimal
because order of lessons is vital in teaching a language effectively
2. Map - verbs map to their conjugations
3. Map - 20 words map to multiple stories made from them. Stories placed after multiple core lessons (1-10)
4. AST - check grammar of user's input to see if it matches grammar tree of Spanish. Optimal because it allows for quick check of sentence gramar without unnecessary processing of word meanings themselves.
5. List - represent lessons themselves and allow for unsuccessful lessons to be appeneded to end to retry
6. Map - cosine similarity for 50 base words
7. Trie - not used because auto complete would be rarely used and usually against the purpose of practicing a language

- Figma
1. Improvements: move input below prompt
2. Images: display image for newly learned nouns (cat, apple, etc)
3. Progress bar: show user how far into the lesson they are (incorrect lessons appended to end)

- Ethical issues/reducing negative impacts
1. Use of AI will allow room for allowed mistakes for user
2. Focuses on Spain-Spanish dialect and promoting that one dialect as the whole of Spanish

- Data processing
1. Cut down Merriam-Webster list into 50 key words
2. Sort words by size to assign difficulty in learning
3. Sort words into categories of verb, noun, adjective so amounts are equal across board

 
## Action Items (Work In Progress):
- Finalize Figma
- Begin 3 key pages