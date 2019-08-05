from django.db import models
from django.core.validators import RegexValidator


class Category(models.Model):
    name = models.CharField('Category name', max_length=40, unique=True)
    created_on = models.DateTimeField('Created on', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['-created_on']


class Contact(models.Model):
    name = models.CharField('Contact name', max_length=40)
    phone = models.BigIntegerField('Phone number', validators=[
                                   RegexValidator(r'^\d{9,10}$')])
    category = models.ForeignKey(
        Category, verbose_name='Belongs to Category', on_delete=models.CASCADE)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-date_registered']


class MessageHistory(models.Model):
    text = models.TextField()
    category = models.CharField(max_length=100)
    recipients = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.text[:100]
