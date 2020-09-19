from django.db import models

# Create your models here.

class User(models.Model):
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
    def __str__(self):
        """String for representing the Model object."""
        return self.name
    def get_absolute_url(self):
        """Returns the url to access a detail record for this user."""
        return reverse('user-detail', args=[str(self.id)])



class Psolved(models.Model):   
    'Creates a model with the class, assignment number, and question number that user has solved'
    class_name = models.CharField(max_length=20, verbose_name='Class No. (e.g. 6.006)', help_text='Enter the class no. as per catalog.mit.edu')
    assign_name = models.IntegerField(verbose_name='Pset No. (e.g. 1)', help_text='Enter the problem set number')
    question_number = models.IntegerField(verbose_name='Question No. (e.g. 1)', help_text='Enter the question which you have solved')
    students = models.ManyToManyField('User')
    def __str__(self):
        """String for representing the Model object."""
        return self.class_name + str(self.assign_name) + str(self.question_number)
    def get_absolute_url(self):
        """Returns the url to access a detail record for this psolved."""
        return reverse('psolved-detail', args=[str(self.id)])

class Punsolved(models.Model):   
    'Creates a model with the class, assignment number, question number, and part number that user has not solved'
    class_name = models.CharField(max_length=20, verbose_name='Class No. (e.g. 6.006)', help_text='Enter the class no. as per catalog.mit.edu')
    assign_name = models.IntegerField(verbose_name='Pset No. (e.g. 1)', help_text='Enter the problem set number')
    question_number = models.IntegerField(verbose_name='Question No. (e.g. 1)', help_text='Enter the question which you have not solved')
    students = models.ManyToManyField('User')
    def __str__(self):
        """String for representing the Model object."""
        return self.class_name + str(self.assign_name) + str(self.question_number)
    def get_absolute_url(self):
        """Returns the url to access a detail record for this punsolved."""
        return reverse('user-detail', args=[str(self.id)])