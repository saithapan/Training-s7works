from django.urls import path, include
from . import views
from .views import ArticleViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    
    #Function based views
    # path('article/', views.article_list, name='article'),
    # path('detail/<int:pk>/', views.article_detail, name='article_detail'),

    # class based views
    path('article/', views.ArticleAPIView.as_view(), name='article'),
    path('detail/<int:id>/', views.ArticleDetails.as_view(), name='article_detail'),

    # Generic based view
    path('generic/article/<int:id>/', views.GenericAPIView.as_view(), name='article'),

    # viewset
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls))


]