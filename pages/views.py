from django.shortcuts import render
from feedback.forms import FeedbackForm
from materials.models import Material

def index(request):
    form = FeedbackForm()
    return render(request, 'pages/index.html', {'form': form})

def poems(request):
    return render(request, 'poems/poem_list.html')

def materials(request):
    materials = Material.objects.filter(is_published=True)
    return render(request, 'pages/materials.html', {'materials': materials})