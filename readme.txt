Project Setup

Create virtual env with pip 
1. Create virtual env | $python3 -m venv brumstick-django-venv 
2. Activate virtual env | source brumstickvenv/bin/activate

To exit venv...
1. $deactivate

Install Django 
1. $pip install django

Create Django Project
1. $django-admin startproject brumstick

Start Server
1. $python manage.py runserver

Create Django Application
1. $python manage.py startapp app_name

Install Django Application
1. In brumstick/settings.py --> Add the new application into INSTALLED_APPS list.

Create a View 
1. Add the following to the hello_world views.py

    def hello_world(request):
        return render(request, 'hello_world.html', {})

Misc.
$django-admin : lists available subcommands

# Understanding url navigation.
When someone visits the URL, django first checks the projects manin urls.py file for a 
matching path in the urlpatterns list.  We'll use mainsite/blog/about as an example. 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
]

It if finds a matching path, it moves to that route.  In this case, the urls.py file 
in the blog application.  Within this new urls.py file, it checks for the remainder
of the path (looking for 'about' in this example.)

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]

It finds the 'about' path then servves up the about function from the views.py file
of the blog application.

1. Detects changes and prepares django to apply database migrations
$python manage.py makemigrations
2. Apply migrations
$python manage.py migrate
3. Create superuser
$python manage.py createsuperuser

Using Typora to create blog posts in markdown.  Edited typora css with the following URLS:
https://codemirror.net/theme/
https://support.typora.io/Add-Custom-CSS/
https://support.typora.io/Code-Block-Styles/
Chose oceanic-next

