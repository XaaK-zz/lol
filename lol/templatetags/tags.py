from django import template
register = template.Library()

@register.simple_tag
def active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''

@register.filter(name='tenlines')
def tenlines(code):
    brokencode = code.split('\n')
    if(len(brokencode) > 10):
        return '\n'.join(brokencode[:10] + ['...'])
    else:
        return code

