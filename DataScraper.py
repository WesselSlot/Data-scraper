from lxml import html
import requests

page = requests.get('https://www.efteling.com/nl/blog')
tree = html.fromstring(page.content)

blogTitles = tree.xpath('//*[contains(@class,"text-secondary")]/text()')
cleanTitles = []

for blogTitle in blogTitles:
    cleanTitles.insert(0, blogTitle.strip())


print('Blog titles: ', blogTitles)
