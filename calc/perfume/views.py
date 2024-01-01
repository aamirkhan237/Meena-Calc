from django.shortcuts import render
from .models import Product, CustomerOrder
from django.http import JsonResponse


def order_form(request):
    products = Product.objects.all()
    orders = CustomerOrder.objects.all()
    context = {"products": products, "orders": orders}
    return render(request, "order_form.html", context)


def process_order(request):
    if request.method == "POST":
        products = request.POST.getlist("product")
        grams = request.POST.getlist("grams")
        quantities = request.POST.getlist("quantity")
        discounts = request.POST.getlist("discount")

        total_price = 0
        orders = []

        for i in range(len(products)):
            product_id = products[i]
            try:
                product = Product.objects.get(id=product_id)
                grams_val = float(grams[i]) if grams[i] else 0
                quantity_val = int(quantities[i]) if quantities[i] else 0
                discount_val = float(discounts[i]) if discounts[i] else 0

                row_price = (
                    product.price_per_gram
                    * grams_val
                    * quantity_val
                    * (1 - discount_val / 100)
                )
                total_price += row_price

                order = CustomerOrder(
                    product=product,
                    grams=grams_val,
                    quantity=quantity_val,
                    discount=discount_val,
                    row_price=row_price,
                )
                order.save()
                orders.append(order)
            except (Product.DoesNotExist, ValueError):
                pass

        orders = CustomerOrder.objects.filter(
            id__in=[o.id for o in orders]
        )  # Retrieve saved orders

        context = {"orders": orders, "total_price": total_price}
        return JsonResponse({"success": True, "context": context})

    return JsonResponse({"success": False, "error": "Invalid Request"})


# Your HTML and JavaScript code remains the same with the following changes:

# 1. Add and Delete Buttons for Order Rows
# 2. Refactored JavaScript to handle row addition, deletion, and form submission efficiently.
