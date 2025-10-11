#vectors 
← [[Vectors, Scalars, and Dot Product|Back]]

-Function of the project is to take in two words from the user and then spit out a similarity score .
-required libraries : numpy and scikit-learn
The step by step is :
1. Get the two texts from the user 
2. calculate the TF-IDf vectors for each.
3. calculate the cosine similarity of the two vectors ,
4. convert into a percentage and spit it out to terminal .
# Code
requirements:
```
uv add numpy scikit-learn
```
code file 
```
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_text_similarity(text1, text2):
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([text1, text2])
    
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    
    percentage = similarity * 100
    
    return percentage

def main():
    print("Text Similarity Calculator")
    print("-" * 30)

    text1 = input("Enter first text: ")
    text2 = input("Enter second text: ")
    
    similarity_percentage = calculate_text_similarity(text1, text2)
    
    print(f"\nSimilarity Score: {similarity_percentage:.2f}%")

if __name__ == "__main__":
    main()
```
# Underlying concepts :
1. TF : This is used to calculate the the frequency of a work within a given strin or document . higher the frequency higher the value . 
			TF(t,d) = (Number of times term t appears in document d) / (Total number of terms in document d) 
2. IDF : is used to calculate the frequency of appearance of any given word in many different documents and its ain a logarithim scale meaning higher the frequency lower the value and vice versa. 
			IDF(t) = log(Total number of documents / Number of documents containing term t)
3. TF-IDF : is just a scalar product of the two  above . why this works well is that one balances the other . just because a word appears many times does-not mean its relevant (for eg the word "the" is used in almost every single document but it hold very low significance but the word quantum may also appear many times in a study about electrons but here is is clearly significant  )so we use these values in conjunction to construct a balanced vectors that accounts for both phenomena 







