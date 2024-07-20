
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from project import views

urlpatterns = [
    path('i18/', include ('django.conf.urls.i18n'))
]

urlpatterns += i18n_patterns(
    path('accounts/',include("django.contrib.auth.urls")),
    path('accounts/',include("accounts.urls",namespace="accounts")),

    path('admin/', admin.site.urls ),
    path('' , views.HOME , name='home'),
    path('base/' , views.BASE , name='base'),
    
    path('products/' , views.PRODUCTS , name='products'),
    path('product_details/<str:slug>' , views.PRODUCT_DETAILS , name='product_details'),
    
    path('search/' , views.SEARCH , name='search'),
    path('contact_us/' , views.CONTACT_US , name='contact_us'),
    
    # CART------------------------------------------
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
    # checkout------------------------------------------ 
    path('cart/checkout/',views.cart_checkout,name='cart_checkout'),
    path('placholder/',views.placholder,name='placholder'),
    
    
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)