from django import forms
from django.forms.widgets import RadioSelect, Textarea



class QuestionForm(forms.Form):

    def __init__(self, questions, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.questions = questions
        for question in questions:
            field_name = "question_%d" % question.pk
            choices = []
            print("questions",question)
            for answer in question.answer_set.all():
                choices.append((answer.pk, answer.text,))
            ## May need to pass some initial data, etc:
            field = forms.ChoiceField(label=question.label, required=True, 
                                      choices=choices, widget=forms.RadioSelect)
        

