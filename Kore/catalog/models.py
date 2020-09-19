from django.db import models

# Create your models here.

class Users(models.Model):
    """Creates a model with the name, kerberos, and year of graduation of user"""
    # Fields
    name = models.CharField(max_length=80, verbose_name='Your Name', help_text='Your Name')
    kerb = models.CharField(max_length = 8, verbose_name='Kerberos', primary_key = True, help_text='Your Kerberos ID')
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    SUPERSENIOR = 'SS'
    ALUM = 'AL'
    grad_year_choices = [(FRESHMAN, 'Freshman'), (SOPHOMORE, 'Sophomore'), (JUNIOR, 'Junior'), (SENIOR, 'Senior'), (SUPERSENIOR, 'Super Senior'), (ALUM, 'Alumni')]
    grad_year = models.CharField(max_length=2, choices=grad_year_choices, default=FRESHMAN,)


class Psolved(models.Model):   
    'Creates a model with the class, assignment number, and question number that user has solved'
    class_name = models.CharField(max_length=20, verbose_name='Class No. (e.g. 6.006)', help_text='Enter the class no. as per catalog.mit.edu')
    assign_name = models.IntegerField(verbose_name='Pset No. (e.g. 1)', help_text='Enter the problem set number')
    question_number = models.IntegerField(verbose_name='Question No. (e.g. 1)', help_text='Enter the question which you have solved')
    students = models.ManyToManyField('Users')

class Punsolved(models.Model):   
    'Creates a model with the class, assignment number, question number, and part number that user has not solved'
    class_name_u = models.CharField(max_length=20, verbose_name='Class No. (e.g. 6.006)', help_text='Enter the class no. as per catalog.mit.edu')
    assign_name_u = models.IntegerField(verbose_name='Pset No. (e.g. 1)', help_text='Enter the problem set number')
    question_number_u = models.IntegerField(verbose_name='Question No. (e.g. 1)', help_text='Enter the question which you have not solved')
    students_u = models.ManyToManyField('Users')