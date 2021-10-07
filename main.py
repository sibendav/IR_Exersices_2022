# installing the library: PyPi - facebook-scraper
# pip install facebook-scraper
from facebook_scraper import get_posts

#import locale
#print(locale.getlocale())

#Hebrew languge
allDataHebrew = ""
for post in get_posts('algoritmim', pages=100):
    allDataHebrew += (post['text'] + '\n')
print(allDataHebrew)

#Enlish languge
allDataEnglish = ""
for post in get_posts('beaverconfessions', pages=100):
    allDataEnglish += (post['text'] + '\n')
print(allDataEnglish)

#Arabic languge
allDataArabic = ""
for post in get_posts('ArabsForZehut', pages=100):
    allDataArabic += (post['text'] + '\n')
print(allDataArabic)





