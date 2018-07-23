from django.db import models
from django.utils import timezone

# Create your models here.



class Clothing(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    data = models.DateTimeField(default=timezone.now)
    sale = models.BooleanField(default=False)
    african_traje = models.BooleanField(default=False)
    artwork = models.ImageField(upload_to='uploads/clothing/', default= " ",blank=False,max_length=45)
    #artwork = models.ImageField(upload_to='uploads/projects/', max_length=45, blank=True)

    Popularity = models.IntegerField(default=0)


#----------------------------------------------------------


# Similar to Color, Photo can be featured alongside Project.
# Multiple instances of Photo can also be created in the admin panel.
class PhotoClothing(models.Model):
    clothing_name = models.ForeignKey(Clothing,on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='uploads/clothing/', max_length=45)
    def projectTitle(self):
        return self.clothing_name.title
#end Photo

#----------------------------------------------------------