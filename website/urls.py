from django.urls import path
from .views import home
from .views import blog
from .views import create_blog
from .views import add_blog


urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('blog/',blog, name='blog'),  # Blog Page
    path('create_blog/',create_blog, name='create_blog'),
    path('add-blog/', add_blog, name='add_blog'),
]
