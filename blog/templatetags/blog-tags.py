from django import template
register = template.Library()
from blog.models import Post


@register.filter
def snippet(value, arg=20):
    return value[:arg] + "..."


@register.inclusion_tag('blog/blog-post-popular.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status = 1).order_by('published_date')[:arg]
    return {'posts' : posts}
