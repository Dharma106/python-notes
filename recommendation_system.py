# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 14:12:07 2019
"""

import math

#%%
data = {
	'Alan Perlis': { 
		'Artificial intelligence': 1.46, 
		'Systems programming': 5.0, 
		'Software engineering': 3.34, 
		'Databases': 2.32
	},

	'Marvin Minsky': { 
		'Artificial intelligence': 5.0, 
		'Systems programming': 2.54,
		'Computation': 4.32, 
		'Algorithms': 2.76
	},

	'John McCarthy': { 
		'Artificial intelligence': 5.0, 
		'Programming language theory': 4.72, 
		'Systems programming': 3.25, 
		'Concurrency': 3.61, 
		'Formal methods': 3.58,
		'Computation': 3.23, 
		'Algorithms': 3.03 
	},

	'Edsger Dijkstra': { 
		'Programming language theory': 4.34, 
		'Systems programming': 4.52,
		'Software engineering': 4.04, 
		'Concurrency': 3.97,
		'Formal methods': 5.0, 
		'Algorithms': 4.92 
	},

	'Donald Knuth': { 
		'Programming language theory': 4.33, 
		'Systems programming': 3.57,
		'Computation': 4.39, 
		'Algorithms': 5.0 
	},

	'John Backus': { 
		'Programming language theory': 4.58, 
		'Systems programming': 4.43,
		'Software engineering': 4.38, 
		'Formal methods': 2.42, 
		'Databases': 2.80 
	},

	'Robert Floyd': { 
		'Programming language theory': 4.24, 
		'Systems programming': 2.17,
		'Concurrency': 2.92, 
		'Formal methods': 5.0, 
		'Computation': 3.18, 
		'Algorithms': 5.0 
	},

	'Tony Hoare': { 
		'Programming language theory': 4.64, 
		'Systems programming': 4.38,
		'Software engineering': 3.62, 
		'Concurrency': 4.88,
		'Formal methods': 4.72, 
		'Algorithms': 4.38
	},

	'Edgar Codd': { 
		'Systems programming': 4.60, 
		'Software engineering': 3.54,
		'Concurrency': 4.28, 
		'Formal methods': 1.53, 
		'Databases': 5.0
	},

	'Dennis Ritchie': { 
		'Programming language theory': 3.45, 
		'Systems programming': 5.0,
		'Software engineering': 4.83,
	},

	'Niklaus Wirth': { 
		'Programming language theory': 4.23, 
		'Systems programming': 4.22,
		'Software engineering': 4.74, 
		'Formal methods': 3.83, 
		'Algorithms': 3.95
	},

	'Robin Milner': { 
		'Programming language theory': 5.0, 
		'Systems programming': 1.66,
		'Concurrency': 4.62, 
		'Formal methods': 3.94,
	},

	'Leslie Lamport': { 
		'Programming language theory': 1.5, 
		'Systems programming': 2.76,
		'Software engineering': 3.76, 
		'Concurrency': 5.0,
		'Formal methods': 4.93, 
		'Algorithms': 4.63
	},

	'Michael Stonebraker': { 
		'Systems programming': 4.67, 
		'Software engineering': 3.86,
		'Concurrency': 4.14, 
		'Databases': 5.0,
	},
}
  
#%%    
"""
Euclidean distance between two points is the length of the line segments connecting
those points.

In recommondation system case, to say two person belong to certian preferences
if and only if, they have ranked two items that defines the preference space.
So we define a preference space for each pair of distinct items, and the points
in the preference space, are given by the people than ranked the two items.
 
we can define the istance between the two people in the preference space as we
define the distance between a pair of points in the plane.

if d(person[i], person[j]) is small, then person[i] is similar to person[j].
In order to get a metric which can tell how similar the two people are we can get 
a number which will be the proportional to similarity of(distance between)
person[i] and person[j].

euclidean smiliarity = 1/[1+ d(person(i), person(j))] lies betwwen [0,1]

The closet to one this metric is, the closet person[i] is to person[j] by similarity.
 
