## The embedding process

![alt text](images/embedding/image-3.png)

- Embeddings generate values from -1 to 1 ever ?
- We split the words in tokens based on rules could be space or something defined. This process of break sentences in tokens is call tokenization.
![alt text](images/embedding/image-6.png)
After that we define each word with embedding. Each dimension of embeddings means something and add this word in a positoin in the vector like this images/embedding/images


![alt text](images/embedding/image.png)


- This is the process that we can use to make our word -> token -> embedding. The same process could happen with document or sentences

![alt text](images/embedding/image-1.png)

- The question is, how this embeddings are related with context ? 
- we have attention decoder or context embedding, the context embedding dind't work very well to good ammount of words, because it's too much context to only one embedding, for this reason have the attention context

![alt text](images/embedding/image-2.png)

#### Representation Models
- BERT is a representation Model that use a transform encoder

![alt text](images/embedding/image-4.png)

#### Generative Models
![alt text](images/embedding/image-5.png)
- How tokenizer works with generative Models
![alt text](images/embedding/image-7.png)
- The number of tokens and the way that this works depending of tokenizer that you use