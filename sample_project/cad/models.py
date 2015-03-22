from django.db import models

def get_title(call_count=[0]):
    call_count[0] += 1
    n = call_count[0]
    msg = 'get_title call #{}'.format(n)
    print msg
    return msg

class Article(models.Model):
    title = models.CharField(max_length=50, default=get_title)
