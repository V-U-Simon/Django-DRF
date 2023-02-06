from django.views.generic import TemplateView


class TailWindPageView(TemplateView):
    template_name = "base_windtail.html"
