from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'learning_log/index.html')

def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    
    return render(request, 'learning_log/topics.html', {'topics': topics})

def topic_detail(request, topic_id):
    """Show a topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')

    return render(request, 'learning_log/topic_detail.html', {'topic': topic, 'entries': entries})

def new_topic(request):
    """Add a new topic."""
    
    if request.method != 'POST':
            form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('learning_log:topics')

    return render(request, 'learning_log/new_topic.html', {'form': form})