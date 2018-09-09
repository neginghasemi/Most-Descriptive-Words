# Most-Descriptive-Words
Implementation of a language model based system for retrieving most descriptive words

## Introduction
Feedback, as one of the main components of information retrieval systems. , occurs when the system output is returned as part of the input and forms a loop. We can use feedback to improve our query. We want to use the idea of feedback to generate the most appropriate words as a query to retrieve documents.
As mentioned in [this](https://dl.acm.org/citation.cfm?id=502654) paper, we can use a generative mixture model. Its definition according to the reference is as follows: 

Assuming a generative model, we estimate the query topic model using the observed feedback documents based upon a maximum likelihood or regularized maximum likelihood criterion. The particular generative model we consider here is a simple mixture model, using the collection language model as one component, and the query topic model as the other. 

I also used Dirichlet smoothing for better results.

## Uses
 - [Sklearn](http://scikit-learn.org/stable/)

## Run
 - `most_descriptive_words.py` will extract 10 most descriptive words (unigram & bigram) from `input.txt` using `corpus.txt`

## Output
 - `Unigram.csv` 10 most descriptive unigrams
 - `Bigram.csv`  10 most descriptive bigrams
