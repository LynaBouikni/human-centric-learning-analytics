import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

# Initilizing faker for generating fake names
fake= Faker()
random.seed(42)

# Parameter for simulation

# Number of simulated learners
n_learners= 100 

# Number of days to simulate behavior 
n_days=60


# -----------------------------------------------------
# 1. Generating Learner Profiles (age, score, etc...)
# -----------------------------------------------------

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


# --------------------------------------------------------------
# 2. Generating Clickstream Events (pages visited, videos watched)
# --------------------------------------------------------------

# an empty list to store all the learner activity events(logs of what they did on the platform)
clickstream= []

# a list of all possible actions the learner might take (watching a video, starting/finishing a quiz, viewing a page)
event_types= ["video_start", "video_end", "quiz_submit", "page_view"] 

for learner in learners:
    for _ in range(random.randint(20, 80)):
        day_offset = random.randint(0, n_days - 1)
        timestamp = datetime.now() - timedelta(days=day_offset)
        clickstream.append({
            "learner_id": learner["learner_id"],
            "timestamp": timestamp.isoformat(),
            "event_type": random.choice(event_types)
        })


df_clickstream= pd.DataFrame(clickstream)

#save to csv 

df_clickstream.to_csv("data/raw/clickstream.csv", index= False)

# -------------------------------
# 3. Generate Reflection Notes
# -------------------------------
notes = []
prompts = [
    "Today I learned...",
    "I found it hard to...",
    "What stood out to me was...",
    "Next time, I will..."
]

for learner in learners: 
    for _ in range(random.randint(2, 5)):
        day_offset = random.randint(0, n_days - 1)
        timestamp = datetime.now() - timedelta(days=day_offset)
        notes.append({
            "learner_id": learner["learner_id"],
            "timestamp": timestamp.isoformat(),
            "note": random.choice(prompts) + " " + fake.sentence(nb_words=10)
        })

df_notes = pd.DataFrame(notes)

# Save to CSV
df_notes.to_csv("data/raw/reflection_notes.csv", index=False)

# Done
print("Synthetic data saved to data/raw/")