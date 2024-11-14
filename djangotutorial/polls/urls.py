from django.urls import path
from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    
    # ex: /polls/5/
    path("specifics/<int:question_id>/", views.DetailView.as_view(), name="detail"),  # Use DetailView as_view()

    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.ResultsView.as_view(), name="results"),

    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# App name to enable namespacing in template URLs
app_name = "polls"
