from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse


def upload_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

class Post(models.Model):

    title = models.CharField(max_length=120)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_location,
    null=True,
    blank=True,
    width_field='width_field',
    height_field='height_field')

    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


    def __unicode__(self):
        return self.title


    def get_absolute_url(self):
        #return '/posts/%s' %(self.id)
        return reverse('posts:detail', kwargs={'pk': self.id} )

    class Meta:
        ordering = ['-timestamp', '-updated']
