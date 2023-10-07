from django.shortcuts import render
from .models import Topic, Entry

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_log/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    
    return render(request, 'learning_log/topics.html', {'topics': topics})

def topic_detail(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    return render(request, 'learning_log/topic_detail.html', {'topic': topic, 'entries': entries})