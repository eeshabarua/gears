from bs4 import BeautifulSoup
import requests

# this demo retrieves all jobs posted few days ago from timesjobs.com


html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text

# prints raw HTML file
# print(html_text)

# create beautifulsoup instance and make it provide HTML
soup = BeautifulSoup(html_text, 'lxml')
# print(soup.prettify)

# in browser -- catch an element and inspect all of them
# jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
# for job in jobs:
#     print(job)

# for the first single instance of the element
# job = soup.find('li', class_='clearfix job-bx wht-shd-bx')
# print(job)

# you want to search an attribute specifically within our element
# company_name = job.find('h3', class_='joblist-comp-name').text
# print(company_name)

# formatting - delete whitespace
# company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
# print(company_name)

# search narrower attribute within the class we scraped - skill
# skill = job.find('span', class_ ='srp-skills').text.replace(' ', '')
# print(skill)

# pretty print statement
# print(f'''
#     Company Name: {company_name}
#     Skill Set: {skill}
# ''')

# encapsulated element - use .span technique
# job_post_date = job.find('span', class_='sim-posted').span.text
# print(job_post_date)

# now with multiple job elements 
jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

# pull code under this for loop so we can do the same for all jobs on the website
# for job in jobs:
#     company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
#     skill = job.find('span', class_ ='srp-skills').text.replace(' ', '')
#     job_post_date = job.find('span', class_='sim-posted').span.text
#     print(job_post_date)
    
#     # print
#     print(f'''
#     Company Name: {company_name}
#     Skill Set: {skill}
#     ''')

#     print('')
#     # WOW!!!

# MISSION - filter job posts that are not published a few days ago

for job in jobs:
    job_post_date = job.find('span', class_='sim-posted').span.text
    if 'few' in job_post_date:
        company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
        skill = job.find('span', class_ ='srp-skills').text.replace(' ', '')
        
        # print(job_post_date)
        
        print
        print(f'''
        Company Name: {company_name}
        Skill Set: {skill}
        ''')

        # print('')
        # DOUBLE WOW!!!

        # write to the file
        # first arg is an index, second is a permission
        # with open(f'posts/{index}.txt', 'w') as f:
        #     # pretty print
        #     f.write(f"Company Name: {company_name}")
        #     f.write(f"Required Skills: {skill}")
        # # print confirmation message
        # print(f'Filed saved: {index}')

