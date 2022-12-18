from bs4 import BeautifulSoup
import requests
import json
points = []
creator = []
time = []
text = []
comments = []
link = []

headers = {
    'Accept': 'Your_accept',
    'User-Agent': 'Your u_a'
}


def parsing(page):
    r = requests.get(f'https://news.ycombinator.com/?p={page}', headers=headers)
    soup = BeautifulSoup(r.text, 'lxml')
    for i in range(len(soup.find_all('span', class_='score'))):
        if page <=3:
            points.append(soup.find_all('span', class_='score')[i].next_element[0:soup.find_all('span', class_='score')[i].next_element.find('p')].strip())
            creator.append(soup.find_all('a', class_='hnuser')[i].text.strip())
            time.append(soup.find_all('span', class_='age')[i]['title'].replace('T', ' ').strip())
            text.append(soup.find_all('span', class_='titleline')[i].text[0:soup.find_all('span', class_='titleline')[i].text.find('(')].strip())
            link.append(str(soup.find_all('span', class_='titleline')[i].next_element)[9:str(soup.find_all('span', class_='titleline')[i].next_element).rfind('"')])
            g = soup.find_all("td", class_="subtext")
            s = g[i].find_all("a")[-1].text
            if s == 'hide' or s == 'discuss':
                comments.append('0')
            else:
                comments.append(s[0:s.find('c')].strip())

        elif page == 4:
            if i <=10:
                points.append(soup.find_all('span', class_='score')[i].next_element[0:soup.find_all('span', class_='score')[i].next_element.find('p')].strip())
                creator.append(soup.find_all('a', class_='hnuser')[i].text.strip())
                time.append(soup.find_all('span', class_='age')[i]['title'].replace('T', ' ').strip())
                text.append(soup.find_all('span', class_='titleline')[i].text[0:soup.find_all('span', class_='titleline')[i].text.find('(')].strip())
                link.append(str(soup.find_all('span', class_='titleline')[i].next_element)[9:str(soup.find_all('span', class_='titleline')[i].next_element).rfind('"')])
                g = soup.find_all("td", class_="subtext")
                s = g[i].find_all("a")[-1].text
                if s == 'hide' or s == 'discuss':
                    comments.append('0')
                else:
                    comments.append(s[0:s.find('c')].strip())
    return creator, points, time, text, comments, link

for i in range(1, 5):
    parsing(i)

with open(r'your_path', 'w') as out:
    for i in range(100):
        dict1 = {
            'id': i+1,
            'creator': creator[i],
            'points': points[i],
            'time': time[i],
            'text': text[i],
            'comments': comments[i],
            'link': link[i]

        }
        json.dump(dict1, out, indent = 10)
