from django.db import models
from django.contrib import admin

class Project(models.Model):
    slug = models.SlugField(null=True, blank=True)
    project_name = models.CharField(max_length=100, null=True)
    project_screenshot = models.ImageField(blank=True, upload_to='project_images')
    project_details = models.TextField(max_length=500)
    github_link = models.URLField(null=True)
    gitlab_link = models.URLField(null=True)
    pub_date = models.DateTimeField('date published')

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )

    def __str__(self):
        return self.project_name
