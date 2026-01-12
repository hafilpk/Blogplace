from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Category


def category_page(request, category_id):
    posts = Blog.objects.filter(status='Published', category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')

    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'category_page.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')
    
    context = {
        'single_blog': single_blog,
    }
    return render(request, 'blog.html', context)