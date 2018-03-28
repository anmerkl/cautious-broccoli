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