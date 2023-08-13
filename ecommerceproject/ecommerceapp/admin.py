from django.contrib import admin
from . models import Category,Product
# Register your models here.

class Category_Admin(admin.ModelAdmin):
    list_display=['name','slug','description']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category,Category_Admin)


class Product_Admin(admin.ModelAdmin):
    list_display = ['name','price','stock','available','created','updated']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20


admin.site.register(Product,Product_Admin)