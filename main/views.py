
from django.shortcuts import render
from blog.models import Category, Blog

def home(request):
    featured = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    categories = Category.objects.all()
    context = {
        'categories':categories,
        'featured': featured,
    }
    return render(request, "home.html", context)