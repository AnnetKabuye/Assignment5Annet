from django.shortcuts import render

# Create your views here.
from myblog.models import myBlog, Category
from django.shortcuts import render_to_response, get_object_or_404
from .forms import PostForm

def index(request):
    return render_to_response('index.html', {
        'categories': Category.objects.all(),
        'posts': myBlog.objects.all()[:5]
    })

def view_post(request, slug):   
    return render_to_response('view_post.html', {
        'post': get_object_or_404(myBlog, slug=slug)
    })

def view_category(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('view_category.html', {
        'category': category,
        'posts': myBlog.objects.filter(category=category)[:5]
    })
def post_new(request):
    form = PostForm()
    return render_to_response('post_edit.html', {'form': form})