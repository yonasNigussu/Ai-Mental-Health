from django.urls import path
from .views import home
from .views import blog
from .views import create_blog
from .views import add_blog
from . import views


urlpatterns = [
    path('', home, name='home'),  # Home page URL
    path('blog/',blog, name='blog'),  # Blog Page
    path('create_blog/',create_blog, name='create_blog'),
    path('add_blog/', add_blog, name='add_blog'),
    path('submit_comment/', views.submit_comment, name='submit_comment'),
    
    #path('show_comments/', views.show_comments, name='show_comments'),
    
]
