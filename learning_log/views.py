from django.shortcuts import render
from .models import Topic, Entry

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_log/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    
    return render(request, 'learning_log/topics.html', {'g_topics': topics})