'''
Created on Nov 12, 2015

@author: Ashwin, Vishesh, Rajkiran, Kshitij
'''
import os
import sys
import math
from collections import defaultdict
from com.gsu.python.helper.parser import Parser
from os.path import dirname
from os import getcwd

class TFIDF:
    #adding all the files to the dictionary
    mypath=dirname(getcwd())+"\\data"
    documentFreqDict={}
    vectorSpaceSet=set()
    fileDetails={}
    nestedDict = defaultdict(dict)
    queryTFIDFDict={}
    N=0
    parser = None
    
    def __init__(self,allFiles):
        self.parser = Parser()
        self.initializeVectorSpace(allFiles)
        
    def initializeVectorSpace(self,allFiles): 
        #try:          
            #setting the of the document to be zero
            docId=1
            for file in allFiles:
                fileName=self.mypath+"\\"+file
                print(fileName) 
                
                if file.endswith(".txt"):
                    self.fileDetails[docId]=fileName                        
                    infile=open(fileName,"r")
                    document = infile.read()
                    infile.close()
                    #tokenized=self.tokenization(document)
                    tokenized=self.parser.tokenise_and_remove_stop_words(document)             
                    tempSet=set(tokenized)
                    print(tempSet)
                    self.vectorSpaceSet=self.vectorSpaceSet.union(tempSet)
                    for term in tempSet:
                        #normalized length
                        self.nestedDict[term][docId]=tokenized.count(term)/len(tokenized)                  
                    docId+=1
                    print(self.nestedDict)
                    print(len(self.nestedDict))
                               
            self.calculateDocumentFrequency()
            self.N =len(self.fileDetails)
            print(self.N)
        #except:
         #   print("Exception occured")'''
    
    #Tokenization function- It splits the files in to lines and then lines into words, removes the punctuation     
    '''def tokenization(self,document):
        try:            
            characters="~@#$%^&*()_-+=!|'\".,!;:\n\t\\\"?!{}[]<>"
            words = document.lower().split()
            return [word.strip(characters) for word in words]
        except:
            print("Exception occured")    '''
    
    def calculateDocumentFrequency(self):
        #calculates the number of documents this given keyword appears       
        for word in self.vectorSpaceSet:
            self.documentFreqDict[word]=len(self.nestedDict[word])        
    def inverseDocumentFrequency(self,term):    
        if term in self.vectorSpaceSet:
            print(self.documentFreqDict[term])
            print(self.N)
            return 1+math.log(self.N/self.documentFreqDict[term])
        else:
            return 0.0 
        
    def imp(self,term,docId):    
        if docId in self.nestedDict[term]:
            return self.nestedDict[term][docId]*self.inverseDocumentFrequency(term)
        else:
            return 0.0
            
    def cosineSimilarity(self,query,docId):
        similarity=0.0
        aSquare=0.0
        bSquare=0.0
        lengthOfQuery=len(query)
        for term in query:
            #normalized frequency
            self.queryTFIDFDict[term]=(query.count(term)/lengthOfQuery)*self.inverseDocumentFrequency(term)
            aSquare+=math.pow(self.queryTFIDFDict[term],2)
            bSquare+=math.pow(self.imp(term,docId),2)
            similarity += self.queryTFIDFDict[term]*self.imp(term,docId)
        modAmodB=math.sqrt(aSquare)*math.sqrt(bSquare)
        similarity=similarity/modAmodB
        return similarity
        #creating Query vector for the dot product with document vector
        
    #Function that creates a set which has all the words from all the the documents, called as corpus dictionary, or the vector spcae which has the document vectors
    #each term is defined as a unit vector,document vector \vec d is just the vector whose component in the direction \vec e_t of term t is a measure of the importance 
    #of term t in the document d
    def searchRelevantDocument(self,lst):
        
        inputQuery=lst.strip()
        inputQuery=self.parser.tokenise_and_remove_stop_words(inputQuery)
        if inputQuery==[]:        
            sys.exit()
            
        else:
            scoresList=[]
            final_set=set()
            relevant_document_ids =[set(self.nestedDict[term].keys()) for term in inputQuery]
            relevant_document_ids=list(relevant_document_ids)    
            #add a if clause
            if(len(relevant_document_ids)>2):
                final_set=(relevant_document_ids[0]).intersection((relevant_document_ids[1]))
                for i in range(2,len(relevant_document_ids)):
                    final_set=set(final_set).intersection(relevant_document_ids[i])
            elif(len(relevant_document_ids)==2):
                final_set=(relevant_document_ids[0]).intersection((relevant_document_ids[1]))
            else:
                final_set=(relevant_document_ids[0]).intersection((relevant_document_ids[0]))
            final_set=list(final_set)               
            for id1 in final_set:                
                result=[(self.cosineSimilarity(inputQuery,id1)),self.fileDetails[id1]]
                scoresList.append(result) 
            scoresList.sort() 
            resStr=''
            
            for i in range(len(scoresList)):
                fname=str(scoresList[i][1]).split("/")
                resStr+=str(i+1)+" "+str(fname[len(fname)-1])+"\n\n"    
            return resStr                  
            
                       
             
    def intersection(self,sets):
        """Returns the intersection of all sets in the list sets. Requires
        that the list sets contains at least one element, otherwise it
        raises an error."""
        print( (set.intersection, [s for s in sets]))   
        return (set.intersection, [s for s in sets])                 
