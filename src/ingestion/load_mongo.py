import pandas as pd
from pymongo import MongoClient

# MongoDB Atlas connection string
MONGO_URI = "mongodb+srv://lynabouikni:Arbre57cat99!@human-learning-cluster.s2zarvn.mongodb.net/learning_analytics?retryWrites=true&w=majority"

# Connect to Atlas
client= MongoClient(MONGO_URI)
db= client["learning_analytics"]

# Load CSVs and convert to dictionaries
learners = pd.read_csv("data/raw/learners.csv").to_dict(orient="records")
clickstream = pd.read_csv("data/raw/clickstream.csv").to_dict(orient="records")
notes = pd.read_csv("data/raw/reflection_notes.csv").to_dict(orient="records")

# Insert into MongoDB collections
db.learners.insert_many(learners)
db.clickstream.insert_many(clickstream)
db.reflection_notes.insert_many(notes)

print("Data loaded into MongoDB Atlas!") 