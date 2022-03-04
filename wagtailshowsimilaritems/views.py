from django.apps import apps
from django.views.decorators.http import require_GET
from django.http import JsonResponse
from django.urls import reverse

from wagtail.search.backends import get_search_backend
from wagtail.core.models import Page

backend = get_search_backend()

@require_GET
def search(request):
    search_query = request.GET.get("query")
    model = apps.get_model(request.GET.get("model"))
    field = request.GET.get("field")
    try:
        instance_id = int(request.GET.get("instance_id"))
    except ValueError:
        instance_id = None
    threshold = float(request.GET.get("threshold"))
    max_items = int(request.GET.get("max_items"))

    query = backend.search(
        search_query, model, fields=[field]).annotate_score("_score")

    response = { "items": [], "is_trimmed": False }
    for q in query:
        if q._score > threshold:
            if len(response["items"]) < max_items:
                if q.id != instance_id:
                    if isinstance(q, Page):
                        url = reverse("wagtailadmin_pages:edit", args=(q.page_ptr.id,))
                    else:
                        url = getattr(q, "showsimilaritems_url", lambda: None)()
                    response["items"].append({"value": getattr(q, field), "url": url})
            else:
                response["is_trimmed"] = True
                break
        else:
            break

    return JsonResponse(response)
