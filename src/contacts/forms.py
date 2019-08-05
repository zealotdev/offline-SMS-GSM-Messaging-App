from django import forms
from django.forms import modelformset_factory

from contacts.models import Category



CategoryFormSet=modelformset_factory(Category, fields=('name',), can_delete=True)
