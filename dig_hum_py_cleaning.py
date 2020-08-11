# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os 
import pandas as pd

os.chdir('C:\\Users\\shimm\\downloads')


# plague_by_word = open("plague_by_word.txt", "w")
#new_plague = open("newplague.txt", "w")
with open("Camus Albert - The Plague.txt") as f:
    flat = f.readlines()
for line in range(len(flat)) :
     if flat[line] != "\n":
         words = flat[line].split(" ")
         for word in words:
             if word != "\n":
                new_plague.write(word + "\n")
#the seperated files of parts where created manually from new_plague.txt
df_part_1 = pd.read_csv("plague_part_1_new", sep="\n", encoding='latin-1')
df_part_2 = pd.read_csv("plague_part_2_new", sep="\n", encoding='latin-1')
df_part_3 = pd.read_csv("plague_part_3_new", sep="\n", encoding='latin-1')
df_part_4 = pd.read_csv("plague_part_4_new", sep="\n", encoding='latin-1')
df_part_5 = pd.read_csv("plague_part_5_new", sep="\n", encoding='latin-1')

p1_lst = ["part_1"] * len(df_part_1)
p2_lst = ["part_2"] * len(df_part_2)
p3_lst = ["part_3"] * len(df_part_3)
p4_lst = ["part_4"] * len(df_part_4)
p5_lst = ["part_5"] * len(df_part_5)
 
df_part_1["part"] = p1_lst
df_part_2["part"] = p2_lst
df_part_3["part"] = p3_lst
df_part_4["part"] = p4_lst
df_part_5["part"] = p5_lst

df = pd.concat([df_part_1, df_part_2, df_part_3, df_part_4, df_part_5])
df['count'] = range(1, len(df) + 1)
df["new_column"] = df['Word'].str.replace('[^\w\s]','')    
df= df.applymap(lambda s:s.lower() if type(s) == str else s)

df.to_csv("plague_by_part_by_word.csv")





