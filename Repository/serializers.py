from rest_framework import serializers
from Repository.models import Questions

class QuestionSerializer(serializers.Serializer):


    title = serializers.CharField(max_length=200)
    
    language = serializers.ChoiceField(choices=Questions.Language_Choices,default="python")

    difficulty_level = serializers.ChoiceField(choices=Questions.Difficulty_level,default="easy")

    notes = serializers.CharField()
    topic = serializers.CharField()

    published_date = serializers.DateTimeField(read_only=True)

    sample_input = serializers.CharField()
    sample_output = serializers.CharField()

    is_active = serializers.BooleanField()