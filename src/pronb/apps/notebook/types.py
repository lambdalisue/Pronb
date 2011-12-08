# vim: set fileencoding=utf8:
"""
Notebook types

VARIABLES:
    NOTEBOOK_TYPE_PUBLIC    - published notebook to anyone
    NOTEBOOK_TYPE_FRIEND    - published only person who know the link
    NOTEBOOK_TYPE_PRIVATE   - not published
    NOTEBOOK_TYPES          - used for choice field

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
from django.utils.text import ugettext_lazy as _

NOTEBOOK_TYPE_PUBLIC = 'public'
NOTEBOOK_TYPE_FRIEND = 'friend'
NOTEBOOK_TYPE_PRIVATE = 'private'

NOTEBOOK_TYPES = (
    (NOTEBOOK_TYPE_PUBLIC,  _('public')),
    (NOTEBOOK_TYPE_FRIEND,  _('friend')),
    (NOTEBOOK_TYPE_PRIVATE, _('private')),
)
