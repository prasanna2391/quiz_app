from django.urls import path
from quiz.views import QuizListView, QuizTake, SubmitAnswers, GetUserData

urlpatterns = [
    path('list-quiz/', QuizListView.as_view(), name='list-quiz'),
    path('<quiz_name>/', QuizTake.as_view(), name='quiz-question'),
    path('submit-answers/', SubmitAnswers.as_view(), name='submit-answers'),
    
]