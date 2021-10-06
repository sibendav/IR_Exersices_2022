# installing the library: PyPi - facebook-scraper
# pip install facebook-scraper
from facebook_scraper import get_posts

#import locale
#print(locale.getlocale())

for post in get_posts('biuconfessions2018'):
    print(post['text'][:50])


