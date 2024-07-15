from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _



class Categories (models.Model):
    name=models.CharField(_("name"),max_length=50)
    
    def __str__(self):
        return self.name  
    
    class Meta:
        verbose_name = (_("Categories"))
        verbose_name_plural = (_("Categories"))
        

class Brand (models.Model):
    name=models.CharField(_("name"),max_length=50)
    
    def __str__(self):
        return self.name  

class Color (models.Model):
    name=models.CharField(_("name"),max_length=50)
    code=models.CharField(_("color"),max_length=50)
    
    def __str__(self):
        return self.name  
    
class Filter_Price (models.Model):
    FILTER_PRICE= (
        ('1000 TO 2000','1000 TO 2000'),
        ('2000 TO 3000','2000 TO 3000'),
        ('3000 TO 4000','3000 TO 4000'),
        ('4000 TO 5000','4000 TO 5000'),
        ('5000 TO 6000','5000 TO 6000'),    
    )
    price=models.CharField(_("price"), choices=FILTER_PRICE ,max_length=50)
    
    def __str__(self):
        return self.price

class Products(models.Model):
    CONDITION= (('New','New'),('Old','Old'),('Header' , 'Header'))
    STOCK= (('In Stock','In Stock'),('Out Of Stock','Out Of Stock'),)
    STATUS= (('Publish','Publish'),('Draft','Draft'),)
    
    unique_id=models.CharField(unique=True ,null=True,blank=True, max_length=200 , )
    img=models.ImageField(upload_to='products/')
    name=models.CharField( max_length=50)
    price=models.IntegerField()
    price_afetr_sale=models.IntegerField(default=0)
    condition=models.CharField(choices=CONDITION , max_length=50)
    information=RichTextField( null=True )
    description=RichTextField( null=True )
    stock=models.CharField(choices=STOCK , max_length=200)
    status=models.CharField( choices=STATUS , max_length=200)
    created_date=models.DateTimeField(default=timezone.now)
    
    categories=models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    color=models.ForeignKey(Color,on_delete=models.CASCADE)
    filter_price=models.ForeignKey(Filter_Price,on_delete=models.CASCADE)
    
    slug=models.SlugField(blank=True ,null=True)

    
    
    def save (self , *args, **kwargs):
        self.slug=slugify(self.name)
        if self.unique_id is None and self.created_date and self.id:
            self.unique_id = self.created_date.strftime('75%Y%m%d23') + str(self.id)
        return super(Products,self).save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    
class Images(models.Model):
    img=models.ImageField(upload_to='products/')
    product=models.ForeignKey(Products,on_delete=models.CASCADE)

    def __str__(self):
        return str (self.product)

class Tags(models.Model):
    name=models.CharField(max_length=50)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name



class Contact_Us (models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=200)
    subject=models.CharField(max_length=50)
    message=models.TextField(max_length=400)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email



class Order(models.Model):
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    country=models.CharField(max_length=50)
    address=models.TextField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    postcode=models.IntegerField(default=0)
    phone=models.CharField(max_length=50)
    email=models.EmailField(max_length=254)
    additional_info=models.TextField(max_length=1000)
    amount=models.CharField(max_length=50)
    payment_id=models.CharField(max_length=50 , blank=True ,null=True)
    baid=models.BooleanField(default=False ,null=True)
    date=models.DateField(auto_now_add=True)


    def __str__(self):
        return self.user.username
    
    
class Order_Item(models.Model):
    order=models.ForeignKey(Order , on_delete=models.CASCADE)
    product=models.CharField(max_length=50)
    img=models.ImageField(upload_to='order/')
    quantity=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    total=models.TextField(max_length=50)
    
    def __str__(self):
        return self.order.user.username



