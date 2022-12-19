from .models import Project
from django.views import generic
from django.utils import timezone

class ProjectsView(generic.ListView):
    template_name = 'projects/base_project.html'
    context_object_name = 'latest_project_list'

    def get_queryset(self):
        """Return the last five published projects,
        not including those set to be published 
        in the future."""
        return Project.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')
