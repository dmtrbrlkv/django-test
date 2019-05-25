from django import template
from random import choice
from django.utils.safestring import mark_safe

register = template.Library()

text = [
    'text1',
    'text2',
    'text3'
]


@register.simple_tag
def get_text(index=None):
	if index is None or not isinstance(index, int) or index >= len(text):
		res = choice(text)
	else:
		res = text[index]
	return mark_safe(f'<p>{res}</p>')