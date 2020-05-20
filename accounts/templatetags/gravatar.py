import hashlib
from django import template

register = template.Library()

@register.filter
def profile_url(email):
    return f"https://s.gravatar.com/avatar/{hashlib.md5(self.email.encode('utf-8').strip().lower()).hexdigest()}?s=170&d=mp"
