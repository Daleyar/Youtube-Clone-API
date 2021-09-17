from django.db import models

# Create your models here.
class Replies(models.Model):
    video_id = models.CharField(max_length=100)
    reply = models.CharField(max_length=100)
    comment = models.ForeignKey('comments.Comment',blank=True, null=True, on_delete=models.CASCADE)