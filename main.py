# installing the library: PyPi - facebook-scraper
# pip install facebook-scraper
from facebook_scraper import get_posts

#import locale
#print(locale.getlocale())

#Hebrew languge
allDataHebrew = open("allDataHebrew.txt","w", encoding='utf-8')
posts = get_posts('kan.news', pages=10, options={"reactors": True})
for post in posts:
    print(post)
    allDataHebrew.writelines(post['text'])
allDataHebrew.close()

#Enlish languge
allDataEnglish = open("allDataEnglish.txt","w", encoding='utf-8')
for post in get_posts('beaverconfessions', pages=10):
    allDataEnglish.writelines(post['text'] + '\n')
allDataEnglish.close()

#Arabic languge
allDataArabic = open("allDataArabic.txt","w", encoding='utf-8')
for post in get_posts('ArabsForZehut', pages=10):
    allDataArabic.writelines(post['text'] + '\n')
allDataArabic.close()





