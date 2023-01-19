# Semantic distance

## Objectives
The goal is to implement a semantic distance between 2 products:

Exemple :

Product A = Président beurre 200g barquette

Product B = Duracell piles AAA blister x4

Product C = Elle & Vire crème fraîche épaisse 50cL

-> the result should be like: Distance(A, C) < Distance(A, B)

(le beurre est sémantiquement plus proche de la crème fraîche que les piles)

## Data

 A product is an object with a name, a brand and one or many categories
 
 ## Scripts
 
**For more details make sure to visit these files to look at script arguments and description**

```Product_similarity_NLP.ipynb.ipynb ``` describes the approches used to solve the problem  (language model/ Doc2vec/google universal encoder)

```product_similarity``` contains the model with a demo of how to use it 
