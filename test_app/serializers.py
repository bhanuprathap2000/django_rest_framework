from rest_framework import serializers 
from .models import TestModel
class TestModelSerializer(serializers.ModelSerializer):
    #if we use the model serializer then we dont need to specify the fields
    #the methods to create and update are automatically created
    #we just need to say the fields that we want to be included in the serializer and the model that we want to serialize in the class Meta that's it
    class Meta:
        model=TestModel
        fields="__all__"
    
    # name = serializers.CharField()
    # description = serializers.CharField()
    # phone_number=serializers.IntegerField()
    # is_alive=serializers.BooleanField()
    # extra_info=serializers.CharField(read_only=True)#this means that this field is read only and cannot be changed by the user so we don't collect it in the post request and don't use in validation and use only in case of get request where we send dataq
    # created_at = serializers.DateTimeField(read_only=True)#same as above
    # updated_at = serializers.DateTimeField(read_only=True)#same as above

    # #here we are overriding the create method of the serializer class
    # #this methods receives the validated data and creates the object in the database
    # #we can we call the serializer.save() then this method will be used inside the save method.
    # def create(self,validated_data):
    #     return TestModel.objects.create(**validated_data)#**validated_data is used to unpack(in the form of keyword arguments) the validated data and pass it to the create method of the model class
    
    # def update(self,instance,validated_data):
    #     TestModel.objects.filter(id=instance.id).update(**validated_data)#FIRST WE FILTER THE DATA BY ID AND THEN WE UPDATE THE DATA ditionary will be unpacked as keyword arguments
    #     return TestModel.objects.get(id=instance.id)#THEN WE RETURN THE UPDATED DATA

    