"""
 
#%%   
# algorithm to compute the euclidean similarity

def euclidean_similarity(person1, person2, data):
    common_ranked_items = [itm for itm in data[person1] if itm in data[person2]]
    item_rankings = [(data[person1][itm], data[person2][itm]) for itm in common_ranked_items]
    distance = [pow((rank[0]- rank[1]), 2) for rank in item_rankings]
    return 1/(1 + sum(distance))
    
#%%
"""
The major flow of the Euclidean distance based comparison is that if the whole
distribution of rankings of a person tends to be higher than the other persons,
this metric would classify them as dissimilar without regard the correlation 
between two people. It is likely that there can be a perfect correlation if
the difference between the rankings are consistent.

"""    

#%%
"""
Pearson Correlation Coefficient (PCC) Algorithm in recommender system helps in 
understanding how related two people are based on the items they both 
have ranked.
PCC helps us find to similarity of a pair of users. In this approach, rather than
using the distance between the rankings on two products, we can consider the 
correlation between the users rating.

"""    

#%%
# pearson correlation coefficient algorithm

def pearson_similarity(person1, person2, data):
    common_ranked_items = [itm for itm in data[person1] if itm in data[person2]]
    tot_nos = len(common_ranked_items)
    # calculate the sum of individual person ratings for common_ranked_items
    sum_rate_per1 = sum([data[person1][itm] for itm in common_ranked_items])
    sum_rate_per2 = sum([data[person2][itm] for itm in common_ranked_items])
    
    # cacluate the sum of square for each peron common item ratings.
    sum_sqr_rate_per1 = sum([pow(data[person1][itm], 2) for itm in common_ranked_items])
    sum_sqr_rate_per2 = sum([pow(data[person2][itm], 2) for itm in common_ranked_items])
    
    rating_prod_sum = sum([data[person1][itm] * data[person2][itm] for itm in common_ranked_items])
    
    numerator = tot_nos * rating_prod_sum - (sum_rate_per1 * sum_rate_per2)
    denominator = math.sqrt((tot_nos * sum_sqr_rate_per1 - math.pow(sum_rate_per1,2)) \
                           * (tot_nos * sum_sqr_rate_per2 - math.pow(sum_rate_per2,2)))    
    return (numerator/denominator) if denominator != 0 else 0


#%%    
"""
The logic behind a recommondation system is to measure everyone against a given person
and find the closet persons to that specific person which can be evaluated by taking those
person whose distance is small, or the similarity value is high.

This approach helps to predict what's going to be the rating if the person rates
a group of the products he has not rated yet.

Most used approach, to this problem is to take the ratings of all the users 
and multiply them to see how similar they are to specific person by rating that
they gave to the product. If the product is very popular, and it has been rated 
by many people, it would have a higher weight, to normalize this behaviour, we
need to divide the weight by the sum of all the similarities for the people
that have rated the product. 
 
(As the different person will have a different rating notion, so   )

"""

#%%

def recommondation(data, person, limit_rating, similarity):
    # calculate the similarity scores of given person with respect to
    # other remaining person where both have rated the items
    scores=[(similarity(person, other, data), other) \
            for other in data if other != person]
    
    scores.sort()
    scores.reverse()
    scores = scores[0:limit_rating]
    
    temp_scores = []
    for itm in scores:
        if itm[0] != 0:
            temp_scores.append(itm)
    scores = temp_scores
    
    recommend = {}
    
    for similarity_score, other in scores:
        ranked = data[other]
        
        for itm in ranked:
            if itm not in data[person]:
                weight = similarity_score * ranked[itm]
                
                if itm in recommend:
                    s, weights = recommend[itm]
                    recommend[itm] = (s + similarity_score, weights + [weight])
                else:
                    recommend[itm] = (similarity_score, [weight])
    
    for reco_itm in recommend:
        similairty, itm_rating = recommend[reco_itm]
        recommend[reco_itm] = sum(itm_rating)/similairty
        
    return recommend
    
    
    
#%%    

