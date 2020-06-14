from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import (get_object_or_404, redirect, render,
                              render_to_response)
from django.views.generic.base import View
from django.views.generic.list import ListView
from quiz.forms import QuestionForm
from quiz.models import Question, Quiz, QuizTakers


class UserLoginAPI(View):
    
    def get(self, request, *args, **kwargs):
        return render(request, "login.html", {})

    def post(self, request, *args, **kwargs):

        error_message = None
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username.strip(), password=password)
        
        if user is None:
            error_message = 'Password or Email Incorrect'
        elif not user.is_active:
            error_message = 'Your account is inactive.'
        else:
            login(request,user)

        if error_message:
            response = {
                'success': False,
                'message': error_message,
            }

        else:
            response = {
                'success': True,
                'message': 'User successfully logged in.',
                'redirect': 'quiz/list-quiz/'
            }
        return JsonResponse(response)


class QuizListView(ListView):
    
    model = Quiz
    template_name = 'quiz_list.html'

    def get_queryset(self):
        queryset = super(QuizListView, self).get_queryset()
        return queryset.filter(roll_out=True)


class QuizTake(ListView):
    
    def get(self, request, quiz_name):
        quiz = Quiz.objects.filter(name__icontains=quiz_name, roll_out=True).first()
        questions = quiz.question_set.all() if quiz else {}
        return render_to_response('question.html', {"questions": questions})


class SubmitAnswers(View):
    
    def post(self, request, quiz_name):
        quiz = Quiz.objects.filter(name__icontains=quiz_name, roll_out=True).first()
        questions = quiz.question_set.all() if quiz else {}
        return render_to_response('question.html', {"questions": questions})

class GetUserData(View):
    
    def get(self, request):
        quiz_takers = QuizTakers.objects.all()
        user_list = []
        for takers in quiz_takers:
            user_data = {'user': takers.user.username, 'quiz': takers.quiz.name, 'score':takers.correct_answers}
            user_list.append(user_data)
        return JsonResponse({"user_list": user_list})
