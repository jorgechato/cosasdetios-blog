#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dynamic_preferences.types import Section
from dynamic_preferences.types import StringPreference
from dynamic_preferences.types import BooleanPreference
from dynamic_preferences.types import LongStringPreference
from dynamic_preferences.registries import global_preferences_registry

general = Section('general')


@global_preferences_registry.register
class SiteTitle(StringPreference):
    section = general
    name = 'title'
    default = 'COSAS DE TÍOS'


@global_preferences_registry.register
class GoogleAnalytics(StringPreference):
    section = general
    name = 'trackingId'
    default = 'UA-00000000-0'


@global_preferences_registry.register
class GoogleADs(StringPreference):
    section = general
    name = 'adsId'
    default = 'ca-pub-0000000000000000'


@global_preferences_registry.register
class Description(LongStringPreference):
    section = general
    name = 'description'
    default = ''


@global_preferences_registry.register
class Keywords(LongStringPreference):
    section = general
    name = 'keywords'
    default = ''


@global_preferences_registry.register
class TwitterUser(StringPreference):
    section = general
    name = 'twitter'
    default = '@beerwhisper'


@global_preferences_registry.register
class PatreonAD(LongStringPreference):
    section = general
    name = 'patreon'
    default = 'La vida debería ser una puta locura. Ahora es tu oportunidad de ayudarme.'
