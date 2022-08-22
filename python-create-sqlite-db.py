# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 13:44:30 2022

@author: abaker
"""

# Import required libraries
import sqlite3
import pandas as pd
  
# Connect to SQLite database
#Pass the name of the database to be created inside this function.
conn = sqlite3.connect(r'yourfilepathhere\dogPersonalities.db')
  
# Load CSV data into Pandas DataFrame
# this only works with double slashes \\ with a Windows machine
personality_data = pd.read_csv('yourfilepathhere\\dogPersonalitiesCSV.csv')



# Write the data to a sqlite table
#create table
personality_data.to_sql('personality_ranking', conn, if_exists='replace', index=True)
#By default, the dataframe index is written as a column. 
#Simply toggle the index parameter to False in order to remove this column
#It needs to be True if you want your columns to have headers!
  


# Create a cursor object
cur = conn.cursor()
# Fetch and display result
for row in cur.execute('SELECT * FROM personality_ranking'):
    print(row)

"""In order to see the column headers in the conversion, I had to 
list them in the first 2 rows of the csv file.
I'm not sure why that is necessary"""


#Try any of these in your python editor! 
#for row in cur.execute('SELECT Breed FROM personality_ranking'):
#    print(row)    



#for row in cur.execute('SELECT Breed_Group FROM personality_ranking'):
#    print(row) 


#for row in cur.execute('SELECT AKC_Recognized FROM personality_ranking'):
#   print(row)   


#for row in cur.execute('SELECT Adaptability FROM personality_ranking'):
#    print(row)    

  
#for row in cur.execute('SELECT Trainability FROM personality_ranking'):
#    print(row)    


#for row in cur.execute('SELECT Affection_Level FROM personality_ranking'):
#    print(row)  

    
#for row in cur.execute('SELECT Territorial Level FROM personality_ranking'):
#    print(row)     
    
 #Close connection to SQLite database
 #REMEMBER TO COMMENT THIS OUT IF YOU WANT TO RUN MULTIPLE QUERIES; 
 #RUN AT THE END OF THE PROGRAM!!!!!!!!!!
conn.close()


