# wagtail-showsimilar

Display similar items by field value from wagtail search results.

![Screeen Shot](https://raw.githubusercontent.com/ongchi/wagtail-showsimilar/master/images/screenshot.gif)

## Quick Start

### Installation

```sh
pip install wagtail-showsimilar
```

### Setup

Add `wagtailshowsimilar` to your `settings.py` in the `INSTALLED_APPS` section:

```python
INSTALLED_APPS = [
    ...
    'wagtailshowsimilar',
]
```

### Add admin urls

```python
from wagtailshowsimilar.urls import urlpatterns as showsimilar_admin_urls

urlpatterns = [
    ...
    path('admin/showsimilar/', include(showsimilar_admin_urls)),
    path('admin/', include(wagtailadmin_urls)),
    ...
]
```

### ```ShowSimilarPanel```

The model should be searchable to work with wagtail-showsimilar, All pages, images and documents are searchable by default in Wagtail. 

#### Options
  - **score_threshold** (```int/float```) - Only score for matched results above this value will be listing. This field only works with Elasticsearch backend. (**default**: 20)
  - **max_items** (```int```) - Maximum number of listing items shown from search results. (**default**: 10)

```python
from django.db import models

from wagtail.search import index
from wagtailshowsimilar.edit_handlers import ShowSimilarPanel

class BreadType(index.Indexed, models.Model):
    title = models.CharField(max_length=255)

    panels = [
        ShowSimilarPanel('title', score_threshold=5),
    ]

    search_fields = [index.SearchField('title', partial_match=True)]
```

You'll need to inherit from ```index.Indexed``` for custom models and add some ```search_fields``` to the model. For more information, please see [Indexing custom models](https://docs.wagtail.org/en/stable/topics/search/indexing.html#indexing-custom-models).

### (Optional) Implement ```get_showsimilar_url```

The result list items create links to the edit view for Page models by default.
It's also possiable to implement get_showsimilar_url to customize link URL for ```Page```, ```Image```, ```Document``` or custom models.

```python
from django.urls import reverse

class BreadType(index.Indexed, models.Model):
    ...

    def get_showimilar_url(self):
        return reverse("breads_breadtype_modeladmin_edit", args=(self.id,))
```
