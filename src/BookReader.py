'''
Created on Nov 29, 2015

@author: carlylevi
'''
import json

def readDatafile (filename):
    f = open(filename)
    result = [ line.strip().split(',') for line in f.readlines() if len(line) > 1 ]
    f.close()
    return result


# PRIMARY MODULE FUNCTION
def getData (filename):
    """
    given the name of a file of data about restaurant ratings, 
      returns two sequences: a list of strings, the restaurant names in file order,
      and a dictionary of strings as the key and a list of ints as the values, the
      raters and their ratings of the books
    """
    data = readDatafile(filename)
    itemlist = []
    for item in data:
        itemlist.extend([item[i] for i in range(1, len(item), 2)])
        break
    ratingsDict = {}
    for i in data:
        ratings = []
        ratings.extend(i[x] for x in range(2,len(i),2))
        if i[0] not in ratingsDict:
            ratingsDict[i[0]] = ratings 
    return (json.dumps(itemlist), json.dumps(ratingsDict))

if __name__ == "__main__":
    (items,ratings) = getData("bookratings.txt")
    print"items = ",items
    print"ratings = ", ratings
  
    print type(items), type(ratings)
    var = json.loads(items)
    print type(var),var
    dvar = json.loads(ratings)
    print type(dvar),dvar
