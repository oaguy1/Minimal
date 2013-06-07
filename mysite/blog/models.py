from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length = 200)
    email = models.CharField(max_length = 200)
    def __unicode__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 200)
    slug = models.CharField(max_length = 200)
    author = models.ForeignKey(Author)
    body = models.TextField()
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
        return self.title
