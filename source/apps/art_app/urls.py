from django.conf.urls import url, patterns
from apps.art_app.views import ColorView

urlpatterns = [
    url(r'$', ColorView.as_view())
]
