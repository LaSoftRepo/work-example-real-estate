# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from common_urls import urlpatterns as urlpatterns_common
from articles_urls import urlpatterns as urlpatterns_articles
from main_urls import urlpatterns as urlpatterns_main
from static_urls import urlpatterns as urlpatterns_static
from services_urls import urlpatterns as urlpatterns_service
from settings_urls import urlpatterns as urlpatterns_settings
from objects_urls import urlpatterns as urlpatterns_objects
from trust_urls import urlpatterns as urlpatterns_trust
from contact_urls import urlpatterns as urlpatterns_contact

urlpatterns = []
urlpatterns.extend(urlpatterns_articles)
urlpatterns.extend(urlpatterns_common)
urlpatterns.extend(urlpatterns_main)
urlpatterns.extend(urlpatterns_static)
urlpatterns.extend(urlpatterns_service)
urlpatterns.extend(urlpatterns_settings)
urlpatterns.extend(urlpatterns_objects)
urlpatterns.extend(urlpatterns_trust)
urlpatterns.extend(urlpatterns_contact)