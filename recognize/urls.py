

from django.urls import path
from . import views


#url本地路由，recognize这个应用里面的本地路由
urlpatterns = [
    # path('', views.msgproc),
    path('', views.upload_file),

]

