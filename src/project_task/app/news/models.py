from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    text = models.TextField()
    
    class Admin:
        pass
    
    def __unicode__(self):
        return self.title
    
class Comment(models.Model):
    news = models.ForeignKey(News)
    username = models.CharField(max_length=70)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    
    class Admin:
        pass
