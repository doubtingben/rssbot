import sys, os
import datetime,calendar
import feedparser
import md5

#sys.path.append('/home/bwilson/python')
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from mysite.rssbot.models import Channel, Feed, Item

def update_feeds():
    feeds = Feed.objects.filter(enabled=True)
    for f in feeds:
        try:
            stream = feedparser.parse(f.url)
            for e in stream['entries']:
                if Item.objects.filter(md5sum=md5.new(e.link).hexdigest()).count() > 0:
                    print 'Skipping duplicate item'
                else:
                    e_date = e.updated_parsed
                    if not e_date:
                        e_date = datetime.datetime.utcnow()
                    i = Item(feed = f,
                             md5sum = md5sum=md5.new(e.link).hexdigest(),
                             guid = e.id,
                             title = e.title.encode('ascii', 'xmlcharrefreplace'),
                             link = e.link,
                             date = e_date,
                             content = e.summary.encode('ascii', 'xmlcharrefreplace'),
                             author = e.author,
                            )
                    i.save()
        except Exception, e:
            print e

