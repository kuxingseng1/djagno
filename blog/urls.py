from django.urls import path
from . import views
# urlpatterns = [
#      path('search_form/', views.logon, name="logon"),
#      # path('logon/', views.logon),
#      path('search/',views.search),
# ]
urlpatterns = [
     #path('search_form/', views.search_form, name="logon"),
     path('home/', views.logon),
     path('文件/',views.search),
     path('图表/',views.ajax),
     path('ajaxe/', views.ajaxe),
     path('test/', views.form),
]