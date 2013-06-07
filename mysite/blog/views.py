from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import markdown2

from blog.models import Post, Blog, Author

def index(request):
    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    if len(Blog.objects.all()) > 0:
        blog = Blog.objects.get(id=1).title
    else:
        blog = None
    if len(Author.objects.all()) > 0:
        author = Author.objects.get(id=1)
    else:
        author = None
    context = {'latest_post_list': latest_post_list, 'blog': blog, 'author':author}
    return render(request, 'blog/index.html', context)

def post(request, post_year, post_month, post_day, post_slug):
    post = Post.objects.get(slug=post_slug)
    post_title = post.title
    post_author = post.author
    post_date = post.pub_date
    post_body = markdown2.markdown(post.body)
    context = {'post_title':post_title, 'post_body':post_body, 'post_date':post_date, 'post_author':post_author}
    return render(request, 'blog/post.html', context)

'''
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            
        else:
            # Return a 'disabled account' error message
        else:
            # Return an 'invalid login' error message
'''
