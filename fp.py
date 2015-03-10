import feedparser

d = feedparser.parse('http://www.datatau.com/rss')

print "datatau"
for f in d['entries']:
  print f['title'] + " - " + f['link'] 

d = feedparser.parse('https://www.reddit.com/r/dataisbeautiful/.rss')

print "\n/r/dataisbeautiful"
for f in d['entries']:
  print f['title'] + " - " + f['link']

d = feedparser.parse('https://www.reddit.com/r/arduino/.rss')

print "\n/r/arduino"
for f in d['entries']:
  print f['title'] + " - " + f['link']

d = feedparser.parse('https://news.ycombinator.com/rss')

print "\nhacker news"
for f in d['entries']:
  print f['title'] + " - " + f['link']




