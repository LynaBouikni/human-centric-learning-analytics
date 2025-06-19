import sqlite3
import pandas as pd

# Connect to SQLite database
conn= sqlite3.connect("data/learning_analytics.db")

# Load CSVs
learners = pd.read_csv("data/raw/learners.csv")
clickstream = pd.read_csv("data/raw/clickstream.csv")
notes = pd.read_csv("data/raw/reflection_notes.csv")

# Write to SQL tables 

learners.to_sql("learners", conn, if_exists="replace", index=False)
clickstream.to_sql("clickstream", conn, if_exists="replace", index=False)
notes.to_sql("reflection_notes", conn, if_exists="replace", index=False)

conn.close()
print("Data loaded into SQLite at data/learning_analytics.db")