from django.conf import settings
from django.db import models


class Ad(models.Model):
    title = models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    description = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="ad_image/", null=True, blank=False)


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    ad = models.ForeignKey("ads.Ad", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now=True)
