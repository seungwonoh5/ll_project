from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

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

def new_entry(request, topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id=topic_id)

    # No data submitted; create a blank form.
    if request.method != 'POST':
            form = EntryForm()
    else:    
        # POST data submitted; process data.
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            print(new_entry)
            new_entry.topic = topic # assign new entry to the topic
            new_entry.save()

            return redirect('learning_log:topic_detail', topic_id=topic_id)

    return render(request, 'learning_log/new_entry.html', {'topic':topic, 'form': form})

def edit_entry(request, entry_id):
    """Add a new entry for a particular topic."""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    # No data submitted; create a blank form.
    if request.method != 'POST':
            form = EntryForm(instance=entry)
    else:    
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('learning_log:topic_detail', topic_id=topic.id)

    return render(request, 'learning_log/edit_entry.html', {'entry': entry, 'topic':topic, 'form': form})