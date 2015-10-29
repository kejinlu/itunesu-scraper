from urllib.request import urlopen
from urllib.parse import urlparse

from bs4 import BeautifulSoup

__author__ = 'Luke'

class Course:
    def __init__(self, url):
        html = urlopen(url)
        bs_html = BeautifulSoup(html.read(), "html.parser")
        self.title = bs_html.select_one("#title > div.left > h1").get_text(strip=True)
        self.publisher = bs_html.select_one("#title > div.left > h2").get_text(strip=True)
        self.category = bs_html.select_one("#left-stack > div.lockup.product.course.itunes-u > ul > li.genre > a > span").get_text(strip=True)
        self.rating = bs_html.select_one("#left-stack > div.extra-list.customer-ratings > div")["aria-label"]

        bs_video_trs = bs_html.find_all("tr",attrs={"class":"podcast-episode video"})
        if bs_video_trs is not None:
            self.video_urls = [bs_video_tr["video-preview-url"] for bs_video_tr in bs_video_trs]


c = Course("https://itunes.apple.com/cn/course/1.-logistics-ios-8-overview/id961180099?i=333886882&mt=2")
print(c.video_urls)