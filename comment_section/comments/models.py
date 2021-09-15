from django.db import models

# Create your models here.
class Comment(models.Model):
    video_id = models.CharField(max_length=100)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comment = models.CharField(max_length=100)

class Reply(models.Model):
    reply = models.CharField(max_length=100)
    comment = models.ForeignKey('comments.Comment', null=True, blank=True, on_delete=models.CASCADE)