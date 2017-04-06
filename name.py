'''
Created on Dec 2, 2016

@author: carlylevi
'''

x = [[1,2,3], [1,2,3], [1,2,3]]
dict = {}

for i in range(len(x)):
    for j in range(i): 
        print j
        if j not in dict:
            dict[i] = j
        else:
            dict[i] += j
            
print dict
        
