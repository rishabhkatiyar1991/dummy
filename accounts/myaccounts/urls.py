from django.urls import path
from myaccounts import views
#from django.conf.urls import  re_path
#from django.contrib.auth.views import login, logout


urlpatterns = [
    #path('', views.user_login, name="user_login"),
    path('', views.home, name="home"),
    path('home/', views.home, name="home"),
    path('aclogin/', views.login, name="aclogin"),
    path('success/', views.success,name="success"),
    path('', views.logout, name="logout"),
    #path('homeeee/', views.homeeee, name="homeeee"),
    path('register/', views.register, name="register"),
    path('feelist/', views.feelist, name="feelist"),
    path('details/(?P<id>\d+)/', views.details, name="details"),
    path('editfee/(?P<id>\d+)/', views.editfee, name="editfee")
]