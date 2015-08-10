import feedparser
import string
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment
import xmlformatter

root = ET.Element("rss")   
item = ET.SubElement(root,"item")

datatau = ET.SubElement(item,"datatau")
d = feedparser.parse('http://www.datatau.com/rss')

for f in d['entries']:
    try: 
        title = filter(lambda x: x in string.printable, str(f['title']).encode('utf-8').replace(",",""))
    except:
        title = ""
    try: 
        link = filter(lambda x: x in string.printable, str(f['link']).encode('utf-8').replace(",",""))
    except:
        link = ""
    ET.SubElement(datatau,"title").text = str(title)
    ET.SubElement(datatau,"link").text = str(link)
    
dataisbeautiful = ET.SubElement(item,"dataisbeautiful")
d = feedparser.parse('https://www.reddit.com/r/dataisbeautiful/.rss')

for f in d['entries']:
    try: 
        title = filter(lambda x: x in string.printable, str(f['title']).encode('utf-8').replace(",",""))
    except:
        title = ""
    try: 
        link = filter(lambda x: x in string.printable, str(f['link']).encode('utf-8').replace(",",""))
    except:
        link = ""
    ET.SubElement(dataisbeautiful,"title").text = str(title)
    ET.SubElement(dataisbeautiful,"link").text = str(link)

hacking = ET.SubElement(item,"hacking")
d = feedparser.parse('https://www.reddit.com/r/hacking/.rss')

for f in d['entries']:
    try: 
        title = filter(lambda x: x in string.printable, str(f['title']).encode('utf-8').replace(",",""))
    except:
        title = ""
    try: 
        link = filter(lambda x: x in string.printable, str(f['link']).encode('utf-8').replace(",",""))
    except:
        link = ""
    ET.SubElement(hacking,"title").text = str(title)
    ET.SubElement(hacking,"link").text = str(link)

cybersecurity = ET.SubElement(item,"cybersecurity")  
d = feedparser.parse('https://www.reddit.com/r/cybersecurity/.rss')

for f in d['entries']:
    try: 
        title = filter(lambda x: x in string.printable, str(f['title']).encode('utf-8').replace(",",""))
    except:
        title = ""
    try: 
        link = filter(lambda x: x in string.printable, str(f['link']).encode('utf-8').replace(",",""))
    except:
        link = ""
    ET.SubElement(cybersecurity,"title").text = str(title)
    ET.SubElement(cybersecurity,"link").text = str(link)

ycombinator = ET.SubElement(item,"ycombinator")  
d = feedparser.parse('https://news.ycombinator.com/rss')

for f in d['entries']:
    try: 
        title = filter(lambda x: x in string.printable, str(f['title']).encode('utf-8').replace(",",""))
    except:
        title = ""
    try: 
        link = filter(lambda x: x in string.printable, str(f['link']).encode('utf-8').replace(",",""))
    except:
        link = ""
    ET.SubElement(ycombinator,"title").text = str(title)
    ET.SubElement(ycombinator,"link").text = str(link)

file = open("daily_news.xml","w")
ET.ElementTree(root).write(file)


