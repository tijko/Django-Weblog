from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class Post(models.Model):
  title = models.CharField(max_length = 30)
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return self.title

class Comment(models.Model):
  author = models.CharField(max_length = 20)
  body = models.TextField()
  post = models.ForeignKey(Post)
  created = models.DateTimeField(auto_now_add=True)

  def __unicode__(self): 
    return unicode("%s: %s" % (self.post, self.body[:60]))

class Index(models.Model):
  entry = models.ForeignKey(Post)  
  index_created = models.DateTimeField(auto_now_add=True)

  def __unicode__(self):
    return unicode("%s" % (self.entry))

class IndexAdmin(admin.ModelAdmin):
  search_fields = ['entry']
  display_fields = ['entry', 'index_created']   

class PostAdmin(admin.ModelAdmin):
  search_fields = ["title"]
  display_fields = ["title", "created"]

class CommentAdmin(admin.ModelAdmin):
  display_fields = ["post", "author", "created"]


