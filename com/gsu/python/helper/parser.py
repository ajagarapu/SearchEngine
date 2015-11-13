'''
Created on Nov 11, 2015

@author: Ashwin, Vishesh, Rajkiran, Kshitij
'''
from com.gsu.python.helper.PorterStemmer import PorterStemmer
from os.path import isfile

class Parser:
    STOP_WORDS_FILE = 'stopwords.txt'

    stemmer = None
    stopwords = []

    def __init__(self, stopwords_io_stream = None):
        self.stemmer = PorterStemmer()
        
        if(not stopwords_io_stream):
            if(isfile(Parser.STOP_WORDS_FILE)):
                #print("File exists")
                stopwords_io_stream = open(Parser.STOP_WORDS_FILE, 'r')
            else:
                print("exit bro")

        self.stopwords = stopwords_io_stream.read().split()

    def tokenise_and_remove_stop_words(self, document):
        #if no elements in the list return an empty list
        if not document:
            return []
        #vocabulary_string = " ".join(document)
        tokenised_vocabulary_list = self._tokenise(document)
        clean_word_list = self._remove_stop_words(tokenised_vocabulary_list)
        return clean_word_list

    def _remove_stop_words(self, list):
        return [word for word in list if word not in self.stopwords ]


    def _tokenise(self, string):
        string = self._clean(string)
        #words = string.split(" ")
        return [self.stemmer.stem(word, 0, len(word)-1) for word in string]

    def _clean(self, string):
        characters="~@#$%^&*()_-+=!|'\".,!;:\n\t\\\"?!{}[]<>"
        words = string.lower().split()
        return [word.strip(characters) for word in words]
        '''string = string.replace(".","")
        string = string.replace("\n"," ")
        string = string.replace("\'","")
        string = string.replace("\"","")
        string = string.replace(","," ")
        string = string.replace("?","")
        string = string.replace("!","")
        string = string.lower()
        return string'''

def main():
    p=Parser()
    