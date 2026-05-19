from django.shortcuts import render
from feedback.forms import FeedbackForm

def index(request):
    form = FeedbackForm()
    return render(request, 'pages/index.html', {'form': form})

def poems(request):
    return render(request, 'poems/poem_list.html')

def materials(request):
    return render(request, 'pages/materials.html')

