from django.db import models

# Create your models here.

#this is a test model
class TestModel(models.Model):
    name = models.CharField(max_length=100,unique=True,blank=True,null=True)#unique true means that the name field must be unique,blank true means that the field can be blank,null true means that the field can take  null values
    description = models.TextField()
    phone_number=models.PositiveIntegerField()
    is_alive=models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)#auto_now_add means that the field will be automatically populated with the current date and time when the object is first created.
    updated_at = models.DateTimeField(auto_now=True)#auto_now means that the field will be automatically populated with the current date and time every time the object is saved.

    def __str__(self):
        return self.name#this is the string representation of the object
    
    #inside the Meta class we can specify the database table name and the order in which the fields are displayed in the admin page also we can specify the fields that are not to be displayed in the admin page and also we can specify the fields that are to be displayed in the admin page
    #basically we can specify the meta data of the model
    class Meta:
        ordering = ['created_at']#ordering is used to specify the order in which the objects are displayed in the admin page. (-) means descending order,(+) means ascending order

