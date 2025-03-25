from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Author, Comment
from .forms import CommentForm

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
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(
                name=form.cleaned_data['name'],
                text=form.cleaned_data['text'],
                article=post
            )
            
            new_comment.ip = request.META.get('REMOTE_ADDR')
            new_comment.user_agent = request.META.get('HTTP_USER_AGENT')
                
            new_comment.save()
            return redirect('blog-post-detail', pk=post.pk)
    else:
        form = CommentForm()
    
    context = {
        'post': post,
        'form': form,
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
