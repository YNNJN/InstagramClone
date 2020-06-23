from django import template

register = template.Library()

@register.filter
def add_link(post):
    content = post.content
    # QuerySet
    tags = post.tags.all()

    for tag in tags:
        content = content.replace(
            f'{tag.name}', f'<a href="/posts/tags/{tag.name}/">{tag.name}</a>')
    return content