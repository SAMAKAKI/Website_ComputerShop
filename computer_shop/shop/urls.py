from django.urls import path
from .views import *

urlpatterns = [
    path('', ShopHome.as_view(), name='home'),
    path('about/', ShopAboutUs, name='about_us'),
    path('shop/', ShopShop.as_view(), name='shop'),
    path('contact/', ShopContact.as_view(), name='contact'),
    path('post_elem/<slug:post_elem_slug>/', ShowCompElem.as_view(), name='post_elem'),
    path('shop/<slug:cat_elem_slug>', ShowCatCompElem.as_view(), name='cat_elem'),
    path('register/', ShopRegister.as_view(), name='register'),
    path('login/', ShopLogin.as_view(), name='login'),
    path('logout/', ShopLogout, name='logout'),
]