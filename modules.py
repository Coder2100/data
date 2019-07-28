from requests import get

from requests.exceptions import RequestException

from contextlib import closing

#from bs4 import BeautififulSoup
from bs4 import BeautifulSoup

#making a web request

def get_request(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def get_names():
    """
    Downloads the page where the list of mathematicians is found
    and returns a list of strings, one per mathematician
    """
    url = 'http://www.fabpedigree.com/james/mathmen.htm'
    response = get_request(url)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        names = set()
        for li in html.select('li'):
            for name in li.text.split('\n'):
                if len(name) > 0:
                    names.add(name.strip())
        return list(names)

    # Raise an exception if we failed to get any data from the url
    raise Exception('Error retrieving contents at {}'.format(url))


def get_hits_on_name(name):
    #accept name of mathematicians as string from wikimedia page, returns last 60 days as an int
    #url_root is template string that is used to build url

    url_root = 'URL_REMOVE_SEE_NOTICE_AT_START_OF_ARTICLE'
    response = get_request(url_root.format(name))

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        hit_link = [a for a in html.select('a')
        if a['href'].find('latest-60') > -1]

        if len(hit_link) > 0:
            #strip the comma
            link_text = hit_link[0].text.replace(',', '')
            try:
                #convert to integer
                return int(link_text)
            except:
                log_error("couldn't parse {} as an `int`".format(link_text))
                #log_error('No page views found for {}'.format(name))
    log_error('No page views found for {}'.format(name))
    return None















































