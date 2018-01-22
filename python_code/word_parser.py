# -*- coding: utf-8 -*-
'''
word-parser takes all the descriptions from wines.csv and count how many times a word appears and the points related
with the descrived words.

'''
import csv,re

#function to make sure that puntuation marks doesn't affect to the results
def textparser(t):
    t=t.lower()
    '''
    t=t.replace(".","")
    t=t.replace(",","")
    t=t.replace(";","")
    t=t.replace(".","")
    t=t.replace("?","")
    t=t.replace("!","")'''
    t=t.replace("'s","")
    t=re.sub("[\.,;\?!&()']","",t)
    t=re.sub('\d+–\d+',"",t)#avoid some number combinations on the sample
    return t
#words that aren't interesting for wine description
excluded_words = ["and","the","this","is","a","with","of","in","wine","to","on","it","drink","but","it's","that","from",\
   "finish","by","are","for","has","an","its","now","offers","though","as","shows","while","more","very","at","well"\
   "not","there's","alongside","years","opens","just","bit","so","made","slightly","there","over","than","some","into"\
   "or","also","what","straightforward","same","two","overall","about","vineyards",'or','plum','nose','up','all','along'\
    ,'like','one','flavors','notes','texture','aroma','aromas','rich','plenty','drinking','drink','will','be','quite',\
    'good','well','yet','make','tastes','here','that','ready','comes','out','s']

with open('wines.csv', 'r', encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile, delimiter=",", quotechar='"')
    #"id","title","description","points","price","variety","winery","id_taster","id_location"
    
    wordsDicc = {}
    words = []
    #GET THE NUMBER OF REPETICIONS OF A WORD AND THE AVERAGE OF PUNTUACION FOR THAT WINES THAT ARE DESCRIBED WITH THIS WORD   
    for row in reader:
        if row[0]!='id':
            words=row[2].split(" ")
            points=int(row[3])
            words=[textparser(w) for w in words]
            for word in words:
                if word not in excluded_words and not(word.isdigit()):
                    if wordsDicc.get(word)==None:
                        wordsDicc[word]= [1,points,points]
                    else:
                        [q,p,avg]=wordsDicc.get(word)
                        q+=1
                        p=p+points
                        avg =  float('{:5.3f}'.format(p/q))
                        wordsDicc[word]=[q,p,avg]
wordsList=[]
#ORDER BY GREATER AVERAGE PUNTUATION FOR WORD
for key, value in wordsDicc.items():
    [q,p,avg]=value
    if q>=9:
        wordsList.append((avg,p,q,key))#lista de tuples con la clave invertida   
wordsList.sort(reverse=True)#ordena por el numero más grandes

#TOP 3 BY AVG
print(wordsList[:3])

#SAVE THE INFORMATION ON A CSV
with open('ranking_words.csv', 'w',newline="\n",encoding="utf-8") as csvfile:
    fieldnames = ["words",'avg_points','total_points',"quantity"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames,  quoting=csv.QUOTE_NONNUMERIC)
    writer.writeheader()#escriu el header
    for avg_p,total_p,quantity,w in wordsList:
        writer.writerow({'words': w, 'avg_points':avg_p,'total_points':total_p,'quantity': quantity})