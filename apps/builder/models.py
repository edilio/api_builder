from __future__ import unicode_literals

from django.conf import settings
from django.db import models

from .constants import PERMISSION_OPTIONS, AUTH_CLASS_OPTIONS, PAGINATION_CLASS, DB_OPTIONS, FIELD_TYPE_OPTIONS


class Authentication(models.Model):
    class_name = models.PositiveSmallIntegerField(choices=AUTH_CLASS_OPTIONS)

    def __unicode__(self):
        return self.get_class_name_display()


class Permission(models.Model):
    class_name = models.PositiveSmallIntegerField(choices=PERMISSION_OPTIONS)

    def __unicode__(self):
        return self.get_class_name_display()


class Project(models.Model):
    name = models.CharField(max_length=20)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    default_permissions_class = models.ManyToManyField(Permission, related_name="projects")
    default_authentication_class = models.ManyToManyField(Authentication)
    default_pagination_class = models.PositiveSmallIntegerField(choices=PAGINATION_CLASS)
    page_size = models.PositiveSmallIntegerField(default=25)
    db_engine = models.PositiveSmallIntegerField(choices=DB_OPTIONS)

    def __unicode__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=20)
    project = models.ForeignKey(Project, related_name="applications")

    def __unicode__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=20)
    application = models.ForeignKey(Application, related_name="models")

    def __unicode__(self):
        return self.name


class FieldType(models.Model):
    name = models.CharField(max_length=25)
    type = models.PositiveSmallIntegerField(choices=FIELD_TYPE_OPTIONS)

    def __unicode__(self):
        return self.name


class FieldTypeParameter(models.Model):
    field_type = models.ForeignKey(FieldType, related_name='parameters')
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name


class Field(models.Model):
    name = models.CharField(max_length=20)
    model = models.ForeignKey(Model, related_name="fields")
    field_type = models.ForeignKey(FieldType)

    def __unicode__(self):
        return self.name


class FieldParam(models.Model):
    name = models.CharField(max_length=20)
    field = models.ForeignKey(Field)
    value = models.CharField(max_length=300, null=True, blank=True)

    def __unicode__(self):
        return self.name
