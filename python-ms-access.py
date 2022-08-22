# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:29:28 2022

@author: abaker
"""
#this python library lets you access Microsoft Access databases
import pyodbc

conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=yourfilepathhere\DogPersonalities.accdb;')
cursor = conn.cursor()
cursor.execute('select * from dogPersonalities')
   
for row in cursor.fetchall():
    print (row)