# -*- coding: utf-8 -*-


import pandas as pd

df = pd.read_csv("star_with_gravity.csv")
df.head()

df.drop(['Unnamed: 0'],axis =1,inplace=True)

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
#convert  df["Distance"] to list and assign to variable dist
Distance=df['Distance'].to_list()
#convert  df["Gravity"] to list and assign to variable gravity
gravity=df['Gravity'].to_list()


# initialize final_star_list  as empty []
final_star_list=[]
temp_dict ={}
for i in range(0,len(name)):
    temp_dict["name"]=name[i]
    temp_dict["mass"]=mass[i]
    # use temp_dict["radius"] to assign radius[i]
    # use temp_dict["distance"] to assign dist[i]
    temp_dict["gravity"]= gravity[i]
    final_star_list.append(temp_dict)
    temp_dict ={}
print(final_star_list)
