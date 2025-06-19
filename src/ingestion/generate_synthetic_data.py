import pandas as pd
import random
from faker import Faker
from datatime import datatime, timedelta

# Initilizing faker for generating fake names
fake= Faker()
random.seed(42)

# Parameter for simulation

# Number of simulated learners
n_learners= 100 

# Number of days to simulate behavior 
n_days=60


# 1. Generating Learner Profiles (age, score, etc...)

learners= []
for i in range(n_learners):
    learners.append({"learner_id":i,
                     "name": fake.first_name(),
                     "age": random.randint(18,60),
                     "gender": random.randint(18,60),
                     "average_score": round(random.uniform(50,100),2)
    })
    
df_learners = pd.DataFrame(learners)

# Save to CSV 
df_learners.to_csv("data/raw/learners.csv", index=False)


# 2. Generating Clickstream Events (pages visited, videos watched)

Clickstream= []
event_types= ["video_start", "video_end", "quiz_submit", "page_view"] 

for learner in learners: 
    