from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Content

# Create your views here.

def home(request):
    page = Content.objects.filter(
        slug='home',
        status='published'
    ).first()

    theme = request.site_settings.active_theme if hasattr(request, 'site_settings') else 'default'

    return render(
        request,
        f'themes/{theme}/page.html',
        {'content': page}
    )


def content_detail(request, slug):
    content = get_object_or_404(
        Content,
        slug=slug,
        status='published'
    )

    template = f"themes/default/{content.content_type}.html"
    return render(request, template, {'content': content})
