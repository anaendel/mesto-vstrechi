from django.shortcuts import get_object_or_404, render

from .models import Author
from poems.utils import get_poem_preview

def author_list(request):
    selected_letter = request.GET.get('letter')

    authors = Author.objects.filter(is_published=True).order_by('name')

    if selected_letter:
        authors = authors.filter(name__istartswith=selected_letter)

    alphabet = list('АБВГДЕЖЗИКЛМНОПРСТЭЮЯ')

    return render(
        request,
        'authors/author_list.html',
        {
            'authors': authors,
            'alphabet': alphabet,
            'selected_letter': selected_letter,
        }
    )


def author_detail(request, slug):
    author = get_object_or_404(Author, slug=slug, is_published=True)
    poems = author.poems.filter(is_published=True)
    poems_with_preview = [
        {'poem': p, 'preview': get_poem_preview(p.text)}
        for p in poems
    ]
    return render(
        request,
        'authors/author_detail.html',
        {'author': author, 'poems_with_preview': poems_with_preview}
    )