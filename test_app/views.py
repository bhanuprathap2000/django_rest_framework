from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TestModel
from .serializers import TestModelSerializer
# Create your views here.

#TestView is a class based view which we inherit from APIView
#we have to define the get,post,put,delete methods in the class we inherit from APIView
class TestView(APIView):

    def get(self,request):
        """
        This method is used to get all the data from the database
        here we are querying the database and getting the data in the form of the queryset
        A QuerySet represents a collection of objects from your database. It can have zero, one or many filters.
        Filters narrow down the query results based on the given parameters. 
        In SQL terms, a QuerySet equates to a SELECT statement, and a filter is a limiting clause such as WHERE or LIMIT .
        """
        serializer=TestModelSerializer(TestModel.objects.all(),many=True)#returns a serializer object since it returns a queryset which is a list of objects we need to specify the many=True
        #here we are getting the data in that case we need to specify from where we are getting the data from
        return Response(serializer.data)#returns the serializer data in the form of a dictionary
    
    def post(self,request):
        """
        This method is used to create a new record in the database
        here we are getting the data from the request object we need to specify the data keyword argument and follwed by the request.data
        since we are getting the data from client we need to validate it before saving it in the database
        if no errors are found then we can save it in the database using the serializer.save() method and return the response the data we saved in the database
        else we can return the errors using the Response method
        """
        serializer=TestModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    
    def put(self,request,*args,**kwargs):
        """
        in case of put request we need to update the fields for existing data
        for that we are expecting the if from frontend we need to send the id of the data which we want to update
        we can get the data as keyword arguments and from that extract the id
        if no id then return the error message
        else we will try to get the instance corresponding to that id
        if no instance then return the error message
        else we will use the serializer and pass the data and instance as keyword arguments
        if the serializer is valid then we can save the data and return the response
        else we can return the errors using the Response method
        """
        id=kwargs.get('id',None)
        if id is None:
            return Response({"message":"id is required"})
        try:
            instance=TestModel.objects.get(id=id)
        except TestModel.DoesNotExist:
            return Response({"message":"id does not exist"})
        serializer=TestModelSerializer(data=request.data,instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



