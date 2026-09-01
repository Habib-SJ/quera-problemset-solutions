# کارت پستال
# ID : 21210
# https://quera.org/problemset/21210


from django import template

register = template.Library()

@register.filter
def convert(text):
    output=''

    E2P_map = {'1' : '۱', '2' : '۲', '3' : '۳', '4' : '۴', '5' : '۵', '6' : '۶', '7' : '۷', '8' : '۸', '9' : '۹', '0' : '۰' }
    for char in text:
        if char in E2P_map:
            output += E2P_map[char]
        else:
        	output += char
    return output