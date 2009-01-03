# Some of this stolen from http://www.bitbucket.org/IanLewis/dlife/src/a64fcf2090a1/dlife/lifestream/feeds.py
import sys, os
import datetime,calendar
import feedparser
import md5

#sys.path.append('/home/bwilson/python')
#os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from mysite.rssbot.models import Channel, Feed, Item, Context

def update_feeds():
    context = Context.objects.get(pk=1)
    feeds = Feed.objects.filter(enabled=True)
    for f in feeds:
        try:
            print "Starting %s..." % (f.title)
            stream = feedparser.parse(f.url)
            for e in stream['entries']:
                try:
                    print "Getting entry id %s" % (e.id)
                    if Item.objects.filter(md5sum=md5.new(e.link).hexdigest()).count() > 0:
                        print 'Skipping duplicate item'
                    else:
                        e_date = e.updated_parsed
                        if not e_date:
                            e_date = datetime.datetime.utcnow()
                        i = Item(feed = f,
                                 md5sum = md5.new(e.link).hexdigest(),
                                 guid = e.id,
                                 title = e.title.encode('ascii', 'xmlcharrefreplace'),
                                 link = e.link,
                                 date = datetime.datetime.utcfromtimestamp(calendar.timegm(e_date)),
                                 content = e.summary.encode('ascii', 'xmlcharrefreplace'),
                                 context = context,
                                )
                        i.save()
                        print "%s - %s - Added!" % (f.title, i.title)
                except Exception, e:
                    print e
        except Exception, e:
            print e

