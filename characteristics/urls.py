

from django.urls import path

from characteristics.views import CharacteristicsView,CharacteristicsIdView

urlpatterns = [
    path("characteristics/", CharacteristicsView.as_view()),
    path("characteristics/<int:id>/", CharacteristicsIdView.as_view()),

]