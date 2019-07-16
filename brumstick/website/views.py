from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Projects

def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def projects(request):
    project_posts = {
        'projects': Projects.objects.all()
    }
    return render(request, 'website/projects.html', project_posts)

class ProjectListView(ListView):
    model = Projects
    template_name = 'website/projects.html'
    context_object_name = 'projects'    # define to match project object name above

class ProjectDetailView(DetailView): 
    model = Projects
    template_name = 'website/project-details.html'