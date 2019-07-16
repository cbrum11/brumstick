from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    abstract = models.TextField(blank=True)
    main_image = models.ImageField(blank=True)
    show_in_list = models.BooleanField(default=False)
    has_jupyter = models.BooleanField(default=False)
    disp_order = models.IntegerField(default=1000000, blank=True)

    class Meta:
        ordering = ['disp_order']

    def __str__(self):
        return self.title

