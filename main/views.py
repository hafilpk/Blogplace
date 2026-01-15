
from django.shortcuts import render, redirect
from blog.models import Category, Blog
from .forms import RegistrationForm

def home(request):
    featured = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    categories = Category.objects.all()
    post = Blog.objects.filter(is_featured=False, status='Published')
    context = {
        'featured': featured,
        'post': post,
    }
    return render(request, "home.html", context)

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form': form,
    }
    return render(request, 'register.html', context)