from django.views.generic.base import TemplateView



class HomePageView(TemplateView):
    template_name = "website/index.html"
