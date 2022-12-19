from django.contrib import admin
from .models import Project

class ProjectAdmin(admin.ModelAdmin):
    search_fields = ['project_name']
    list_filter = ['pub_date']
    list_display = ('project_name', 'pub_date')
    fieldsets = [
        (None, {'fields': ['project_name']}),
        ('Project details', {'fields': ['project_details']}),
        ('Project screenshot', {'fields': ['project_screenshot']}),
        ('GitHub link', {'fields': ['github_link']}),
        ('GitLab link', {'fields': ['gitlab_link']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Project, ProjectAdmin)
