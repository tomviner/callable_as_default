# ./sample_project/manage.py shell
# ipython: run show_bug.py
# plain shell: execfile('show_bug.py')

from django.forms.models import modelform_factory

from cad.models import Article

article_modelform = modelform_factory(Article, fields=('title',))

print 'instantiate form'
form = article_modelform()

print 'render form as HTML'
form.as_p()
