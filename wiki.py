import pywikibot
site = pywikibot.Site(‘en’,’wikipedia’)
category = pywikibot.Category(site, 'Category:Python (programming language)')
articles = category.articles()
for page in list(articles)[:10]:
if page.exists():
text = page.text
new_text = text.replace('Python', 'Python programming language')
if text != new_text:
page.text = new_text
page.save('Bot edit: clarified "Python" to "Python programming language"')
