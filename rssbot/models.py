from django.db import models

# Create your models here.

class Channel(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Feed(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(blank=True)
    siteurl = models.URLField(blank=True)
    description = models.TextField(blank=False)
    add_date = models.DateTimeField('date added')
    refreshed_date = models.DateTimeField('date refreshed', blank=True)
    refreshinterval = models.IntegerField(null=True, blank=True, default=0)
    etag = models.CharField(max_length=200, blank=True)
    icon = models.URLField(blank=True)
    enabled = models.BooleanField(default=True)
    channel = models.ForeignKey(Channel, blank=True)
    def __unicode__(self):
        return self.title
    
class Context(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name
    
class Item(models.Model):
    feed = models.ForeignKey(Feed)
    md5sum = models.CharField(max_length=255)
    guid = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    date = models.DateTimeField('date added')
    content = models.TextField(blank=False)
    content_type = models.CharField(max_length=255, null=True, blank=True)
    author = models.CharField(max_length=255, blank=True)
    unread = models.BooleanField(default=True)
    context = models.ForeignKey(Context)
    
    def __unicode__(self):
        return self.title

