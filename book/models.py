from django.db import models

class SubjectModel(models.Model):
	name = models.CharField(max_length=512,blank=False)

	def __str__(self):
		return self.name


# Create your models here.
class BookModel(models.Model):
	isbn = models.CharField(max_length=13,primary_key=True,unique=True)
	prices=models.FloatField()
	title = models.CharField(max_length=255,blank=True)
	authors = models.CharField(max_length=2000,blank=True)
	publisher = models.CharField(max_length=500,blank=True)
	year = models.IntegerField(blank=True)
	desc = models.TextField(null=True,blank=True)
	thumbnail_small = models.ImageField(blank=True,null=True,default='None')
	thumbnail = models.ImageField(blank=True,default='https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/2000px-No_image_available.svg.png')
	quantity = models.PositiveIntegerField(default='1')
	subject = models.ForeignKey("SubjectModel",on_delete="CASCADE",)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('book:book_details', args=[str(self.isbn)])

class Book(models.Model):
	name = models.CharField(max_length=100)

class BookOrderSearch(models.Model):
	title = models.CharField(max_length=880,blank=True)
	author = models.CharField(max_length=512,blank=True)
	keyword = models.CharField(max_length=512,blank=True)
	isbn = models.PositiveIntegerField(blank=True)

class VisionBooksModel(models.Model):
	Title = models.CharField(max_length=999)
	Author= models.CharField(max_length=999)
	Quantity = models.CharField(max_length=999)
	Price = models.CharField(max_length=999)
	Location = models.CharField(max_length=999)
	Isbn = models.CharField(max_length=999)
	EditionYear = models.CharField(max_length=999)
	Publisher = models.CharField(max_length=999)
	Edition = models.CharField(max_length=999)
	Cover = models.CharField(max_length=999)
	Subject = models.CharField(max_length=999)
	Pages = models.CharField(max_length=999)
	Language = models.CharField(max_length=999)
	Display = models.CharField(max_length=999)

	def __str__(self):
		return self.Title