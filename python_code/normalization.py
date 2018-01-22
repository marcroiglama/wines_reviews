# -*- coding: utf-8 -*-

'''
normalization.py reads winemag-data-130k-v2.csv, the original dataset, and separates into 3 cvs. location.csv contains
province and country info, taster.csv contains taster names and wines.csv all the other relevant info.
'''
import csv

with open('winemag-data-130k-v2.csv', 'r', encoding="utf-8") as inp, open('wines.csv','w',newline='\n',encoding='utf-8') as out:
    reader = csv.reader(inp, delimiter=",", quotechar='"')
    #[0-'id', 1-'country', 2-'description', 3-'designation', 4-'points', 
    # 5-'price', 6-'province', 7-'region_1', 8-'region_2', 9-'taster_name', 
    # 10-'taster_twitter_handle', 11-'title', 12-'variety', 13-'winery']


#CREATE WINES INFORMATION CSV    
    fieldnames = ["id","title","description","points","price","variety","winery","id_taster","id_location"]
    writer = csv.writer(out, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(fieldnames)

    with open('location.csv', 'w',newline="\n",encoding="utf-8") as location,open('taster.csv', 'w',newline="\n",encoding="utf-8") as tasters_csv:
    #CREATE LOCATION INFORMATION CSV
        fieldnames3 = ["id_province","province","country"]
        writer_loc = csv.DictWriter(location, fieldnames=fieldnames3,  quoting=csv.QUOTE_NONNUMERIC)
        writer_loc.writeheader()#escriu el header
        id_province = 0
        provinces = []   
        provinces_list = []
    #CREATE TASTERS CSV INFORMATION 
        fieldnames2 = ["id_taster","taster_name","taster_twitter"]
        writer_taster = csv.DictWriter(tasters_csv, fieldnames=fieldnames2,  quoting=csv.QUOTE_NONNUMERIC)
        writer_taster.writeheader()#escriu el header
        id_taster = 0
        tasters = [] 
        tasters_list = []

    #FIll CSV INFORMATION
        for row in reader:
            if row[0]=='id'or row[0]==None:
                continue
            else:
                province = str(row[6])
                taster_name = str(row[9])
                if not(province in provinces):
                    if province == " ":
                        provinces.append(province)
                        provinces_list.append([0,province])
                        writer_loc.writerow ({'id_province':0,'province':" ",'country':' '})                                                        
                    else:
                        id_province +=1
                        provinces.append(province)
                        provinces_list.append([id_province,province])
                        writer_loc.writerow ({'id_province':id_province,'province':province,'country':str(row[1])}) 

                if not(taster_name in tasters):
                    if taster_name == " ":
                        tasters.append(taster_name)
                        tasters_list.append([0,taster_name])
                        writer_taster.writerow ({'id_taster':0,'taster_name':" ",'taster_twitter':None})
                    else: 
                        id_taster +=1
                        tasters.append(taster_name)
                        tasters_list.append([id_taster,taster_name])
                        writer_taster.writerow ({'id_taster':id_taster,'taster_name':taster_name,'taster_twitter':str(row[10])})
    #FILL WINES.CSV        
            winerow=[]
            winerow=[row[0],row[11],row[2],row[4],row[5],row[12],row[13]]
            for t in tasters_list:
                if row[9]==t[1]:
                    winerow.append(t[0]) 
            for l in provinces_list:
                if row[6]==l[1]:
                    winerow.append(l[0])      
            writer.writerow(winerow)
