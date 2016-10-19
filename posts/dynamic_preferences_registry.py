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
    default = 'EL PAPEO NERD'


@global_preferences_registry.register
class GoogleAnalytics(StringPreference):
    section = general
    name = 'trackingId'
    default = 'UA-00000000-0'


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
