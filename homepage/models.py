from django.db import models

# Create your models here.


class Topic(models.Model):
    category = models.CharField(max_length=50, default="")
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=50)
    Image = models.ImageField(upload_to='uploads/homepage_topics/', max_length=45, blank=True)
