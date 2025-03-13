from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, "website/index.html")
def blog(request):
    return render(request, "website/blog.html")
