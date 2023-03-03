from django import template

from app.models import SubCategory

register = template.Library()


@register.inclusion_tag('includes/menu.html')
def draw_menu(menu):
    subcategories = SubCategory.objects.select_related('cat__menu').all()
    categories = {}
    for sub in subcategories:
        if sub.cat.menu.name != menu:
            continue
        if sub.cat in categories:
            categories[sub.cat].append(sub)
        else:
            categories[sub.cat] = [sub]
    print(categories)
    return {'categories': categories}
