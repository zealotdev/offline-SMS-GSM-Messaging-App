from django.contrib import admin
from django.db import models
from django import forms

from contacts.models import Category, Contact


class InineContact(admin.TabularInline):
    model = Contact
    extra = 1
    can_delete = True


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_on',)

    fieldsets = (
        ('Basic Info', {
            "fields": (
                'name',
                'created_on'
            ),
        }),
    )

    inlines = [InineContact]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Contact)
