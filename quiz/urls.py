from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('select-options/', views.select_options, name='select_options'),
    path('quiz/', views.quiz, name='quiz'),
    path('quiz/questions/', views.get_questions, name='get_questions'),
    path('quiz/update-score/', views.update_score, name='update_score'),
    path('game-over/', views.game_over, name='game_over'),
]