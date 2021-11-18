import json

def analyse_movies_directors():
    with open('task5.json','r') as l:
        mm=json.load(l)
        Ankita_gole=0
        Hrishikesh_Mukherjee=0
        Sanjay_Leela_Bansali=0
        dict1={}

        for j in mm:
            for k in j.values():
                if 'Ankita gole' in k['director']:
                    Ankita_gole+=1
                if 'Hrishikesh Mukherjee' in k['director']:
                    Hrishikesh_Mukherjee+=1
                if "Sanjay Leela Bansali" in k['director']:
                    Sanjay_Leela_Bansali+=0
        
        dict1['Ankita gole']=Ankita_gole
        dict1['Hrishikesh Mukherjee']=Hrishikesh_Mukherjee
        dict1['Sanjay Leela Bansali']=Sanjay_Leela_Bansali
        with open('task7.json','w') as v:
            json.dump(dict1,v,indent=4)

m=analyse_movies_directors()
