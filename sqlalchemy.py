# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 11:18:00 2018

@author: souravg
"""

"""
Read the following data set: https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
Task:
1. Create an sqlalchemy engine using a sample from the data set
2. Write two basic update queries
3. Write two delete queries
4. Write two filter queries
5. Write two function queries

"""

# Read the following data set:https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
import pandas as pd
import sqlite3
from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())
adultdata = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data", sep=' *, *', header=None, engine="python")
adultdata.columns = ('age','workclass','fnlwgt','education','education-num','marital-status','occupation','relationship','race','sex','capital-gain','capital-loss','hours-per-week','native-country','salary')
adultdata.head()
conn=sqlite3.connect('sqlalchemyadb.db')
adultdata.to_sql('sqlalchemytable', conn)

# 1.Create an sqlalchemy engine using a sample from the data set

from sqlalchemy import create_engine
import pandas as pd
# Create engine: engine
engine = create_engine('sqlite:///sqlalchemyadb.db')

#2.1 Write two basic update queries

# Open engine connection
con = engine.connect()
# Update query to set fnlwgt = 99999 where fnlwgt = 77143 and native-country is Germany
con.execute("UPDATE sqlalchemytable set fnlwgt = 99999 where fnlwgt = 77143 and `native-country` = 'Germany';")
rs = con.execute("SELECT * from sqlalchemytable where fnlwgt = 99999;")
# Save results of the query to DataFrame: df
dfadult = pd.DataFrame(rs.fetchall())
# Close connection
con.close()
# Print head of DataFrame df to display the desired result
dfadult.head()

#2.2 Write two basic update queries

# Open engine connection
con = engine.connect()
# Update query to set age = 999 where age is 30 and marital-status is Divorced and workclass is Local-gov and occupation is Adm-clerical and relationship is Not-in-family
con.execute("UPDATE sqlalchemytable set age = 999 where age = 31 and `marital-status` = 'Divorced' and workclass = 'Local-gov' and occupation = 'Adm-clerical' and relationship = 'Not-in-family';")
rs = con.execute("SELECT * from sqlalchemytable where age = 999;")
# Save results of the query to DataFrame: df
dfadult = pd.DataFrame(rs.fetchall())
# Close connection
con.close()
# Print head of DataFrame df to display the desired result
dfadult.head()

#3.1 Write two delete queries

# Open engine connection
con = engine.connect()
# Delete query to remove row for fnlwgt = 99999
con.execute("DELETE from sqlalchemytable where fnlwgt = 99999;")
rs = con.execute("SELECT * from sqlalchemytable where fnlwgt = 99999;")
# Save results of the query to DataFrame: df
dfadult = pd.DataFrame(rs.fetchall())
# Close connection
con.close()
# Print head of DataFrame df to display the empty result
dfadult.head()

#3.2 Write two delete queries

# Open engine connection
con = engine.connect()
# Delete query to remove row for age = 999
con.execute("DELETE from sqlalchemytable where age = 999;")
rs = con.execute("SELECT * from sqlalchemytable where age = 999;")
# Save results of the query to DataFrame: df
dfadult = pd.DataFrame(rs.fetchall())
# Close connection
con.close()
# Print head of DataFrame df to display the empty result
dfadult.head()

#4.1 Write two filter queries

# Open engine connection
con = engine.connect()
# Perform query to filter rows based on condition who are Bachelors and never married
rs = con.execute("SELECT * FROM sqlalchemytable where education = 'Bachelors' and `marital-status` = 'Never-married';")
# Save results of the query to DataFrame: df
dfadult = pd.DataFrame(rs.fetchall())
# Close connection
con.close()
# Print head of DataFrame df to display the desired result
dfadult.head()

#4.2 Write two filter queries

# Open engine connection
con = engine.connect()
# Perform query to filter rows based on condition who work in Private class and either age is more than 30 or native country is United States
rsother = con.execute("SELECT * FROM sqlalchemytable where workclass = 'Private' and (age > 30 or `native-country` = 'United-States');")
# Save results of the query to DataFrame: df
dfadult = pd.DataFrame(rsother.fetchall())
# Close connection
con.close()
# Print head of DataFrame df to display desired result
dfadult.head()

#5.1 Write two function queries

# Open engine connection
con = engine.connect()
# Perform query to Show the frequency table for occupation
rsother = con.execute("SELECT occupation,count(occupation) as Frequency FROM sqlalchemytable group by occupation;")
# Save results of the query to DataFrame: df
dfadult = pd.DataFrame(rsother.fetchall())
# Close connection
con.close()
# Print head of DataFrame df
dfadult.head()

#5.2 Write two function queries

# Open engine connection
con = engine.connect()
# Perform query to Calculate age distribution by country
rsother = con.execute("SELECT `native-country`, avg(age), min(age), max(age) from sqlalchemytable group by `native-country`;")
# Save results of the query to DataFrame: df
dfadult = pd.DataFrame(rsother.fetchall())
# Close connection
con.close()
# Print head of DataFrame df
dfadult.head()