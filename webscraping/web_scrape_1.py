from bs4 import BeautifulSoup
import requests

# read the HTML
URL = "https://www.causeiq.com/organizations/securities-investor-protection-corporation,520910763/"
page = requests.get(URL)

# store the HTML
soup = BeautifulSoup(page.content, "lxml")

# print raw HTML
# print(soup.prettify())

# scrape and print text from HTML classes
course_tags = soup.find_all('div', class_='org-title-bar')

for course_tag in course_tags:
    course_name = course_tag.h1.text
    course_id = course_tag.h1.text.split()[-1]
    print(course_name)
    print(course_id)

# present info in a sentence
print(f'{course_name} contains the ID {course_id}')