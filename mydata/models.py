from django.db import models

# Create your models here.

class Add_Collage(models.Model):
    collage_name = models.CharField(max_length=100,unique=True)  
    def __str__(self):
        return f"Collge name :{self.collage_name}"
    
 


class Add_Collage_Branch(models.Model):     
    collage_name = models.ForeignKey(Add_Collage, on_delete=models.CASCADE,to_field='collage_name')
    branch_name= models.CharField(max_length=100,unique=True)

    def __str__(self):
        return f"Collage name :{self.collage_name} , Collage Branch: {self.branch_name}"
    



# want to save another field of a model as a foreign key in Django, 
# you can use the ForeignKey field along with the to_field attribute. 
class Add_Student(models.Model):  
    collage_name = models.ForeignKey(Add_Collage, on_delete=models.CASCADE,to_field='collage_name')
    branch_name = models.ForeignKey(Add_Collage_Branch, on_delete=models.CASCADE,to_field='branch_name')
    student_name= models.CharField(max_length=200,)
    student_age=models.IntegerField()

    # def __str__(self):
    #     return f"Collage Name: {self.collage_name}, Collage Branch: {self.branch_name}, Student Name {self.student_name}, Student age {self.student_age}"
