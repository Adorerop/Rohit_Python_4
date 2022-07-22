'''Write a Python script to sort (ascending and descending) a dictionary by
value'''
import operator
d={1:52,2:4444,3:54,4:0,5:542}
print('Original dictionary : ',d)
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1)))
print('Dictionary in ascending order by value : ',sorted_d)
sorted_d = dict( sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)