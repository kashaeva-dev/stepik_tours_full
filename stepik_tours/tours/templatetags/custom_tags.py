from django import template

register = template.Library()


@register.filter()
def lookup(the_dict, key):
    return the_dict.get(key, '')


@register.filter()
def word_title(string):
    pattern = str(string[0]).lower()
    return string.replace(string[0], pattern)


@register.filter()
def price_format(price):
    return str('{0:,}'.format(int(price))).replace(",", " ")


@register.filter()
def pluralize_ru1(number, string):
    lst = string.split(",")
    if number % 10 == 1 and number % 100 != 11:
        return lst[0]
    elif number % 10 >= 2 and number % 10 <= 4 and number % 100 not in [11, 12, 13, 14]:
        return lst[1]
    else:
        return lst[2]


@register.filter()
def pluralize_ru2(number, string):
    lst = string.split(",")
    if number % 10 == 1 and number % 100 != 11:
        return lst[0]
    else:
        return lst[1]
