from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.causeiq.com/search/organizations/?view=list').text

soup = BeautifulSoup(html_text, 'lxml')
# print(soup.prettify)

tags = soup.find_all('div', class_='search-list-item')

# find nonprofit name
names = []

for tag in tags:
    # print(tag.prettify())
    name_line = tag.find('h2')
    name = tag.find('a').text
    # print(name)
    names.append(name)

# find location

locations = []

for tag in tags:
    # print(tag.prettify())
    location_line = tag.find_all('div', class_='fields-item')
    location_line_2 = location_line[1]
    # print(type(location_line_2_name)) gets bs4.element.ResultSet
    # print(location_line_2)
    # for name in location_line_2:
    locations.append(location_line_2.text[9:])

for name in names:
    print(name)

for location in locations:
    print(location)
