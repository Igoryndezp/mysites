from django.views.generic.base import TemplateView


class AboutAuthorView(TemplateView):
    template_name = 'app_name/about_author.html'


class AboutTechView(TemplateView):
    template_name = 'app_name/about_tech.html'
