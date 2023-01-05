from django.utils.translation import gettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel


class ShowSimilarPanel(FieldPanel):
    def __init__(self, field_name, score_threshold=20, max_items=10, **kwargs):
        self.threshold = score_threshold
        self.max_items = max_items
        super().__init__(field_name, **kwargs)

    def clone_kwargs(self):
        kwargs = super().clone_kwargs()
        kwargs.update({
            "score_threshold": self.threshold,
            "max_items": self.max_items,
        })

        return kwargs

    def get_bound_panel(self, instance=None, request=None, form=None, prefix="panel"):
        bound_panel = super().get_bound_panel(instance, request, form, prefix)
        bound_panel.threshold = self.threshold
        bound_panel.max_items = self.max_items

        return bound_panel

    class BoundPanel(FieldPanel.BoundPanel):
        template_name = "wagtailshowsimilar/field_panel.html"

        def get_context_data(self, parent_context=None):
            context = super().get_context_data(parent_context)

            meta = getattr(self.instance, "_meta")
            context.update({
                "label": _("Similar items:"),
                "target_model": f"{meta.app_label}.{meta.model_name}",
                "instance_id": self.instance.id if self.instance else None,
                "threshold": self.threshold,
                "max_items": self.max_items,
            })

            return context

        class Media:
            js = ("wagtailshowsimilar/showsimilar.js", )
