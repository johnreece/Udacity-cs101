import sys


def get_next_target(html):
	start_link =  html.find('<a href=')
	if start_link == -1:
		return None,0
	start_quote = html.find('"',start_link)
	end_quote =  html.find('"',start_quote+1)
	url = html[start_quote+1:end_quote]
	return url,end_quote
	
def print_all_links(html):
	"""In print_all_links"""
	while True   :
		url,endpos = get_next_target(html)
		if url:
			print url
			html = html[endpos:]
		else:
			break
def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ""
	
if __name__ =='__main__':
#	page = '<html><body>This is a test<a href="http://www.example.com/">Example</a> Testing Testing Testing <a href="http://www.intel.com"/>Intel</a>Test</body></html>'
#	page = 'good'
#	print(get_page('http://www.intel.com/'))
	print_all_links(get_page('http://www.google.com/'))
	"""This is a test docstring"""
	
	