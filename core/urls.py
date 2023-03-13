from django.urls import path 
from . import views
from .views import shopView, OrderSummary

urlpatterns = [
    path('', views.index, name='index'),
    path('shop', shopView.as_view(), name='shop'),
    path('checkout', views.checkout, name='checkout'),
    path('product_details/<slug>', views.product_details, name='product-details'),
    path('cakes', views.cakes, name='cakes'),
    path('blog', views.blog, name='blog'),
    path('about_us', views.about_us, name='about-us'),
    path('menu', views.menu, name='menu'),
    path('contact_us', views.contact, name='contact-us'),
    path('add_to_cart/<slug>', views.add_to_cart, name='add-to-cart'),
    path('order_summary', OrderSummary.as_view(), name='cart'),
    path('remove_from_cart/<slug>', views.remove_from_cart, name='remove-from-cart'),
    path('shop_stands', views.shop_stands, name='shop-stands'),
    path('shop_cakes', views.shop_cakes, name='shop-cakes'),
    path('shop_decorating_tools', views.shop_decorateTools, name='shop-decorating-tools'),
    path('shop_decoration', views.shop_decoration, name='shop-decoration'),
    path('shop_bake_materials', views.shop_bakeMat, name='shop-bakeMat'),
    path('shop_packaging_materials', views.shop_packageMat, name='shop-packageMat'),
    path('wedding_cakes', views.weddingCake, name='wedding-cakes'),
    path('birthday_cakes', views.birthdayCake, name='birthday-cakes'),
    path('shop_search_results', views.searchShop, name='search-shop'),
    path('login', views.login, name='login'),
]