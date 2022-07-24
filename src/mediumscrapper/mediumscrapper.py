import requests
from bs4 import BeautifulSoup


def scrape_by_tag(tag, sort_by='latest'):
    """Get the titles and article links of the medium articles."""
    url = 'https://medium.com/tag/' + tag + '/' + sort_by
    data = requests.get(url).text
    soup = BeautifulSoup(data, 'lxml')

    posts = []

    post_content = soup.findAll("article")
    for i in post_content:
        items = dict()
        title = i.find("h2")
        link = i.find("a", {'aria-label': 'Post Preview Title'})
        items['title'] = title.text
        items['link'] = "https://medium.com" + link['href'].split("?")[0]

        posts.append(items)

    return posts
