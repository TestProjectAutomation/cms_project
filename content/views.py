from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Content

# Create your views here.

def content_detail(request, slug):
    content = get_object_or_404(
        Content,
        slug=slug,
        status='published'
    )

    template = f"themes/default/{content.content_type}.html"
    return render(request, template, {'content': content})
