from django.views.generic import TemplateView


class BootstrapPageView(TemplateView):
    template_name = "base_bootsrap.html"
