from django.shortcuts import render

# Create your views here.
from catalog.models import student, solvedProblem, unsolvedProblem

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_students = student.objects.all().count()
    
    context = {
        'num_students': num_students,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
