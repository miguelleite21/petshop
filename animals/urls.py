
from django.urls import path

from animals.views import AnimalsView,AnimalsIdView

urlpatterns = [
    path("animals/", AnimalsView.as_view()),
    path("animals/<int:id>/", AnimalsIdView.as_view()),

]