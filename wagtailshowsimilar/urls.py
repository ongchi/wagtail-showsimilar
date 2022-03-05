from django.urls import path
try:
    from wagtail.admin.decorators import require_admin_access
except ImportError:
    from wagtail.admin.auth import require_admin_access

from wagtailshowsimilar.views import search

urlpatterns = [
    path(r"search/", require_admin_access(search)),
]
