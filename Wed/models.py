from django.db import models

# Create your models here.
class Intro(models.Model):
    brides_name = models.CharField(max_length=30)
    grooms_name = models.CharField(max_length=30)
    date = models.DateField()
    ceremony = models.CharField(max_length=50, null=True, blank=True)
    event = models.CharField(max_length=50)
    back_img = models.ImageField(upload_to='', null=True, blank=True)

    def __str__(self) -> str:
        return self.grooms_name + ' and ' +  self.brides_name

class Story(models.Model):
    grooms_name = models.CharField(max_length=30)
    grooms_image = models.ImageField(upload_to='Story')
    grooms_story = models.TextField(blank=True, null=True)
    brides_name = models.CharField(max_length=30)
    brides_image = models.ImageField(upload_to='')
    brides_story = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.grooms_name + ' and ' + self.brides_name
    
class Main_Story(models.Model):
    fast_meet = models.CharField(max_length=150, blank=True, null=True)
    he_proposed = models.CharField(max_length=150, blank=True, null=True)
    love_story = models.CharField(max_length=150, blank=True, null=True)

class Gallery(models.Model):
    image = models.ImageField(upload_to='')

class Prog_Detail(models.Model):
    prog_name = models.CharField(max_length=30)
    time = models.TimeField()
    discription = models.TextField(blank=True, null=True)
    bg_img = models.ImageField(upload_to='')

    def __str__(self) -> str:
        return self.prog_name
    
class Blog(models.Model):
    title = models.CharField(max_length=30)
    date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='blog')
    discription = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class Single_blog(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='')
    discription = models.TextField()

    def __str__(self) -> str:
        return self.title
    
class Accommodation(models.Model):
    title = models.CharField(max_length=50, blank=True, null=True)
    discription = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='accommodation')

    def __str__(self) -> str:
        return self.title

