 # This script aggregates and retains the necessary parts of the devpost csv
 # dump to be able to input it into gavel
 #
 # Run with the file name of the devpost csv passed in as an arg
 # (should be in same directory)

import csv
import sys

projects = []

# Helper function for projects submitted under multiple categories
def find_project(name):
    for project in projects:
        if project['name'] == name:
            return project
    return None

def main():
    if (len(sys.argv) < 2):
        print("File name of devpost csv must be passed in!")
        sys.exit()

    file_name = sys.argv[1]
    with open(file_name) as devpost_file:
        reader = csv.reader(devpost_file)
        next(reader)
        for line in reader:
            project = find_project(line[1])
            if project is not None:
                project['category'] = project['category'] + " | " + line[0]
            else:
                projects.append({
                    'name': line[1],
                    'category': line[0],
                })

    with open('gavel-input.csv', 'w') as f:
        writer = csv.writer(f)
        for project in projects:
            writer.writerow([project["name"], project["category"], " ", " "])

if __name__ == "__main__":
    main();
