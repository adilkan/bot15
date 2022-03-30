import requests
from bs4 import BeautifulSoup

URL = "https://rt.potnhub.com/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('li', class_="pcVideoListItem js-pop videoblock videoBox")
    anime = []

    for item in items:
        anime.append(
            {
                "title": URL + item.find('div', class_="thumbnail-info-wrapper clearfix").get_text(),
                'image': URL + item.find('div', class_='phimage').find('img').get('src')
            }
        )
    return anime


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        anime = []
        for page in range(1, 2):
            html = get_html(f"https://rt.pornhub.com/video?page={page}")
            anime.extend(get_data(html.text))
        return anime
    else:
        raise Exception("Error in parser function")
