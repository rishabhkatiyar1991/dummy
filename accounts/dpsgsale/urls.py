from django.urls import path
from dpsgsale import views



urlpatterns = [
    #path('', views.user_login, name="user_login"),
    path('', views.login, name="dlogin"),
    path('dlogin/', views.login, name="dlogin"),
    path('dashbord/', views.dashbord, name="dashbord"),
    path('', views.logout, name="logout"),
    path('registration/', views.registration, name="registration"),
    path('reg_list', views.reglist, name="reg_list"),
    path('product', views.product, name="product"),
    path('product_list', views.product_list, name="product_list"),
    #path('sold_product/(?P<id>\d+)/', views.sold_product, name="sold_product"),
    path('sold_product/<int:id>/', views.sold_product, name="sold_product"),
    path('sold_productlist', views.sold_productlist, name="sold_productlist")
]

