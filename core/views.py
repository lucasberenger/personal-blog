from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Post, Comment, Category
from .forms import CommentForm

## Homepage view 
class HomeView(View):
    
    def get(self, request):
        posts = Post.objects.all().order_by('-created_on')
        context = {
            'posts': posts,
        }
        return render(request,'home.html', context)

# Detail
class BlogDetailView(View):

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        comments = Comment.objects.filter(post=post)

        context = {
            'post': post,
            'comments': comments,
            'form': CommentForm()
        }

        return render(request, 'details.html', context)

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        form = CommentForm(data=request.POST)

        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data['author'],
                body=form.cleaned_data['body'],
                post=post,
            )

            comment.save()

            return redirect('blog_detail', pk=pk)

        comments = Comment.objects.filter(post=post)
       
        context = {
           'post': post,
           'comments': comments,
           'form': CommentForm(),
        }

        return render(request, 'details.html', context)


# Category
class BlogCategoryView(View):

    def get(self, request, category):
        posts = Post.objects.filter(
            categories__name__contains=category
        ).order_by('-created_on')

        context = {
            'category': category,
            'posts': posts,
        }

        return render(request, 'category.html', context)
