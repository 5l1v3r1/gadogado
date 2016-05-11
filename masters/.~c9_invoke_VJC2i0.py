from __future__ import unicode_literals

from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.utils.html import format_html


class Kid(models.Model):
    GENDER = (
        ('B', 'Boy'),
        ('G', 'Girl'),
    )
    
    #adult_id = models.ForeignKey(Adult1, on_delete=models.CASCADE)
    first_name = models.CharField("First name", max_length=30)
    last_name = models.CharField("Last name", max_length=30)
    gender = models.CharField("Gender", max_length=1, choices=GENDER)
    mobile_no = models.CharField("Mobile no.", max_length=15)
    email = models.CharField("Email address", max_length=30,blank=True)
    date_joined = models.DateField()
    date_left = models.DateField(blank=True, null=True)
    
    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "kid"
        
    def __str__(self):
        return self.first_name  
        

        
class Adult(models.Model):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER)
    members = models.ManyToManyField(Kid, through='Membership')
    mobile_no = models.CharField(max_length=15)
    email = models.CharField("Email address", max_length=30,blank=True)
    date_joined = models.DateField(default = timezone.now)
    date_left = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    city = models.CharField(max_length=20)
    postcode = models.CharField("Post Code",max_length=5)
    state = models.CharField(max_length=30)
    country = CountryField()
    line1 = models.CharField(max_length=30,default="-")
    line2 = models.CharField(max_length=30,default="-")
    line3 = models.CharField(max_length=30,default="-")

    def colored_first_name(self):
        return format_html('<span style="color: #{};">{}</span>',self.first_name, self.last_name)
        
                           
                           
    class Meta:
        ordering = ["first_name"]
        verbose_name_plural = "adult"
        
    def __str__(self):
        return self.first_name


class Membership(models.Model):
    adult = models.ForeignKey(Adult, on_delete=models.CASCADE)
    kid = models.ForeignKey(Kid, on_delete=models.CASCADE)
    relationship = models.BooleanField("Children", default=True) 
    
    
class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()
        
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
return self.title    
    def __unicode__(self):
        return self.name
        
        
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    e-mail = models.E-mailField()
    
    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    num_pages = models.IntegerField(blank=True, null=True)
    objects = BookManager()
    
    def __unicode__(self):
        return self.title