from django.contrib import admin
from quiz.models import Quiz, Question, Answer, QuizTakers, Response
from .utils import export_to_csv


class QuizAdmin(admin.ModelAdmin):
    
    list_display = ('name', 'questions_count', 'slug')

    search_fields = (
        'name',
    )
    list_filter = (
        'name',
    )

class QuestionAdmin(admin.ModelAdmin):
    
    list_display = ('quiz', 'label',)

    search_fields = (
        'quiz',  'label'
    )

class AnswerAdmin(admin.ModelAdmin):
    
    list_display = ('question', 'text', 'is_correct')

    search_fields = (
        'question',  'text'
    )

class QuizTakersAdmin(admin.ModelAdmin):
    
    list_display = ('user', 'quiz', 'correct_answers', 'completed')

    search_fields = (
        'quiz',  'user'
    )
    actions = [export_to_csv, ]

class ResponseAdmin(admin.ModelAdmin):
    
    list_display = ('quiztaker', 'question', 'answer')

    search_fields = (
        'quiztaker', 
    )


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuizTakers, QuizTakersAdmin)
admin.site.register(Response, ResponseAdmin)