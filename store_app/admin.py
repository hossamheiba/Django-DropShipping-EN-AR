from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Categories , Brand , Color , Filter_Price , Products , Images , Tags , Contact_Us , Order , Order_Item 


class ImagesInline(admin.TabularInline):
    model = Images
    
class TagsInline(admin.TabularInline):
    model = Tags
    
class ProductsAdmin(admin.ModelAdmin):
    inlines = [ImagesInline , TagsInline]



class OrderInline(admin.TabularInline):
    model = Order_Item

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderInline]
    

admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Products , ProductsAdmin)
admin.site.register(Images)
admin.site.register(Tags)
admin.site.register(Contact_Us)

admin.site.register(Order, OrderAdmin)
admin.site.register(Order_Item)

