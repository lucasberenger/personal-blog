from django.urls import path
from .views import HomeView, BlogDetailView, BlogCategoryView, AboutView, ContactView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(), name='blog_detail',),
    path('category/<category>/',BlogCategoryView.as_view(), name='blog_category'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact')
]