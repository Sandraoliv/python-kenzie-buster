from django.urls import path
from movies.views import MoviesView, DetailMovieView, MovieOrderView


urlpatterns = [
    path('movies/', MoviesView.as_view()),
    path("movies/<int:movie_id>/", DetailMovieView.as_view()),
    path("movies/<int:movie_id>/orders/", MovieOrderView.as_view()),
]