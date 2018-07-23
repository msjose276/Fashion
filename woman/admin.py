from django.contrib import admin
from .models import Clothing
from .models import PhotoClothing

# Register your models here.
#------------------------------- clothing ----------------------------------------------------
class PhotoClothingInline(admin.TabularInline):
    model = PhotoClothing

class ClothingAdmin(admin.ModelAdmin):
    ordering = ['title']
    list_display = ['title','price','data','Popularity','sale','african_traje']
    inlines = [PhotoClothingInline]

#-----------------------------------------------------------------------------------
admin.site.register(Clothing, ClothingAdmin)
