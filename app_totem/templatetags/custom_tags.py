from django import template
from app_totem import models

register = template.Library()

@register.simple_tag

def imp_links(initial=None, _count=[0]):
    lista = links()

    if initial is not None:
        _count[0] = initial
        return ''
    # increment counter
    _count[0] += 1
    apresenta = int(_count[0]-1)

    return lista[apresenta]


def links():
    humor_lis = []
    conta = 0
    status_humor = models.StatusAtendimento.objects.values_list('humor')
    for humor in status_humor:
        ajusta = str(humor[0]).lower()
        busca = models.Emoji.objects.values_list(ajusta)
        humor_lis.append(busca[conta][0])
        conta +=1

    return humor_lis