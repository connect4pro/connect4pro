from django.forms import ModelForm, Textarea
from .models import QuestionsAndAnswers


class PostModelForm(ModelForm):
    class Meta:
        model = QuestionsAndAnswers
        fields = ('__all__')
        widgets = {
            'question': Textarea(attrs={'cols': 80, 'rows': 15}),
            'answer': Textarea(attrs={'cols': 80, 'rows': 15}),
        }
