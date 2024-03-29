from django.shortcuts import render, get_object_or_404
from blog.models import Post


def blog_view(request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def single_view(request, id):
    post = get_object_or_404(Post, id=id, status=1)
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)



