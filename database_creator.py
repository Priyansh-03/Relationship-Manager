import pandas as pd
from faker import Faker
fake = Faker()

# Define the number of entries
num_entries_with_rel = 100
num_entries_without_rel = 100

# Define relationship types
relationships = ["friend", "family", "coworker", "ex-partner"]

# Generate entries with relationships
data_with_rel = [{
    "Name": fake.name(),
    "Email": fake.email(),
    "Relationship Status": fake.random.choice(relationships)
} for _ in range(num_entries_with_rel)]

# Generate entries without relationships
data_without_rel = [{
    "Name": fake.name(),
    "Email": fake.email(),
    "Relationship Status": ""  # Empty relationship status
} for _ in range(num_entries_without_rel)]

# Combine the data
full_data = data_with_rel + data_without_rel

# Convert to DataFrame
df = pd.DataFrame(full_data)

# Save to CSV
df.to_csv("contact_data.csv", index=False)
