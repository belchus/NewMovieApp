from django import template

register = template.Library()

@register.filter
def stars(rating):
    full_stars = int(rating)
    empty_stars = 5 - full_stars

    full_stars_html = '<i class="fas fa-star"></i>' * full_stars
    empty_stars_html = '<i class="far fa-star"></i>' * empty_stars

    return full_stars_html + empty_stars_html