from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = "app_main/index.html"
