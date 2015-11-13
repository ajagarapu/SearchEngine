'''
Created on Nov 11, 2015

@author: Ashwin
'''
from com.gsu.python.algo.vector_space import VectorSpace
from os.path import isfile,join,dirname
from os import listdir,getcwd
from com.gsu.python.algo.tfidf import TFIDF
from com.gsu.python.ui.display import Display
 
def main():
    mypath = dirname(getcwd())+'\\data'
    docfile_list = [f for f in listdir(path=mypath) if isfile(join(mypath,f))]
    d=Display(docfile_list)
    #d.search
    #tfidf=TFIDF(docfile_list)
    #tfidf.searchRelevantDocument()
    #vs = VectorSpace(docfile_list)
    
main()