#!/usr/bin/env python


import pymysql
import csv
import json

mydb = pymysql.connect(host='localhost',
    user='root',
    passwd='password',
    db='codetest')
#cursor = mydb.cursor()

# read the CSV data file places into the table places
#csv_data = csv.reader(open(r'C:\Users\KevinAiwala\Downloads\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\DE challenge\data\places.csv',encoding="utf8"))
#next(csv_data)
#for row in csv_data:
  #cursor.execute('Insert INTO places(city,county,country) values(%s,%s,%s)',row)
#mydb.commit()
#cursor.close()

# read the CSV data file people into the table people
#cursor = mydb.cursor()
#csv_data = csv.reader(open(r'C:\Users\KevinAiwala\Downloads\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\DE challenge\data\people.csv',encoding="utf8"))
#next(csv_data)
#for row in csv_data:
  #cursor.execute('Insert INTO people(given_name,family_name,date_of_birth,place_of_birth) values(%s,%s,%s,%s)',row)
#mydb.commit()
#cursor.close()

#Loading data from json to table json_table 
#cursor = mydb.cursor()
#json_data = json.load(open(r'C:\Users\KevinAiwala\Downloads\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\DE challenge\data\sample_output.json', encoding="utf8"))

#for item in json_data:
  #person=item.get("person")
  #year=item.get("year")
  #cursor.execute('Insert into `json_table`(country,year) values(%s,%s)', (person,year))
#mydb.commit()
#cursor.close()   

#output the table to a JSON file
#cursor = mydb.cursor()
#sql = "select places.country, count(people.given_name) from places inner join people on places.city = people.place_of_birth group by country"

#cursor.execute(sql)
#rows = cursor.fetchall()
#for row in rows:
  #print(row[0])
#with open(r'C:\Users\KevinAiwala\Downloads\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\DE challenge\data\handson_output.json', 'w') as json_file:
  #rows = [{'country':row[0], 'no_of_people_born':row[1]} for row in rows]
  #json.dump(rows, json_file)
 
#mydb.commit()
#cursor.close()
   
 #output the table to a csv file
#cursor = mydb.cursor()
#sql = "select places.country, count(people.given_name) from places inner join people on places.city = people.place_of_birth group by country"


#cursor.execute(sql)
#rows = cursor.fetchall()
#for row in rows:
  #print(row[0])
#with open(r'C:\Users\KevinAiwala\Downloads\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\DE challenge\data\handsonc_output.csv', 'w') as csv_file:
  #writer = csv.writer(csv_file)
  #writer.writerows(rows)
#mydb.commit()
#cursor.close()

#output the csv file to json file
cursor = mydb.cursor()
rows = csv.reader(open('data\people.csv',encoding="utf8"))
next(rows)
with open(r'C:\Users\KevinAiwala\Downloads\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\Solution_DE-Challenge_Kevin-main\DE challenge\data\cToJ_output .json', 'w') as json_file:
  rows = [{'given_name':row[0], 'family_name':row[1], 'date_of_birth' : row[2], 'place_of_birth':row[1]} for row in rows]
  json.dump(rows,json_file)
mydb.commit()
cursor.close()  
  