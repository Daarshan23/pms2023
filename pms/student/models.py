from django.db import models

# Create your models here.
class Coures(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fees = models.IntegerField()

    def __str__(self):
            return self.name
            
    class Meta:
        db_table = 'coures'
        
        
        
class Student(models.Model):
    coures = models.ForeignKey(Coures,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'student'
        
        
genderChoice = (("Male","male"),("Female","Female"))

    
class Faculty(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        password = models.CharField(max_length=100)
        gender = models.CharField(choices=genderChoice,max_length=10)
        created_at = models.DateField(auto_now_add=True)
        updated_at = models.DateField(auto_now=True)
        
        
        class Meta:
            db_table = 'faculty'
            
        def __str__(self):
            return self.name
        
class Subjects(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
        
    
    
    class Meta:
        db_table ='subjects'
        
        def __str__(self):
            return self.name
        
class Batch(models.Model):
    name = models.CharField(max_length=100)
    Faculty = models.ForeignKey(Faculty,on_delete=models.CASCADE) 
    subjects = models.ForeignKey(Subjects,on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
        
    
    class Meta:
        db_table ='batch'
        
        def __str__(self):
            return self.name



        
        
        