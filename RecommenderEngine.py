'''
Created on Nov 29, 2015

@author: carlylevi
'''
import SimpleFoodReader
import json
import operator

def match_zero(list, dictionary):
    dict = {}
    n = 0
    for i in list:
        dict[i] = []
        for key in dictionary:
            if dictionary[key][n] != 0:
                dict[i].append(dictionary[key][n])
        n += 1
    return dict

def match(list, dictionary):
    dict = {}
    n = 0
    for i in list:
        dict[i] = []
        for key in dictionary:
            dict[i].append(dictionary[key][n])
        n += 1
    #print dict
    return dict


def averages(items, ratings):
    dict = match_zero(items, ratings)
    for key in dict:
        sum = 0
        for i in dict[key]:
            sum += int(i)
            length = len(dict[key]) + 1
        dict[key] = float(int(sum))/(int(length))
    final = [(key, dict[key]) for key in dict]
    final = sorted(final, key = operator.itemgetter(1), reverse = True)
    #print final
    return final

def dotproduct(list1, list2):
    sum = 0
    for i in range(len(list1)):
            sum += int(list1[i])*int(list2[i])
    return sum

def similarities(name, ratings):
    dict = ratings
    list = []
    for i in dict:
        if i != name:
            dp = dotproduct(dict[name], dict[i])
            person = (i, int(dp))
            list.append(person)
    list2 = sorted(list)
    #print sorted(list2, key = operator.itemgetter(1), reverse = True)
    return sorted(list2, key = operator.itemgetter(1), reverse = True)

def scores(slist,items,ratings,n):
    slist = slist[:n]
    #print closeratings
    list = []
    for i in items:
        list.append([i,0])
        #print list
    for i in slist:
        name = i[0]
        value = ratings[name]
        weight = i[1]
        for x in range(len(value)):
            num = value[x] * weight
            list[x][1] += num
        break
    list = sorted(list)
    list = sorted(list, key=operator.itemgetter(1), reverse = True)
    tuplelist = []
    for i in list:
        i = tuple(i)
        tuplelist.append(i)
    print tuplelist

def recommend(name,items,ratings,count):
    slist = similarities(name, ratings)
    x = scores(slist, items, ratings, count)
    list = []
    personratings = ratings[name]
    for i in range(len(personratings)):
        if personratings[i] == 0:
            list.append(items[i])
    newList = []
    for i in x:
        if i >= 0 and i[0] in list:
            newList.append(i)
    return newList

(items,ratings) = SimpleFoodReader.getData("foodratings_example.txt")
items = json.loads(items)
ratings = json.loads(ratings)
