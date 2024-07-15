from django.shortcuts import render  ,redirect 
from store_app.models import Products , Categories , Filter_Price , Color , Brand , Contact_Us
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from cart.cart import Cart
from store_app.forms import Order_Form 
from django.contrib.auth import logout


def HOME (request):
    products = Products.objects.filter(condition='New')
    product_headers = Products.objects.filter(condition='Header')
    context={
        'products':products,
        'product_headers':product_headers,
      #   'hello' : _('f اهلا')
    }
    return render(request , 'main/home.html' , context)


def BASE (request):
    return render(request , 'main/base.html' )
 

def SEARCH (request):
    query=request.GET.get('query')
    products = Products.objects.filter(name__icontains = query)
    
    context={
       'products':products
    }
    
    return render(request , 'main/search.html' , context)


def PRODUCTS (request):
    products = Products.objects.all()
    paginator = Paginator(products, 12)
    page_number = request.GET.get("page")
    products = paginator.get_page(page_number)

    
    categories = Categories.objects.all()
    filter_price = Filter_Price.objects.all()
    colors = Color.objects.all()
    brands = Brand.objects.all()
    
    categories_id=request.GET.get('categories')
    filter_price_id=request.GET.get('filter_price')
    colors_id=request.GET.get('color')
    brands_id=request.GET.get('brand')
    
    ATOZ_ID=request.GET.get('ATOZ')
    ZTOA_ID=request.GET.get('ZTOA')
    
    HIGHTOLOW_ID=request.GET.get('HIGHTOLOW')
    LOWTOHIGH_ID=request.GET.get('LOWTOHIGH')
    
    NEWBYOLD_ID=request.GET.get('NEWBYOLD')
    OLDBYNEW_ID=request.GET.get('OLDBYNEW')
    
    if categories_id:
       products = Products.objects.filter(categories = categories_id)
       
    elif filter_price_id:
       products= Products.objects.filter(filter_price = filter_price_id)
       
    elif colors_id:
       products= Products.objects.filter(color = colors_id)
       
    elif brands_id:
       products= Products.objects.filter(brand = brands_id)
       
       
    elif ATOZ_ID:
       products= Products.objects.filter(status='Publish').order_by('name')
       
    elif ZTOA_ID:
       products= Products.objects.filter(status='Publish').order_by('-name')
       
       
    elif HIGHTOLOW_ID:
       products= Products.objects.filter(status='Publish').order_by('price')
       
    elif LOWTOHIGH_ID:
       products= Products.objects.filter(status='Publish').order_by('-price')
       
       
    elif NEWBYOLD_ID:
       products= Products.objects.filter(status='Publish' , condition='New').order_by('-id')
       
    elif OLDBYNEW_ID:
       products= Products.objects.filter(status='Publish' , condition='Old').order_by('-id')
       
       
    else:
       products = Products.objects.filter(status='Publish').order_by('-id')
    
     
    context={
        'products':products,
        'categories':categories,
        'filter_price':filter_price,
        'colors':colors,
        'brands':brands,
    }
    return render(request , 'main/products.html' , context )


def PRODUCT_DETAILS (request , slug):
    product_details = Products.objects.get(slug = slug)
    context={
        'product_details' : product_details
    }
    return render(request , 'main/product_details.html' , context)
 
 
def CONTACT_US (request):
   if request.method == 'POST':
      name = request.POST.get('name')
      email = request.POST.get('email')
      subject = request.POST.get('subject')
      message = request.POST.get('message')
      
      contact = Contact_Us(
         name = name,
         email = email,
         subject = subject,
         message = message, 
      )
      
      subject = subject
      message = message
      email = email
      try:
         send_mail(subject,message,'settings.EMAIL_HOST_USER',[email])
         contact.save()
         return redirect('/')
      except:
         return redirect('/contact_us')
         
      
   return render(request , 'main/contact_us.html' )
 
 
# CART ----------------------------------
  
@login_required(login_url="login")
def cart_add(request, id):
      cart = Cart(request)
      product = Products.objects.get(id=id)
      cart.add(product=product)
      return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="login")
def item_clear(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.remove(product)
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="login")
def item_increment(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.add(product=product)
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Products.objects.get(id=id)
    cart.decrement(product=product)
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url="login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')
 
 
 
 

@login_required(login_url="login")
def cart_checkout(request):
    return render(request, 'cart/checkout.html')
 
 

def signout(request):
    logout(request)
    return redirect('/')
