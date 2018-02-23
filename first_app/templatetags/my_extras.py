from django import template

register = template.Library()

@register.filter(name='cut_string')
def cut_string(value, arg):

	'''
	This cuts out all values of "arg" from the string
	'''
	return value.replace(arg, '')

# register.filter('cut_string', cut_string)