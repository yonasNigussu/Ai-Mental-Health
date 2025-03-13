from django.urls import path
from .views import home
from .views import blog

urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('blog/',blog, name='blog'),  # Blog Page
]
