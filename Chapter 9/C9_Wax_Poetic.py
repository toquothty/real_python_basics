# Chapter 9 Challenge: Wax Poetic
# Randomly select the following number of elements from each list:
# 3-nouns, 3-verbs, 3-adjectives, 2-prepositions, 1-adverb
# 
import random

# Define the wordlists utilized
nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango",
"extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", 
"curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", 
"exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", 
"for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", 
"furiously", "sensuously"]

def randomizer():
    noun = random.choices(nouns, k=3)
    verb = random.choices(verbs, k=3)
    adjective = random.choices(adjectives, k=3)
    preposition = random.choices(prepositions, k=2)
    adverb = random.choices(adverbs, k=3)

    print(f"A {adjective[0]} {noun[0]} \n")
    print(f"A {adjective[0]} {noun[0]} {verb[0]} {preposition[0]} the {adjective[1]} {noun[1]} \n{adverb[0]}, the {noun[0]} {verb[1]} \n")
    print(f"the {noun[1]} {verb[2]} {preposition[1]} a {adjective[2]} {noun[2]}")



randomizer()