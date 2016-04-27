from django.views.generic import TemplateView

from apps.utils.led import blink


class ColorView(TemplateView):
    template_name = 'art_app/index.jade'

    def get(self, request, *args, **kwargs):
        blink(17)
        return super(ColorView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ColorView, self).get_context_data(**kwargs)
        context['color'] = kwargs.get('color')
        return context
