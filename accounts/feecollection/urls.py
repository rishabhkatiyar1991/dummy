from django.urls import path
from feecollection import views
#from django.conf.urls import  re_path
#from django.contrib.auth.views import login, logout


urlpatterns = [
    #path('', views.user_login, name="user_login"),
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('fee_dashbord', views.fee_dashbord, name="fee_dashbord"),
    path('feelogin', views.feelogin, name="feelogin"),
    path('feefinddate', views.feefinddate, name="feefinddate"),
    path('fee_logout', views.fee_logout, name="fee_logout"),

]