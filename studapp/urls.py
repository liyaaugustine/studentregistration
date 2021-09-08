from django.urls import path
from . import views
urlpatterns = [
    path('studlogin',views.studlogin,name='studlogin'),
    path('signup',views.signup, name='signup'),
    path('admin',views.admin, name='admin'),
    path('studhome',views.studhome, name='studhome'),
    path('sprofile',views.sprofile, name='sprofile'),
    path('studlogout',views.studlogout, name='studlogout'),
    path('active', views.active, name='active'),
    path('inactive', views.inactive, name='inactive'),
    path('emailcheck',views.emailcheck, name='emailcheck'),
    path('inactivate/<int:inid>',views.inactivate, name='inactivate'),
    path('activate/<int:acid>',views.activate, name='activate'),
    path('updprofile',views.updprofile, name='updprofile'),
    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('welcome',views.welcome, name='welcome'),
    path('alogout',views.alogout, name='alogout')
]