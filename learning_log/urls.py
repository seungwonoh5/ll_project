"""URL configuration for learning_logs."""

from django.urls import path

from . import views

app_name = 'learning_log'
urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    # Page that shows all topics.
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>', views.topic_detail, name='topic_detail')
]