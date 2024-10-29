# from bs4 import BeautifulSoup
# import ipdb

# # projects: kickstarter.select("li.project.grid_4")[0]
# # title: project.select("h2.bbcard_name strong a")[0].text
# # image link: project.select("div.project-thumbnail a img")[0]['src']
# # description: project.select("p.bbcard_blurb")[0].text
# # location: project.select("ul.project-meta span.location-name")[0].text
# # percent_funded: project.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")

# def create_project_dict():
#     html = ''
#     with open('./fixtures/kickstarter.html') as file:
#         html = file.read()
#     kickstarter = BeautifulSoup(html, 'html.parser')
#     projects = {}
#     # Iterate through the projects
#     for project in kickstarter.select("li.project.grid_4"):
#         title = project.select("h2.bbcard_name strong a")[0].text
#         projects[title] = {
#         'image_link': project.select("div.project-thumbnail a img")[0]["src"],
#         'description': project.select("p.bbcard_blurb")[0].text,
#         'location': project.select("ul.project-meta span.location-name")[0].text,
#         'percent_funded': project.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")
#         }
#     # return the projects dictionary

#     return projects

# projects = create_project_dict()
# print(projects)

# projects: kickstarter.select("li.project.grid_4")[0]
# projects: kickstarter.select("li.project.grid_4")[0]
# title: project.select("h2.bbcard_name strong a")[0].text
# image link: project.select("div.project-thumbnail a img")[0]['src']
# description: project.select("p.bbcard_blurb")[0].text
# location: project.select("ul.project-meta span.location-name")[0].text
# percent_funded: project.select("ul.project-stats li.first.funded strong")[0].text.replace("%","")
import json
from bs4 import BeautifulSoup
import ipdb

def save_projects_to_json():
    # Load the HTML content
    html = ''
    with open('./fixtures/kickstarter.html') as file:
        html = file.read()

    # Parse with BeautifulSoup
    kickstarter = BeautifulSoup(html, 'html.parser')
    
    # Get the projects
    projects = []
    for project in kickstarter.select("li.project.grid_4"):
        project_data = {
            "title": project.select("h2.bbcard_name strong a")[0].text,
            "image_link": project.select("div.project-thumbnail a img")[0]['src'],
            "description": project.select("p.bbcard_blurb")[0].text,
            "location": project.select("ul.project-meta span.location-name")[0].text,
            "percent_funded": project.select("ul.project-stats li.first.funded strong")[0].text.replace("%", "")
        }
        projects.append(project_data)
    
    # Set the breakpoint here
    ipdb.set_trace()

    # Save to a JSON file
    with open('projects.json', 'w') as f:
        json.dump(projects, f, indent=4)

# Run the function
save_projects_to_json()