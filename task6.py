# import json,requests
# from task1 import *
# from bs4 import BeautifulSoup
# from pprint import pprint
# listP=[]

# def movie_details(link__):
#     listP=[]
#     am=1
#     for i1 in link__:   
#         data=requests.get(i1).text
#         dicp={}
#         dd={}
#         director_lst=[]
#         language_=[]
#         bio_list=[]
#         genre=[]
        
#         data=BeautifulSoup(data,"html.parser")
#         gen=data.find_all("div",class_="GenresAndPlot__ContentParent-cum89p-8 bFvaWW Hero__GenresAndPlotContainer-kvkd64-11 twqaW")
#         for i in gen:
#             pr=(i.find("span",class_="GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD").text)
#             bio_list.append(pr)
#             gg=i.findAll("a")
#             for i in gg:
#                 if "read all" in i.text:
#                     pass
#                 else:
#                     genre.append(i.text)
#         # print(genre)
#         # print()
#         # print("\n")
        
#         director=data.find('a',class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text   
#         name=data.find(class_="TitleHeader__TitleText-sc-1wu6n3d-0 dxSWFG").text
#         director=data.find('a',class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
#         director_lst.append(director)
#         timeClass=data.find('ul',role="presentation").text
#         length=len(timeClass)
#         j1=length-8
#         ll=timeClass[j1:]
        
#         lng=data.findAll("div",class_="styles__MetaDataContainer-sc-12uhu9s-0 cgqHBf")
#         for i in lng:
#             prin=(i.findAll("a"))
#             for i in prin:
#                 if "country" in str(i):
#                     vvv=i.text
                    
#                 if "language" in str(i):
#                     language_.append(i.text)
#         dicp['movie name']=name
#         dicp['country']=vvv
#         dicp['language']=language_
#         dicp['runtime']=ll
#         dicp['director']=director
#         dicp['genre']=genre
#         dicp['bio']=bio_list
#         dd[am]=dicp
#         am+=1
#         listP.append(dd)
#         print(dd)

#     with open('./scraping_data/task6.json','w') as c:
#         json.dump(listP,c,indent=4)
#     return listP

# nk=movie_details(link[:37])



import json

from task7 import analyse_movies_directors

def analyse_movies_language()
    with open('task5.json','r') as l:
        mm=json.load(l)
        Hindi=0
        English=0
        Malyalam=0
        dict1={}

        for j in mm:
            for k in j.values():
                if 'Hindi' in k['language']:
                    Hindi+=1
                if 'English' in k['language']:
                    English+=1
                if "Malyalam" in k['language']:
                    Malyalam+=1
        # print(Hindi)
        # print(English)
        # print(Malyalam)
        dict1['Hindi']=Hindi
        dict1['English']=English
        dict1['Malyalam']=Malyalam
        with open('task6.json','w') as v:
            json.dump(dict1,v,indent=4)
jj=analyse_movies_directors()