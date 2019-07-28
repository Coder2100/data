from modules import get_request

from bs4 import BeautifulSoup
raw_html = get_request('https://realpython.com/blog/')
len(raw_html)
print(len(raw_html))

content_html = open('content.html').read()
html = BeautifulSoup(content_html, 'html.parser')
for p in html.select('p'):
	if p['id'] == 'zux':
		print(p.text)