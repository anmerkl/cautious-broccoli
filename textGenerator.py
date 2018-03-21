"""Generates text in a variety of different formats and filetypes"""
__author__ = "Aleksey Berdnikov for Infinite Monkeys"

from sys import argv
import random
import string

""" 
textGenerate() generates text for the purpose of testing lambda functions and word matching.

    params:
        wordOrChar       = tag that dictates whether or not the output will consist
                         of legible words, or of completely random characters.

        separateOrStream = tag that dictates whether or not the output will consist
                        of a series of variable-length strings, or of a single large stream of
                        characters.
                
        length          = an int that dictates, in the case that separateStrings is TRUE, the amount
                        of distinct words to be generated.
                        
        output          = a string that dictates in what form the generated text should be output.
                        By default, textGenerate will output a csv file named "output.txt".  
                        
    format for command line arguments:
        textGenerate.py -w "word"/"char" -s "separate"/"stream" -l "123" -o "filename.txt"
"""

def generateRandomWord():

    stream = []

    splitStream = []

    while True:
        stream.append(random.choice(string.ascii_letters))
        if random.randint(4, 12) < len(stream):
            splitStream.append(''.join(stream))
            break

    return ''.join(splitStream)


def fetchWord(wordOrChar):

    if wordOrChar == "word":

        words = open("words.txt", "r").readlines()

        word = random.choice(words)

        return word.rstrip()
    else:

        return generateRandomWord()


def generateStream(length, wordOrChar):

    stream = []

    for i in range(0, length):
        stream.append(fetchWord(wordOrChar))

    return ''.join(stream)


def generateWords(length, wordOrChar):

    words = []

    for i in range(0, length):
        word = fetchWord(wordOrChar)
        word += "\n"
        words.append(word)

    return words


def getopts(argv):
    opts = {}
    while argv:
        # Found a possible "-name value" pair.
        if argv[0][0] == '-':
            # Add key and value to the dictionary.
            opts[argv[0]] = argv[1]
        argv = argv[1:]
    return opts


def textGenerate(argv):

    params = getopts(argv)

    output = []

    if params["-s"] == "stream":
        output = generateStream(int(params["-l"]), params["-w"])
    else:
        output = generateWords(int(params["-l"]), params["-w"])

    targetFile = open(params["-o"], "w")

    for word in output:
        targetFile.write("%s" % word)

    print("Successfully created {}!".format(params["-o"]))

if __name__ == "__main__":
    textGenerate(argv)