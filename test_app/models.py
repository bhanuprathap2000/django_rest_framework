from django.db import models

# Create your models here.

#this is a test model
class TestModel(models.Model):
    name = models.CharField(max_length=100,unique=True,blank=True,null=True)#unique true means that the name field must be unique,blank true means that the field can be blank,null true means that the field can take  null values
    description = models.TextField()
    phone_number=models.PositiveIntegerField()
    is_alive=models.BooleanField(default=True)
    extra_info=models.TextField(max_length=255,editable=False,default="null")
    created_at = models.DateTimeField(auto_now_add=True)#auto_now_add means that the field will be automatically populated with the current date and time when the object is first created.
    updated_at = models.DateTimeField(auto_now=True)#auto_now means that the field will be automatically populated with the current date and time every time the object is saved.

    def __str__(self):
        return self.name#this is the string representation of the object
    
    #we are overriding the save method to add extra info to the object
    def save(self,*args,**kwargs):
        self.extra_info=self.name+" "+str(self.phone_number)
        super().save(*args,**kwargs)#this is the save method of the model super() is used to call the save method of the parent class
    
    #inside the Meta class we can specify the database table name and the order in which the fields are displayed in the admin page also we can specify the fields that are not to be displayed in the admin page and also we can specify the fields that are to be displayed in the admin page
    #basically we can specify the meta data of the model
    class Meta:
        ordering = ['created_at']#ordering is used to specify the order in which the objects are displayed in the admin page. (-) means descending order,(+) means ascending order

class ModelX(models.Model):
    test_content=models.ForeignKey(TestModel,on_delete=models.CASCADE,related_name="modelx")#this is a foreign key field on delete means that if the object is deleted then the object referenced by the foreign key field is also deleted(when test model is deleted then the modelx object is also deleted)
    #related_name is used in order to access the fields of modelx in TestModel model(example self.modelx.field_name)
    milage=models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)#auto_now_add means that the field will be automatically populated with the current date and time when the object is first created.
    updated_at = models.DateTimeField(auto_now=True)#auto_now means that the field will be automatically populated with the current date and time every time the object is saved.

    def __str__(self):
        return self.test_content.name#aacesing the name field of the test model object beacause the test model is the foreign key field of the modelx model and a relation exists between the two models.
    
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'ModelX'#this is used to specify the name of the model in the admin page

