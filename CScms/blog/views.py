from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Author

def home(request):
    category_id = request.GET.get('category')  # Get category ID from request
    posts = Post.objects.all()

    if category_id:
        posts = posts.filter(category_id=category_id)

    categories = Category.objects.all()

    author_id = request.GET.get('author')
    authors = Author.objects.all()

    context = {
        'authors': authors,
        'posts': posts,
        'categories': categories,
        'selected_category': int(category_id) if category_id else None,
        'selected_author': int(author_id) if author_id else None,
    }

    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    context = {
        'post': post,
    }
    
    return render(request, 'blog/post_detail.html', context)

def author_posts(request, author_id):
    author = Author.objects.get(id=author_id)  # Fetch the Author object
    posts = author.posts.all()  # Get all posts related to this author

    context = {
        'posts': posts,
        'author': author,
    }

    return render(request, 'blog/author_posts.html', context)
