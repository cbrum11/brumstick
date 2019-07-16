from django.db import models
from django.contrib.auth.models import User

class Projects(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    abstract = models.TextField(blank=True)
    main_image = models.ImageField(blank=True)
    show_in_list = models.BooleanField(default=False)
    has_jupyter = models.BooleanField(default=False)
    disp_order = models.IntegerField(default=1000000, blank=True)
    part1_link = models.CharField(max_length=50, blank=True)
    part1_title = models.CharField(max_length=50, blank=True)
    part2_link = models.CharField(max_length=50, blank=True)
    part2_title = models.CharField(max_length=50, blank=True)
    part3_link = models.CharField(max_length=50, blank=True)
    part3_title = models.CharField(max_length=50, blank=True)
    part4_link = models.CharField(max_length=50, blank=True)
    part4_title = models.CharField(max_length=50, blank=True)
    part5_link = models.CharField(max_length=50, blank=True)
    part5_title = models.CharField(max_length=50, blank=True)
    part6_link = models.CharField(max_length=50, blank=True)
    part6_title = models.CharField(max_length=50, blank=True)
    part7_link = models.CharField(max_length=50, blank=True)
    part7_title = models.CharField(max_length=50, blank=True)
    part8_link = models.CharField(max_length=50, blank=True)
    part8_title = models.CharField(max_length=50, blank=True)
    part9_link = models.CharField(max_length=50, blank=True)
    part9_title = models.CharField(max_length=50, blank=True)
    part10_link = models.CharField(max_length=50, blank=True)
    part10_title = models.CharField(max_length=50, blank=True)


    class Meta:
        verbose_name_plural = "Projects" # Fix admin panel doulbe 's'
        ordering = ['disp_order']

    def __str__(self):
        return self.title

