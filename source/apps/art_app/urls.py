from django.conf.urls import url, patterns
from apps.art_app.views import ColorView

urlpatterns = [
    url(r'(?P<color>[a-z]+)/$', ColorView.as_view())
]
