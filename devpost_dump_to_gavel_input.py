 # Aggregates and retains the necessary parts of the devpost csv dump to be
 # able to input it into gavel


import csv

projects = []

# Helper function for projects submitted under multiple categories
def find_project(name):
    for project in projects:
        if project['name'] == name:
            return project
    return None

def transform(devpost_dump):
    for entry in devpost_dump[1:]:
        project = find_project(entry[1])
        if project is not None:
            project['category'] = project['category'] + " | " + entry[0]
        else:
            projects.append({
                'name': entry[1],
                'category': entry[0],
            })

    gavel_input = []
    for project in projects:
        gavel_input.append([project["name"], project["category"], " ", " "])
    return gavel_input
