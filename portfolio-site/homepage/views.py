from homepage.models import HomePage
from django.views import generic

class HomePageView(generic.ListView):
    template_name = "homepage/base_home.html"
    context_object_name = 'latest_homepage'

    def get_queryset(self):
        """Return the most recent HomePage Object"""
        return HomePage.objects.all()
