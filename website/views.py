from django.shortcuts import render, redirect
from .forms import BlogForm
from django.utils import timezone  # Import timezon
from .models import Blog
from django.http import HttpResponse
from .models import Comment

# Create your views here.


def home(request):
    return render(request, "website/index.html")
def blog(request):
    
    comments = Comment.objects.all().order_by('-created_at')  # Fetch all comments, newest first
    blogs=Blog.objects.all().order_by('-created_at') 
    return render(request, 'website/blog.html', {'comments': comments,'blogs': blogs})
def create_blog(request):
    return render(request, "website/create_blog.html")
def add_blog(request):
    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        title = request.POST.get('title')
        detail = request.POST.get('detail')

        print(f"Name: {name}, Title: {title}, Detail: {detail}")

        # Create a new Blog object and save it to the database
        new_blog = Blog(name=name, title=title, detail=detail)
        new_blog.save()

        # Redirect after saving
        return redirect('blog')  # Replace with your actual success URL

    return render(request, 'website/create_blog.html')
def submit_comment(request):
    if request.method == 'POST':
        comment_text = request.POST.get('comment')
        name = request.POST.get('name', 'Anonymous') # Get name or default to Anonymous

        if comment_text:  # Check if comment is not empty
            comment = Comment(name=name, comment=comment_text)
            comment.save()
            return redirect('blog')  # Redirect to a success page or back to the same page.
        else:
            # Handle empty comment submission (optional)
            return render(request, 'website/blog.html', {'error': 'Comment cannot be empty.'}) #example of error handling

    # Handle GET requests (optional, if you want to display the form initially)
    return render(request, 'website/blog.html')
def display_comments(request):
    comments = Comment.objects.all().order_by('-created_at')  # Fetch all comments, newest first
    return render(request, 'website/blog.html', {'comments': comments})
