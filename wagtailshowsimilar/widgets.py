from django import forms
from django.forms.widgets import TextInput
from django.utils.translation import gettext_lazy as _

from wagtail.utils.widgets import WidgetWithScript

class ShowSimilarWidget(WidgetWithScript, TextInput):
    template_name = "wagtailshowsimilar/showsimilar.html"

    def __init__(self, instance, threshold, max_items):
        self.instance = instance
        self.threshold = threshold 
        self.max_items = max_items

        super().__init__()

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)

        if context["widget"]["value"] is None:
           context["widget"]["value"] = "" 

        meta = self.instance._meta
        context["label"] = _("Similar items:")
        context["target_model"] = f"{meta.app_label}.{meta.model_name}"
        context["instance_id"] = self.instance.id
        context["threshold"] = self.threshold
        context["max_items"] = self.max_items

        return context

    @property
    def media(self):
        return forms.Media(
            js=["wagtailshowsimilar/showsimilar.js"],
        )
