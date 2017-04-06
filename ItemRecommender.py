'''
Created on Nov 29, 2015

@author: carlylevi
'''
import RecommenderEngine 
import json
import BookReader
import operator

if __name__ == "__main__":
    (jitems,jratings) = BookReader.getData("bookratings.txt")
#    print "items = ",jitems
#    print "ratings = ", jratings
    items = json.loads(jitems)
    ratings = json.loads(jratings)
    
    avg = RecommenderEngine.averages(items,ratings)
    avg = sorted(avg, key = operator.itemgetter(1), reverse = True)
    print "Here are some movies you should watch", avg[:10]
    print "This is a movie you wouldn't like", avg[-1]
#     
#    for key in ratings:
#        slist = RecommenderEngine.similarities(key,ratings)
#         print key,slist
#        print "\t",RecommenderEngine.scores(slist,items,ratings,1)
#        print "\t",RecommenderEngine.scores(slist,items,ratings,len(slist))
    