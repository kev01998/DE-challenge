import csv
import json
import pymysql

# connect to  pymysql database
mydb = pymysql.connect(host='localhost',
    user='root',
    passwd='password',
    db='codetest')

#read the CSV data file places into the table places 
cursor = mydb.cursor()   
with open(r'data\places.csv', encoding="utf8") as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader: 
    cursor.execute('Insert INTO places(city,county,country) values(%s,%s,%s)',row)
mydb.commit()
cursor.close()


#read the CSV data file people into the table people 
cursor = mydb.cursor()   
with open(r'data\people.csv', encoding="utf8") as csv_file:
  reader = csv.reader(csv_file)
  next(reader)
  for row in reader: 
    cursor.execute('Insert INTO people(given_name,family_name,date_of_birth,place_of_birth) values(%s,%s,%s,%s)',row)
mydb.commit()
cursor.close()


#Loading data from json to table json_table 
cursor = mydb.cursor()
json_data = json.load(open(r'data\readjson_output.json', encoding="utf8"))
for item in json_data:
  person=item.get("person")
  year=item.get("year")
  cursor.execute('Insert into tbjson(person,year) values(%s,%s)', (person,year))
mydb.commit()
cursor.close()


#output the table to a JSON file
cursor = mydb.cursor()
sql = "select places.country, count(people.given_name) from places inner join people on places.city = people.place_of_birth group by country"
cursor.execute(sql)
rows = cursor.fetchall()
with open(r'data\summary_output.json', 'w') as json_file:
    rows = [{'country':row[0], 'no_of_people_born':row[1]} for row in rows]
    json.dump(rows, json_file)
mydb.commit()
cursor.close()


#output the table to a CSV file
cursor = mydb.cursor()
sql = "select places.country, count(people.given_name) from places inner join people on places.city = people.place_of_birth group by country"
cursor.execute(sql)
rows = cursor.fetchall()
with open(r'data\handsonc_output.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(rows)
mydb.commit()
cursor.close()


#output the csv file to json file
rows = csv.reader(open(r'data\people.csv', encoding="utf8"))
next(rows)
with open(r'data\cToJ_output .json', 'w') as json_file:
    rows = [{'given_name':row[0], 'family_name':row[1], 'date_of_birth' : row[2], 'place_of_birth':row[1]} for row in rows]
    json.dump(rows,json_file)
mydb.commit()

