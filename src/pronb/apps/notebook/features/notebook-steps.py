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
from lettuce import step, before, world
from nose.tools import eq_
from django.http import HttpRequest
from django.contrib.auth.models import User, AnonymousUser

from pronb.apps.notebook import models

@before.each_scenario
def set_request(scenario):
    world.request = HttpRequest()
    # TODO: add sample Notebook

@step(r'annonymous user access the "(.*)" method')
def annonymous_user_access_the_value_method(step, value):
    request = world.request
    request.user = AnonymousUser()
    world.qs = getattr(models.Notebook.objects, value)(request)
@step('he get queryset of all notebook which type is public')
def he_get_queryset_of_all_notebook_which_type_is_public(step):
    qs = world.qs.exclude(type='public')
    eq_(qs.count(), 0)
@step(r'authenticated user access the "(.*)" method')
def authenticated_user_access_the_value_method(step, value):
    request = world.request
    request.user = User.objects.get(pk=1)
    world.qs = getattr(world.Notebook.objects, value)(request)
@step(r'the queryset of all notebook which type is public are not own')
def he_get_queryset_of_all_notebook_which_type_is_public(step):
    qs = world.qs.filter(type='public')
    qs = qs.filter(author=world.request.user)
    eq_(qs.count(), 0)
@step(r'he get queryset of all notebook which he have')
def he_get_queryset_of_all_notebook_which_he_have(step):
    qs = world.qs.filter(author=world.request.user)
    qs2 = models.Notebook.objects.filter(author=world.request.user)
    qs2 = qs2.exclude(is_draft=False).exclude(is_removed=False)
    eq_(qs.count(), qs2.count())
@step(r'the queryset of all notebook which he have is assumed is_draft or is_removed is not True')
def the_queryset_of_all_notebook_which_he_have_is_assumed_is_draft_or_is_removed_is_not_true(step):
    qs = world.qs.filter(author=world.request.user)
    qs2 = qs.filter(is_draft=True)
    eq_(qs2.count(), 0)
    qs2 = qs.filter(is_removed=True)
    eq_(qs2.count(), 0)
