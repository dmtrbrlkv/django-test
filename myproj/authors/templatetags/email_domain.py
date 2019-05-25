from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='test_filter')
@stringfilter
def cut_email_domain(value):
	if '@' not in value:
		return '<not stated>'
	else:
		return value.partition('@')[2]
