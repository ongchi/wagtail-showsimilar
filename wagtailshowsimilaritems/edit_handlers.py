from wagtail.admin.edit_handlers import FieldPanel

from .widgets import ShowSimilarItems

class ShowSimilarItemsPanel(FieldPanel):
    def __init__(self, *args, **kwargs):
        self.threshold = kwargs.pop("score_threshold", 20)
        self.max_items = kwargs.pop("max_items", 10)

        super().__init__(*args, **kwargs)

    def on_instance_bound(self):
        self.widget = ShowSimilarItems(
            instance=self.instance,
            threshold=self.threshold,
            max_items=self.max_items
        )
