from django import template


register = template.Library()

CENSOR_LIST = ['каганатом', "яснее"]


@register.filter()
def censor(value):
    if not isinstance(value, str):
        raise ValueError('Неправильные данные')

    for word in CENSOR_LIST:
        value = value.replace(word[1:], '*' * (len(word) - 1))
        return value
