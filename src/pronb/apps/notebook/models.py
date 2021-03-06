# vim: set fileencoding=utf8:
"""
short module explanation

AUTHOR:
    lambdalisue[Ali su ae] (lambdalisue@hashnote.net)
    
Copyright:
    Copyright 2011 Alisue allright reserved.

License:
    Licensed under the Apache License, Version 2.0 (the "License"); 
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unliss required by applicable law or agreed to in writing, software
    distributed under the License is distrubuted on an "AS IS" BASICS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""
__AUTHOR__ = "lambdalisue (lambdalisue@hashnote.net)"
__VERSION__ = "0.1.0"
from django.db import models
from django.db.models import Q
from django.contrib.auth.models import User
from django.utils.text import ugettext_lazy as _

import lettuce
import types

class NotebookManager(models.Manager):
    """Manager class of Notebook model"""
    def published(self, request):
        """
        return published queryset

        return queryset of ``types='public'`` notebooks for anonymous user.
        return complex queryset of not own ``types='public'`` and
        or ``author=user`` and ``is_draft=False`` and ``is_removed=False``
        notebooks for authenticated user.
        """
        if not request.user.is_authenticated():
            return self.filter(type=types.NOTEBOOK_TYPE_PUBLIC)
        else:
            q = Q(author=request.user)
            q &= ~Q(is_draft=True)
            q &= ~Q(is_removed=True)
            q |= ~Q(author=request.user)
            q &= Q(type=types.NOTEBOOK_TYPE_PUBLIC)
            return self.filter(q).distinct()
    def draft(self, request):
        """
        return queryset of draft notebooks

        return empty queryset for anonymou user.
        return queryset of own draft notebooks for authenticated user.
        """
        if not request.user.is_authenticated():
            return self.none()
        return self.filter(author=request.user).filter(is_draft=True)
    def removed(self, request):
        if not request.user.is_authenticated():
            return self.none()
        return self.filter(author=request.user).filter(is_removed=True)

@lettuce.world.absorb
class Notebook(models.Model):
    """Notebook model class"""
    type = models.CharField(_('type'), max_length=10, choices=types.NOTEBOOK_TYPES, default='private')
    is_draft = models.BooleanField(_('is draft'), default=False)
    is_removed = models.BooleanField(_('is removed'), default=False)

    title = models.CharField(_('title'), max_length=255, default=_('No title'))
    description = models.TextField(_('description'), blank=True)
    author = models.ForeignKey(User, verbose_name=_('author'), related_name='notebooks')

    created_at = models.DateTimeField(_('date time created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('date time updated'), auto_now=True)

    objects = NotebookManager()
