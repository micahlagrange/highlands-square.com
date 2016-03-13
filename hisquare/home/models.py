import os
from django.db import models
from django.utils import timezone
import datetime
from django.template.defaultfilters import slugify


# Create your models here.
class AboutPage(models.Model):
	text = models.TextField(null=True, blank=False)
	date_updated = models.DateTimeField(null=True, blank=False)

	def save(self, *args, **kwargs):
		self.date_updated = timezone.now()
		super(AboutPage, self).save(*args, **kwargs)

	def __str__(self):
		return '{}'.format(self.text[0:50])


class AboutPromotion(models.Model):
	quote = models.TextField(null=True, blank=False)
	promoter = models.CharField(max_length=200, null=True, blank=False)
	date_quoted = models.DateTimeField(null=True, blank=False)
	aboutpage = models.ForeignKey(AboutPage, null=True, blank=False)


class ShopCategory(models.Model):
	name = models.CharField(max_length=200, null=True, blank=False, unique=True)
	slug = models.SlugField(null=True)
	
	def save(self, *args, **kwargs):
	  self.slug = slugify(self.name)
	  super(ShopCategory, self).save(*args, **kwargs)

	def __str__(self):
		return '{}'.format(self.name)

	class Meta:
		verbose_name = 'Merchant Category'


class Business(models.Model):
	name = models.CharField(max_length=200, null=True, blank=False)
	tagline = models.CharField(max_length=75, null=True, blank=True)
	description = models.TextField(max_length=800, null=True, blank=True)
	logo = models.ImageField(upload_to='businesses/logos', null=True, blank=True)
	website = models.URLField(null=True, blank=True)
	category = models.ForeignKey(ShopCategory, null=True, blank=False, on_delete=models.SET_NULL)

	street = models.CharField(max_length=200, null=True, blank=False)
	city = models.CharField(max_length=200, null=True, blank=False)
	state = models.CharField(max_length=200, null=True, blank=False)
	zip = models.IntegerField(null=True, blank=False)

	email = models.EmailField(null=True, blank=True)
	phone = models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return '{} - {}'.format(self.category, self.name)
		
	class Meta:
		ordering = ['category','name']
		verbose_name = 'Merchant'


class CategoryImage(models.Model):
	category = models.ForeignKey(ShopCategory, null=True, blank=False)
	image = models.ImageField(upload_to='categories/images', null=True, blank=False)

	def __str__(self):
		return '"{}" carousel image | {}'.format(self.category.name, os.path.basename(self.image.name))
		
	class Meta:
		ordering = ['category']
		verbose_name = 'Carousel Category Image'


class Event(models.Model):
	title = models.CharField(max_length=200, null=True, blank=False)
	starttime = models.TimeField(null=True, blank=True, default=datetime.time.min)
	endtime = models.TimeField(null=True, blank=True,  default=datetime.time.max)
	date = models.DateField(null=False, blank=False, default=timezone.now)
	description = models.TextField(null=True, blank=False)
	eventimage = models.ImageField(upload_to='events/images', null=True, blank=True)
	
	def __str__(self):
		return "{}".format(self.title)
