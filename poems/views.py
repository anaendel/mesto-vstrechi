from django.shortcuts import get_object_or_404, render
from .utils import get_poem_body, get_poem_preview
from .models import Poem


def poem_detail(request, slug):
    poem = get_object_or_404(Poem, slug=slug, is_published=True)
    poem_body = get_poem_body(poem.text)
    return render(request, 'poems/poem_detail.html', {
        'poem': poem,
        'poem_body': poem_body,
    })


def poem_list(request):
    poem = None
    poem_body = None
    if request.GET.get('random') == '1':
        poem = Poem.objects.filter(is_published=True).order_by('?').first()
        if poem:
            poem_body = get_poem_body(poem.text)

    return render(request, 'poems/poem_list.html', {
        'poem': poem,
        'poem_body': poem_body,
    })