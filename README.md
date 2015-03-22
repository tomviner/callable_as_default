# callable_as_default
Sample Django project to show Django bug https://code.djangoproject.com/ticket/11390

> If you use a callable as default value on a model field, it gets called 3 times.

Sample code to reproduce this:

```
def get_title(call_count=[0]):
    call_count[0] += 1
    n = call_count[0]
    msg = 'get_title call #{}'.format(n)
    print msg
    return msg

class Article(models.Model):
    title = models.CharField(max_length=50, default=get_title)
```
This repo contains a Django project containing that model.

To show 2 seperate calls to get the default field value, run/execfile `show_bug.py` from a `./manage shell`:

```
In [1]: from django.forms.models import modelform_factory

In [2]: from cad.models import Article

In [3]: article_modelform = modelform_factory(Article, fields=('title',))

In [4]: form = article_modelform()
get_title call #1

In [5]: form.as_p()
get_title call #2
Out[5]: u'<p><label for="id_title">Title:</label> <input id="id_title" maxlength="50" name="title" type="text" value="get_title call #2" /><input id="initial-id_title" name="initial-title" type="hidden" value="get_title call #2" /></p>'
```

#### call 1 & 2:

django/contrib/admin/options.py:ModelAdmin.changeform_view

one call for each of these 2 lines

    form = ModelForm(initial=initial)
    formsets, inline_instances = self._create_formsets(request, self.model(), change=False)


#### call 3:

django/forms/forms.py:BoundField

    BoundField.__str__
    BoundField.as_widget
    BoundField.value



