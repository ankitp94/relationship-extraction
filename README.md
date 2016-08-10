# Implementation Project
# Kernel Methods for Relation Extraction 

We have implemented the paper [Kernel Methods for Relation Extraction](www.jmlr.org/papers/volume3/zelenko03a/zelenko03a.pdf) by Dmitry Zelenko  et. al.

Due to lack of benchmarking dataset available  to reproduce the result, we have used Google's [Relation Extraction database](https://research.googleblog.com/2013/04/50000-lessons-on-how-to-read-relation.html) to create a small dataset of around 700 sub-examples.


Making use of the flexibility provided by the kernel function framework proposed by authors, we modified text_similarity function of paper to neglect the text of entities and names while comparing text to  to achieve better results on our dataset. 

To compare it with other kernels, we also implemented another tree kernel which ignores the text while matching. 


### Code Structure

The data structure used by us is that each example is saved as  node_list,adjacency,word_lemma_role 
The code structure is as follows

- makeParseTree.py and make_tree.py are used to save each sub-example as node,list and adjacency matrix and role_list.

- kernel1.py , kernelSparse1.py defines the kernel as per paper.
	- uncomment the first if block in fucntion 'k' in each of the above to neglect the text of entities to increase the accuracy for this case.  

- Matrix.py
	- Calls kernel1.py and kernelSparse1.py to calculate the grammian matrix for given value of lambda or type of kernel - sparse or contiguous.

- newkernel.py
	- Implements a kernel which only takes the grammatical structure into account.
	- [Making tree kernels practical for natural language learning](http://www.aclweb.org/anthology/E06-1015)

- 'optimized' in fileName suggests an optimized implementation of the kernel fucntion.

- Python notebook 'gram_matrix_svm.ipynb' was used to generate the results reported in paper.

- Python notebook 'parse_and_save_dataset.ipynb' was used to craete the sub-examples from the google database.

- Provide your api_key in create_dataset.py to download database from google.

- final_list_of_subexamples.pickle and y736.pickle contains correspdnding lists of the sub-examples and output_labels respectively and hence, constitute our the training data. 

### Team Members
Ankit Pensia, Rajat Panda and Sai Krishna
