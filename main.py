import requests
from bs4 import BeautifulSoup

print("Enter a skill that you are not familiar with: ")
unfamiliar_skill = input("> ")
print(f"Filtering out {unfamiliar_skill}")


def find_jobs():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from'
                             '=submit&txtKeywords=python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for index, job in enumerate(jobs):
        published = job.find('span', class_='sim-posted').span.text

        if ('few' or 'today') in published:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']

            if unfamiliar_skill not in skills:
                with open(f'Job-posts/{index}.txt', 'w') as file:
                    file.write(f"COMPANY NAME: {company_name.strip()} \n")
                    file.write(f"REQ SKILLS: {skills.strip()} \n")
                    file.write(f"MORE INFO: {more_info} \n")
                    file.write(f"Posted : {published}")
                print(f"File saved: {index}.txt")


if __name__ == '__main__':
    find_jobs()
    # time_wait = 10
    # print(f"Waiting {time_wait} min...")
    # time.sleep(600)
