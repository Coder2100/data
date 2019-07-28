from bs4 import BeautifulSoup

from modules import get_request

raw_html = get_request('http://www.fabpedigree.com/james/mathmen.htm')
html = BeautifulSoup(raw_html, 'html.parser')

#loop using enumarate method
for i, li in enumerate(html.select('li')):
	print(i, li.text)

	#loop using zip method if key value pairs

#for i, li in zip(html.select('li')):
#	print(i, li.text)