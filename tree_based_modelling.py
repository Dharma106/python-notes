# Decision tree is a type of supervised learning algorithm (having a pre-defined
# target variable) that is mostly used in classification porblems. It works for
# both categorical and continuous input and output variable. 

# In this technique we split the population or sample into two or more
# homogeneous sets (or sub-populations) based on the most significant splitter /
# differntiator in input variables.

# Types of Decision tree
#    1. Categorical Variable Decision tree: The decision tree which has categorical
#       target variable is referred as categorical variable decision tree.
#    1. Continuous Variable Decision tree: The decision tree which has continuous 
#       target variable is referred as categorical variable decision tree.

# Advantage of decision tree based model
# 1. Easy to understand : Decision tree is easy to understand. It's graphical
#   representation is very intitutive and users can easily relate their 
#   hypothesis.
# 2. Useful in data exploration : One of the fastest way to identify most significant
#   variables and relation between two or more variables. 
# 3. Less data cleaning required: It requires less data cleaning compared to 
#   some other modeling techniques. It is not influenced by outliers and 
#   missing values to a fair degree.
# 4. Data type is not a constraint: It can handle both numerical and categorical 
#   variables.
# 5. Non Parametric Method: Decision tree is considered to be a non-parametric 
#   method. This means that decision trees have no assumptions about
#   the space distribution and the classifier structure.

# Disadvantages
# 1. Over fitting: Over fitting is one of the most practical difficulty for
#    decision tree models. This problem gets solved by setting constraints
#    on model parameters and pruning.
# 2. Not fit for continuous variables: While working with continuous numerical
#    variables, decision tree looses information when it categorizes variables
#    in different categories.


# Information Gain: 
# A less impure node requires less information to describe it and more impure node
# requires more information. 
# Information theory is a measure to define the disorganization in a system which is
# called as "Entropy".
# If the sample is completely homogenous (of the same kind), then entropy is zero and
# if the sample is equally divided, it has entropy of 1. 
# Entropy =  -p* log2(p) - q*log2(q)

# entropy is calculated as 
from math import log2
p = 0.2 # probability of success
q = (1-p) # probability of failure
entropy =  -p* log2(p) - q*log2(q)
entropy
# this entropy can be used with the categorical target variable. It choose the split
# has the lowest entropy compared to parent node and other splits. The lesser the 
# entropy the better it is  

# Steps to calculate entropy for a split:
#   step1: calculate the entropy of parent node.
#   step2: calculate the entropy of each individual split and calcuate the 
#           weighted average of all the sub-nodes available in split.

# Information gain from the entropy is (1- entropy)


# key Parmeters of tree modelling and things to aviod overfitting
#   if there is no limit set to decision tree, it will give 100% accuracy on
#   training set because in worse case it will end up making 1 leaf for each observation
#   The things to be conisder while making tree is 
#       a) setting constrains on tree size
#       b) Tree Pruning

# Parmeters used for defining a tree are as follows:
# 1) Minimum samples for a node split
#   * define the minimum number of samples (observation) which are required in a
#     node to be considered for splitting. 
#   * This is done to control over-fitting. higher values prevent a model from 
#      learning relations which might be highly specific to a particular sample
#      selected for a tree.
#   * Too high values can lead to under-fitting hence, it should be tuned
#      with CV (cross-validation).
    
# 2) Minimum samples for a terminal node (leaf)
#   * define the minimum number of samples (observation) which are required in a 
#     node to be considered for splitting. 
#   * This is done to control over-fitting. higher values prevent a model from 
#      learning relations which might be highly specific to a particular sample
#      selected for a tree.
#   * Too high values can lead to under-fitting hence, it should be tuned
#      with CV (cross-validation).
   


# tree based modelling using "sklearn"
# import other data wraggling libraries such as numpy, pandas and so on
from sklearn import tree
# Now call the predictor variable say x_train and dependent or target variable y_trian
# from already created training data variable.

# create a tree object
model = tree.DecisionTreeClassifier(criterion = 'gini') 
# for classification, the lgorithm can be changed from gini to entropy. Here default
# is set to be gini.
# for regression type
# model = tree.DecisionTreeRegressor(criterion= 'mse')

# Next step is to train the training data set and checks score
x_train = 'training_independent_var' # change the value
y_train = 'training_dependent_var' # change the value
model.fit(x_train, y_train)
model.score(x_train, y_train)

# read the test data to predict the accuracy
x_test = "test_data"
# predict the output
predicted = model.predict(x_test) 

