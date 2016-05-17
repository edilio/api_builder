from django.contrib import admin

from . import models


@admin.register(models.Authentication)
class AuthenticationAdmin(admin.ModelAdmin):
    list_display = ('class_name', )


@admin.register(models.Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('class_name', )


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'default_pagination_class', 'page_size', 'db_engine')
    list_filter = ('default_pagination_class', 'db_engine')


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'project')


@admin.register(models.Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'application')
    list_filter = ('application', )


class FieldParamInline(admin.TabularInline):
    model = models.FieldParam


@admin.register(models.Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'field_type')
    list_filter = ('model', )

    inlines = [FieldParamInline, ]
