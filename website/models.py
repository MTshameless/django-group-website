from django.db import models
from django.db.models.fields.related import ManyToManyField

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.name
    
    
class ResearchArea(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='research_area')
    class Meta:
        verbose_name_plural = "research areas"
    def __str__(self):
        return self.name
    

class RepresentativePublications(models.Model):
    name = models.CharField(max_length=200)
    authors = models.TextField()
    doi = models.CharField(max_length=100)
    journal = models.CharField(max_length=100)
    publish_year = models.CharField(max_length=100)
    publish_issue = models.CharField(max_length=100)
    publish_page = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "representative publications"
    def __str__(self):
        return self.name
    

class ResearchDetails(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='research_details')
    publications = ManyToManyField(RepresentativePublications)
    class Meta:
        verbose_name_plural = "research details"
    def __str__(self):
        return self.name
    

class Publications(models.Model):
    name = models.CharField(max_length=200)
    authors = models.TextField()
    doi = models.CharField(max_length=100)
    journal = models.CharField(max_length=100)
    publish_year = models.CharField(max_length=100)
    publish_issue = models.CharField(max_length=100)
    publish_page = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = "publications"
    def __str__(self):
        return self.name
    

class Members(models.Model):
    name = models.CharField(max_length=100)
    homeland = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    image = models.ImageField(upload_to='members')
    class Meta:
        verbose_name_plural = "members"
    def __str__(self):
        return self.name
    

class Positions(models.Model):
    name = models.CharField(max_length=100)
    member = ManyToManyField(Members)
    class Meta:
        verbose_name_plural = "positions"
    def __str__(self):
        return self.name
    
class Instruments(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='instruments')
    class Meta:
        verbose_name_plural = "instruments"
    def __str__(self):
        return self.name
    
class News(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    short_description = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title