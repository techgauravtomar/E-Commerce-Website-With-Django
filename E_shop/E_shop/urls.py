"""
URL configuration for E_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from app.views import*
from django.contrib.auth import login,logout
from django.urls import include,path,re_path
from django.conf import settings
from django.conf.urls.static import static
# from . import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('app.urls')),
    path('',hometwo,name="hometwo"),
    path('home-one',homeone,name="homeone"),
    path('about-us/',aboutus,name="about"),
    path('page404/',page404,name="page404"),
    path('order-tracking/',ordertracking,name="ordertracking"),
    path('faq/',faq,name="faq"),
    path('comingsoon/',comingsoon,name="comingsoon"),
    # path('cart/',cart,name="cart"),
    path('checkout/',checkout,name="checkout"),
    path('compare/',compare,name="comparepage"),
    path('wishlist/',wishlist,name="wishlist"),
    path('accountpage/',accountpage,name="accountpage"),
    path('HandleRegister/',HandleRegister,name="register"),
    path('Handlelogin/',HandleLogin,name="login"),
    path('HandleLogout/',HandleLogout,name="logout"),
    path('emptycart/',emptycart,name="emptycart"),
    path('thankyoupage/',thankyoupage,name="thankyoupage"),
    path('shop_3_column/',shop_3_column,name="shop_3_column"),
    path('shop_4_column/',shop_4_column,name="shop_4_column"),
    path('shop_left_sidebar/',shop_left_sidebar,name="shop_left_sidebar"),
    path('shop_right_sidebar/',shop_right_sidebar,name="shop_right_sidebar"),
    path('shop_list_left_sidebar/',shop_list_left_sidebar,name="shop_list_left_sidebar"),
    path('shop_list_right_sidebar/',shop_list_right_sidebar,name="shop_list_right_sidebar"),
    path('single_product/<str:id>',single_product,name="single_product"),
    path('product_variable/',product_variable,name="product_variable"),
    path('product_affiliate/',product_affiliate,name="product_affiliate"),
    path('product_group/',product_group,name="product_group"),
    path('single_product_tabstyle_2/',single_product_tabstyle_2,name="single_product_tabstyle_2"),
    path('single_product_tabstyle_3/',single_product_tabstyle_3,name="single_product_tabstyle_3"),
    path('single_product_slider/',single_product_slider,name="single_product_slider"),
    path('single_product_gallery_left/',single_product_gallery_left,name="single_product_gallery_left"),
    path('single_product_gallery_right/',single_product_gallery_right,name="single_product_gallery_right"),
    path('single_product_sticky_left/',single_product_sticky_left,name="single_product_sticky_left"), 
    path('single_product_sticky_right/',single_product_sticky_right,name="single_product_sticky_right"),  
    path('contact/',contact,name="contact"),
    path('search/',search,name="search"),
    
    path('cart/add/<int:id>/',cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/',cart_detail,name='cart'),
]  + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)