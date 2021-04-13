##
# pig_latin.py
# Jordan Maloney
# 13/4/21

VOWELS = ["a", "e", "i", "o", "u"]
COSONANTS = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
             "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


def sentence_input():
    """
    Takes an input from the user, and converts it to a list
    """
    loop = True
    while loop == True:
        try:
            # Input sentence
            sentence = input(
                "Please input a sentence to be converted to Pig Latin(Without punctuation): "
                ).lower()
            # Trigger TypeError if punctuation is in sentence
            for char in sentence:
                if char not in VOWELS and char not in COSONANTS and char != " ":
                    print("String" * "String")
            loop = False
        except:
            TypeError
            print("Please do not input punctuation.")
            loop = True
    words = sentence.split(" ")
    converter(words)



def converter(words):
    for word in words:
        if words[word][0] in COSONANTS:
            words[word].append((words[word][0]), "ay")
            words[word].remove(words[word][0])
        else:
            words[word].append((words[word][0]), "way")
            words[word].remove(words[word][0])
    print(words)
sentence_input()
