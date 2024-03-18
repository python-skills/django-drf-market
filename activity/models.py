from django.db import models
from directory.models import Directory
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class Comment(models.Model):
    caption = models.TextField(verbose_name=_('caption'))
    user = models.ForeignKey(User, related_name='comments',
                             on_delete=models.CASCADE, verbose_name=_('user'))
    directory = models.ForeignKey(Directory, related_name='comments',
                                  on_delete=models.CASCADE, verbose_name=_('directory'))
    reply_to = models.ForeignKey('self', related_name='replies',
                                 on_delete=models.CASCADE,
                                 blank=True,
                                 null=True,
                                 verbose_name=_('reply_to')
                                 )

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.caption
