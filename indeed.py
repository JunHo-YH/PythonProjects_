import requests
from bs4 import BeautifulSoup


limit = 50
url = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&as_phr=&as_any=&as_not=&as_ttl=&as_cmp=&jt=all&st=&salary=&radius=25&l=&fromage=any&limit={limit}&sort=&psf=advsrch&from=advancedsearch"


def extract_indeed_pages():
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    pagination = soup.select_one('ul.pagination-list')
    pages = pagination.select('ul > li > a > span')

    spans = list()
    for page in pages[:-1]:
        spans.append(int(page.get_text()))
    max_page = spans[-1]
    return max_page

def extract_indeed_job(last_page):
    jobs = list()
    for n in range(last_page):
        print(f"Scrapping Indeed: page {n+1}...")
        result = requests.get(f"{url}&start={n * limit}")
        #https://kr.indeed.com/jobs?q=python&limit=50&radius=25&start=50









