from django import template
from subprocess import PIPE, Popen
from fortune.models import Fortune, Pack
from django.utils.safestring import mark_safe
from fortune import utils


register = template.Library()

fortunes_path = utils.get_fortunes_path()
humorists_fortunes_path = fortunes_path.joinpath("humorists")
Pack.load(str(humorists_fortunes_path))


@register.simple_tag
def cowsay():
    cow = Popen(['/usr/games/cowsay', Fortune.fortune()], stdout=PIPE)
    output = cow.stdout.read()
    cow.stdout.close()

    return mark_safe('<div><pre>{}</pre></div>'.format(
        output.decode(encoding='UTF-8')))
