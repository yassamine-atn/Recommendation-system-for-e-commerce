from sklearn.metrics.pairwise import cosine_similarity
import gensim
from gensim.models.doc2vec import Doc2Vec
import os 
import pickle
this_dir, this_filename = os.path.split(__file__)  # Get path of data.pkl
data_path = os.path.join(this_dir, 'embeddings.pickle')
with open(data_path, 'rb') as fin:
    description_embeddings= pickle.load(fin)

this_dir, this_filename = os.path.split(__file__)  # Get path of data.pkl
data_path = os.path.join(this_dir, 'indice.pickle')
with open(data_path,'rb') as fin:
    indices= pickle.load(fin)

this_dir, this_filename = os.path.split(__file__)  # Get path of data.pkl
data_path = os.path.join(this_dir,"product.model")
model = Doc2Vec.load(data_path)
def find_similar_products(product: str, products_catalogue: list,n_similar: int,method: str):
  if (n_similar<= len(products_catalogue)):
    a=indices[product]
    list_indices=list ()
    list_similar=list ()
    for i in products_catalogue:
      x=indices[i]
      list_indices.append(x)
  
    for i in list_indices :
      if (method=="bert_approach"):
        d=cosine_similarity(
        [description_embeddings[a]],
        [description_embeddings[i]])
        list_similar.append(d)
      elif (method=="doc2vec_approach"):
        d=model.docvecs.similarity(a,i)
        list_similar.append(d)
      else : 
        print("not valid method: the name of the method should be doc2vec_approach or bert_approach")
        break

    dictionary_product = dict(zip(products_catalogue,list_similar)) 
    dictionary_product_sotred= dict(sorted(dictionary_product.items(), key=lambda item: item[1], reverse=True))
    similar_product=list (dictionary_product_sotred.keys())
    similarity_indice=list ( dictionary_product_sotred.values())
    res=  (similar_product[:n_similar],similarity_indice[:n_similar])
    print(res)
  else:
    print("number of similar products should be smaller than the number of all the products")
    


  
 
  
