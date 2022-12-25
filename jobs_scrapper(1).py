import requests
from bs4 import BeautifulSoup
def parse(page):
    soup = BeautifulSoup(page, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    
headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding":"gzip, deflate, br",
    "accept-language": "youe_accept_language",
    "cache-control": "max-age=0",
    "user-agent": "your_ua"
}
with open('saved_page.html', 'r') as f:
    page = f.read()

def parse(page):
    soup = BeautifulSoup(page, 'lxml')
    jobs = soup.find_all('li', class_ = 'clearfix job-bx wht-shd-bx')
    jobs_list = []
    for job in jobs:
        company_name = job.h3.text.split()
        company_name_fixed = ''
        for i in company_name:
            company_name_fixed += i
            company_name_fixed += ' '
        inner_inf = job.find('ul', class_= 'top-jd-dtl clearfix')
        experience = inner_inf.find_all('li')[0].text.split('travel')[1]
        try:
            location = inner_inf.find_all('li')[1].span.text
        except:
            location = inner_inf.find_all('li')[2].span.text

        if not location:
            location = 'no location'
        inner_inf = job.find('ul', class_= 'list-job-dtl clearfix')
        job_desc = str(inner_inf.find_all('li')[0]).split('</label>')[1].split(' <a')[0][2:]
        skills = inner_inf.find_all('li')[1].text.replace(' ', '').replace('\n', '').replace(':', ': ').replace(',', ', ')
        new_skills = ''
        for i in skills:
            if skills !='\n':
                new_skills += i
        inf_str =  f'''
        Company name: {company_name_fixed}
        Experience: {experience}
        Location: {location}
        Job description: {job_desc}
        {new_skills}
        '''
        print(new_skills)
        jobs_list.append(inf_str)
    return jobs_list
jobs_list = parse(page=page)
for i in range(2,5):
    try:
        url = f'https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords=Python&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&luceneResultSize=25&postWeek=60&txtKeywords=Python&cboWorkExp1=0&pDate=I&sequence={i}&startPage={i}'
        page = requests.get(url=url, headers=headers)
        print(page.request.url, page)
        jobs_list.append(parse(page=page.text))
    except Exception as Err:
        print(Err)
        break
with open('test.txt', 'w') as f:
    for i in jobs_list:
        for j in i:
            f.write(j)
