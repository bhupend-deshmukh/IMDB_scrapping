from task1 import *
import json
from pprint import pprint
def realeas_yr():
    year=[]
    for i in top250movies():
        for j in i:
            if i['year'] not in year:
                year.append(i['year'])
    year=sorted(year)
    movie_dict={i:[] for i in year}
    for i in top250movies():
        yr=i['year']
        for x in movie_dict:
            if str(x)==str(yr):
                movie_dict[x].append(i)
    return movie_dict
d=realeas_yr()

with open('task2.json','w') as v:
    json.dump(d,v,indent=4)
    