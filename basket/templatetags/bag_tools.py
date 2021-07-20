from django import template

register = template.Library()

@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price*quantity

@register.filter(name='calc_delivery_total')
def calc_delivery_total(grand_total):
    return grand_total+int(5)