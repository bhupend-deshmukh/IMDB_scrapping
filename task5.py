import json,requests
from task1 import *
from bs4 import BeautifulSoup
from pprint import pprint

lisssss=[]
def movie_details(link__):
    number=1
    for ii in link__:

        data=requests.get(ii).text
        dicp={}
        dicp1={}
        director_lst=[]
        language_=[]
        bio_list=[]
        genre=[]
        
        data=BeautifulSoup(data,"html.parser")
        ge=data.find('li',{"data-testid":"storyline-genres"})
        nre=ge.find('ul',class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base")
        for i in nre:
            a=i.get_text()
            genre.append(a)

        bio=data.find('p').get_text()
        bio_list.append(bio)
        director=data.find('a',class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text   
        name=data.find(class_="TitleHeader__TitleText-sc-1wu6n3d-0 dxSWFG").text
        director=data.find('a',class_="ipc-metadata-list-item__list-content-item ipc-metadata-list-item__list-content-item--link").text
        director_lst.append(director)
        timeClass=data.find('ul',role="presentation").get_text().split(" ")

        hou=int(timeClass[0][-2:-1])
        hourss=hou*60
        mi=''
        for j in timeClass[1]:
            if j.isdigit():
                mi+=j
        mintt=int(mi)
        runtime=hourss+mintt
        
        
        lng=data.findAll("div",class_="styles__MetaDataContainer-sc-12uhu9s-0 cgqHBf")
        for i in lng:
            prin=(i.findAll("a"))
            for i in prin:
                if "country" in str(i):
                    vvv=i.text
                    
                if "language" in str(i):
                    language_.append(i.text)
        dicp['movie name']=name
        dicp['country']=vvv
        dicp['language']=language_
        dicp['runtime']=runtime
        dicp['director']=director
        dicp['genre']=genre
        dicp['bio']=bio
        dicp1[number]=dicp
        # print(dicp1)
        lisssss.append(dicp1)
        number+=1
    with open("task5.json",'w') as c:
        json.dump(lisssss,c,indent=4)
    return lisssss
p=movie_details(link[:30])
# print(p)           

