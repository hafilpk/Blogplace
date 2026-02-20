from django.shortcuts import render
from blog.models import Blog, Category
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        'category_count': category_count,
        'blogs_count': blogs_count,
    }
    return render(request, 'dashboards/dashboard.html', context)

def categories(request):
    return render(request, 'dashboards/categories.html')    