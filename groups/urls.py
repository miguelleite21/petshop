
from django.urls import path

from groups.views import GroupsView,GroupsIdView

urlpatterns = [
    path("groups/", GroupsView.as_view()),
    path("groups/<int:id>/", GroupsIdView.as_view()),

]

