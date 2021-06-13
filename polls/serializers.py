from rest_framework import serializers
from polls.models import Question, Choice, Answer 

# from polls.models import Question, Answer, Result
# class QuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Question
#         fields = ['id', 'title']
#         read_only_fields = ['id']

# class AnswerSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Answer
#         fields = ['answers']
#         read_only_fields = ['id']

# class ResultSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Result
#         fields = ['user', 'question', 'user_answer']
#         read_only_fields = ['id']

class ChoiceSerializer(serializers.ModelSerializer):
    percent = serializers.SerializerMethodField()

    class Meta:
        model = Choice
        fields = ['pk', 'points', 'percent', 'lock_other', ]

    def get_percent(self, obj):
        total = Answer.objects.filter(question=obj.question).count()
        current = Answer.objects.filter(question=obj.question, choice=obj).count()
        if total != 0:
            return float(current * 100 / total)
        else:
            return float(0)


class QuestionSerializer(serializers.ModelSerializer):
    choices = ChoiceSerializer(many=True, source='choice_set', )

    class Meta:
        model = Question
        fields = ['pk', 'title', 'choices', 'max_points', ]


class AnswerSerializer(serializers.Serializer):
    answers = serializers.JSONField()

    def validate_answers(self, answers):
        if not answers:
            raise serializers.Validationerror("Answers must be not null.")
        return answers

    def save(self):
        answers = self.data['answers']
        user = self.context.user
        for question_id in answers:  # тут наверное лишняя запятая , ошибка в оригинальном коде
            question = Question.objects.get(pk=question_id)
            choices = answers[question_id]
            for choice_id in choices:
                choice = Choice.objects.get(pk=choice_id)
                Answer(user=user, question=question, choice=choice).save()
                user.is_answer = True
                user.save()