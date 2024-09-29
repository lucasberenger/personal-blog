from django.urls import path
from .views import HomeView, BlogDetailView, BlogCategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(), name='blog_detail',),
    path('category/<category>/',BlogCategoryView.as_view(), name='blog_category'),
]