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

    query = backend.search(search_query, model, fields=[field])
    try:
        q = query.annotate_score("_score")
        # Since django queryset is lazy, this will trigger queryset to
        # be evaluated to make sure whether annotate_score is supported
        # by current search backend.
        _ = q[0]
        query = q
        with_score = True
    except:
        with_score = False

    response = {"items": [], "is_trimmed": False}
    for q in query:
        if (with_score and q._score > threshold) or not with_score:
            if len(response["items"]) < max_items:
                if q.id != instance_id:
                    if hasattr(q, "get_showsimilar_url"):
                        url = getattr(q, "get_showsimilar_url")()
                    elif isinstance(q, Page):
                        url = reverse(
                            "wagtailadmin_pages:edit",
                            args=(q.page_ptr.id,)
                        )
                    else:
                        url = None
                    response["items"].append({
                        "value": getattr(q, field),
                        "url": url,
                    })
            else:
                response["is_trimmed"] = True
                break
        else:
            break

    return JsonResponse(response)
