#!/usr/bin/env python

# Load required libraries
import requests
import json
import datetime
import time
import MySQLdb
from evohomeclient2 import EvohomeClient


client = EvohomeClient('evohome_username', 'evohome_password')
# Open database connection
db = MySQLdb.connect("127.0.0.1","username","password","name_mysql_database",port )

# prepare a cursor object using cursor() method
cursor = db.cursor()
    
for device in client.temperatures():
    print device['name']
    print device['temp']
    # Prepare SQL query to INSERT a record into the database.
    if (device['name'] == "Livingroom"):
        temp1 = float(device['temp'])
    if (device['name'] == "Bathroom"):
        temp2 = float(device['temp'])
    if (device['name'] == "Kitchen"):
        temp3 = float(device['temp'])
    if (device['name'] == "Office"):
        temp4 = float(device['temp'])
        
sql = "INSERT INTO EvohomeTemperatures(Livingroom, Bathroom, Kitchen, Office) VALUES ('%f', '%f', '%f', '%f')" % (temp1, temp2, temp3, temp4)
try:
    # Execute the SQL command
    cursor.execute(sql)
    # Commit your changes in the database
    db.commit()
except:
    # Rollback in case there is any error
    print "Error adding value"
    db.rollback()

# disconnect from server
db.close()