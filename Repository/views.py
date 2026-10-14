from django.shortcuts import render
from Repository.models import Questions
from Repository.serializers import QuestionSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class QuestionListCreateView(APIView):
    def get(self,request):
        qs=Questions.objects.all()  #collection of Questions
        serializer_instance=QuestionSerializer(qs,many=True)
        #many=True means tells the serialiser that the input contain multiple objects
        return Response(serializer_instance.data)
    #Returns the sreialized data as a reponse
    def post(self,request):
        form_data=request.data      #form_data dictionary -----> python native type
        serializer_instance=QuestionSerializer(data=form_data)#create serializer instance with form data
        if serializer_instance.is_valid():# check if the data is valid according to the seraializers validation request
            actual_data=serializer_instance.validated_data# get the validated data from the serializer
            Questions.objects.create(**actual_data)#create a new question object using the validated data
            return Response(data=serializer_instance.data)#return the serialized data as response
        else:
            return Response(serializer_instance.errors)#returns validation response as a response
class QuestionRetreveUpdateDeleteView(APIView):
    def get(self,request,pk):
        qs=Questions.objects.get(id=pk)
        serializer_instance=QuestionSerializer(qs)
        return Response(data=serializer_instance.data)
    def put(self,request,pk):
        form_data=request.data

        serializer_instance=QuestionSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            Questions.objects.filter(id=pk).update(**actual_data)
            return Response(data=serializer_instance.data)
        else:
            return Response(data=serializer_instance.errors)

