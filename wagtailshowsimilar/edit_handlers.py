from wagtail.admin.edit_handlers import FieldPanel

from .widgets import ShowSimilarWidget

class ShowSimilarPanel(FieldPanel):
    def __init__(self, *args, **kwargs):
        self.threshold = kwargs.pop("score_threshold", 20)
        self.max_items = kwargs.pop("max_items", 10)

        super().__init__(*args, **kwargs)

        self.widget = ShowSimilarWidget(
            instance=None,
            threshold=self.threshold,
            max_items=self.max_items
        )

    def on_instance_bound(self):
        self.widget.instance = self.instance

    def clone(self):
        return self.__class__(
            field_name=self.field_name,
            classname=self.classname,
            score_threshold=self.threshold,
            max_items=self.max_items
        )
