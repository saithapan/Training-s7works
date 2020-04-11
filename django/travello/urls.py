from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    # path(r'^([0-9]+)/$',views.detail,name='detail')
    path('post_url',views.post_destination, name='post_destination') # use for posting the newcity from ui itself
]