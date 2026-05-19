import pandas as pd
from faker import Faker
import random

fake = Faker()

courses = ["Python", "Java", "Data Science", "AI", "SQL"]
cities = ["Bangalore", "Hyderabad", "Chennai", "Mumbai", "Delhi"]

students = [
    {
        "student_id": i,
        "Name": fake.name,
        "Age": random.randint(18,23),
        "Address": fake.address,
        "Email":fake.email,
        "Course":random.choice(courses),
        "City":random.choice(cities),
        "Marks":random.randint(35,100),
        "Admission_date":fake.date_between(start_date="-2y",end_date="today")
    }
    for i in range(1,100)
]

df = pd.DataFrame(students)

df.to_csv("Students_100records.csv",index=False)
df = pd.read_csv("Students_100records.csv")
print(df)
print("CSV Created successfully!!!")

