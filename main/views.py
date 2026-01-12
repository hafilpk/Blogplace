
from django.shortcuts import render
from blog.models import Category, Blog

def home(request):
    featured = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    categories = Category.objects.all()
    post = Blog.objects.filter(is_featured=False, status='Published')
    context = {
        'featured': featured,
        'post': post,
    }
    return render(request, "home.html", context)