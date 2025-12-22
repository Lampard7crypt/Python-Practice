from django.shortcuts import render, HttpResponse, redirect
from .forms import CommentForm, SignupForm


posts = [
    {'author': 'Corey Schafer',
     'title': 'A new Blog post',
     'content': 'First content',
     'date_posted': 'October 9, 2025'},
    {'author': 'Test User',
     'title': 'A Second Blog post',
     'content': 'Second content',
     'date_posted': 'October 19, 2025'}
]

def index(request):
    return render(request, 'blog/home.html', {'posts':posts}) # dict there == faking capyured values

def about(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Success Bihh ahh nigga!')
    else:
        form = CommentForm()
    return render(request, 'blog/about.html', {'form': form})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'blog/signup.html', {'form': form})