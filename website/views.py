from django.shortcuts import render, redirect
from .forms import BlogForm
from django.utils import timezone  # Import timezone

# Create your views here.


def home(request):
    return render(request, "website/index.html")
def blog(request):
    return render(request, "website/blog.html")
def create_blog(request):
    return render(request, "website/create_blog.html")
def add_blog(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        title = request.POST.get('title')
        detail = request.POST.get('detail')

        if not name:
            # Generate a default incremental name
            last_blog = BlogForm.objects.order_by('-id').first()
            if last_blog:
                last_id = last_blog.id
                name = f"Anonymous {last_id + 1}"
            else:
                name = "Anonymous 1"

        BlogForm.objects.create(name=name, title=title, detail=detail, created_at=timezone.now())
        return redirect('website/index.html')  # Redirect to your home page or blog list

    return render(request, 'website/blog.html')  # Render the form template
