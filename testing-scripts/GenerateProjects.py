import csv
import random
import string

capitals = []
with open("states.csv") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        capitals.append(row.pop())

# randomize states for use in locations
random.shuffle(capitals)

# generate 35 projects
with open("projects.csv",'w',newline='') as projects:
    writer = csv.writer(projects)
    for i in range(35):
        projectID = ''.join(random.choices(string.ascii_letters + string.digits,k=6))
        location = capitals.pop()
        desc = "Test Project " + str(i+1)
        writer.writerow([projectID,location,desc])

# generate 6 judges with the same email for testing
with open("judges.csv", 'w', newline='') as judges:
    writer = csv.writer(judges)
    for i in range(6):
        name = "Test Judge " + str(i+1)
        desc = "Judge for Testing"
        writer.writerow([name,"viren.c.sawant@gmail.com",desc])