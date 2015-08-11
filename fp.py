import feedparser
import string
import xml.etree.cElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment
import xmlformatter

root = ET.Element("rss")   
#item = ET.SubElement(root,"item")

datatau = ET.SubElement(root,"datatau")
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
    item = ET.SubElement(datatau,"item")
    ET.SubElement(item,"title").text = str(title)
    ET.SubElement(item,"link").text = str(link)
    
dataisbeautiful = ET.SubElement(root,"dataisbeautiful")
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
    item = ET.SubElement(dataisbeautiful,"item")
    ET.SubElement(item,"title").text = str(title)
    ET.SubElement(item,"link").text = str(link)

hacking = ET.SubElement(root,"hacking")
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
    item = ET.SubElement(hacking,"item")
    ET.SubElement(item,"title").text = str(title)
    ET.SubElement(item,"link").text = str(link)

cybersecurity = ET.SubElement(root,"cybersecurity")  
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
    item = ET.SubElement(cybersecurity,"item")
    ET.SubElement(item,"title").text = str(title)
    ET.SubElement(item,"link").text = str(link)

ycombinator = ET.SubElement(root,"ycombinator")  
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
    item = ET.SubElement(ycombinator,"item")
    ET.SubElement(item,"title").text = str(title)
    ET.SubElement(item,"link").text = str(link)

file = open("daily_news.xml","w")
ET.ElementTree(root).write(file)


