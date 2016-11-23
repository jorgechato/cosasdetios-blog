from django import template
from subprocess import PIPE, Popen
from fortune.models import Fortune
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def cowsay():
    cow = Popen(['/usr/games/cowsay', Fortune.fortune()], stdout=PIPE)
    output = cow.stdout.read()
    cow.stdout.close()

    return mark_safe('<div><pre>{}</pre></div>'.format(
        output.decode(encoding='UTF-8')))
