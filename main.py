from urllib.request import urlopen
from urllib.parse import unquote
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import unquote
import concurrent.futures
import urllib.request
from bs4 import BeautifulSoup
from tqdm import tqdm
from urllib.request import urlopen

'''
#IO-bound
url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'

for i in range(100):
    s = urlopen(url)
    print(unquote(s.url))



url = 'https://ru.wikipedia.org/wiki/%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%A1%D0%BB%D1%83%D1%87%D0%B0%D0%B9%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0'

res = open('res.txt', 'w', encoding='utf8')

for i in tqdm(range(100)):
    html = urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')

    for l in links:
        href = l.get('href')
        if href and href.startswith('http') and 'wiki' not in href:
            print(href, file=res)

# синхронно в 1 поток
links = open('res.txt', encoding='utf8').read().split('\n')

for url in links:
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        print(code)
        resp.close()
    except Exception as e:
        print(url, e)

# асинхронно
def load_url(url, timeout):
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=timeout)
        code = resp.code
        resp.close()
        return code
    except Exception as e:
        return [url, e]


links = open('res.txt', encoding='utf8').read().split('\n')

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    future_to_url = {executor.submit(load_url, url, 5) for url in links}
    for future in concurrent.futures.as_completed(future_to_url):
        print(future.result())
'''

from hashlib import md5
from random import choice


def generate():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            print(s, h)


def find_coins(needed: int):
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        tasks = [executor.submit(generate) for i in range(needed)]
        for task in concurrent.futures.as_completed(tasks):
            print(task.result())


if __name__ == '__main__':
    find_coins(5)
