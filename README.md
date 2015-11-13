# Search for static library files
Language: Pyhton
Search based on Vector Space Model on large set of text files.
It uses Porter Stemmer algorithm to stem the words of each of the text files.
Below are the steps implemented in this project:

Step 1: Extract all the files from the folder.
Step 2: For each document, split, strip, tokenize and stem the document data.
Step 3: Create the document vectors.
Step 4: Fetch the input query from the user.
Step 5: Repeat Step 2 and Step 3 to create the query vector.
Step 6: Remove the irrelevant documents and calculate the cosine similarity on the relevant documents.
Step 7: Apply TF-IDF algorithm to the vectors.
Step 8: Display the final results in a sorted order.

