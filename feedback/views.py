from django.shortcuts import redirect, render

from .forms import FeedbackForm

def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('pages:index') 

def success_view(request):
    return render(request, 'feedback/success.html')
    
