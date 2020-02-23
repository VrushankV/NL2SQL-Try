from django.conf.urls import url,include
from . import views

app_name='basic'
urlpatterns=[
    url(r'^$',views.index,name='index'),
url(r'^upload/$',views.simple_upload,name='upload')
]