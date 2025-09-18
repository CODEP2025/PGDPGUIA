from django import template

register = template.Library()

@register.filter
def lines(value):
    """Quebra texto em linhas limpas para usar como <li>.
    Remove marcadores comuns (–, -, •) e espaços extras."""
    if not value:
        return []
    items = []
    for raw in str(value).splitlines():
        cleaned = raw.strip().lstrip("-•– ")
        if cleaned:
            items.append(cleaned)
    return items
