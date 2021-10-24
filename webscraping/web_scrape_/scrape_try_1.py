from bs4 import BeautifulSoup
import requests

html_text_1 = requests.get('https://www.causeiq.com/search/organizations/?view=list').text
html_text_2 = requests.get('https://www.causeiq.com/search/organizations/o_502388e448a5db61/?view=list').text

soup1 = BeautifulSoup(html_text_1, 'lxml')
soup2 = BeautifulSoup(html_text_2, 'lxml')

# print(soup.prettify)

tags_1 = soup1.find_all('div', class_='search-list-item')
tags_2 = soup2.find_all('div', class_='search-list-item')

# find nonprofit name
names = []

for tag in tags_1:
    # print(tag.prettify())
    name_line = tag.find('h2')
    name = tag.find('a').text
    # print(name)
    names.append(name)

for tag in tags_2:
    # print(tag.prettify())
    name_line = tag.find('h2')
    name = tag.find('a').text
    # print(name)
    names.append(name)

# find location

locations = []

for tag in tags_1:
    # print(tag.prettify())
    location_line = tag.find_all('div', class_='fields-item')
    location_line_2 = location_line[1]
    # print(type(location_line_2_name)) gets bs4.element.ResultSet
    # print(location_line_2)
    # for name in location_line_2:
    locations.append(location_line_2.text[9:])

for tag in tags_2:
    # print(tag.prettify())
    location_line = tag.find_all('div', class_='fields-item')
    location_line_2 = location_line[1]
    # print(type(location_line_2_name)) gets bs4.element.ResultSet
    # print(location_line_2)
    # for name in location_line_2:
    locations.append(location_line_2.text[9:])

for name in names:
    print(name)

print('')

for location in locations:
    print(location)

