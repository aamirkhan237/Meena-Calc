from django.shortcuts import render
from .models import Product, CustomerOrder
from django.http import JsonResponse
from .serializers import CustomerOrderSerializer
from decimal import Decimal


def order_form(request):
    if request.method == "POST":
        # Retrieve form data
        products_list = request.POST.getlist("product[]")
        grams_list = request.POST.getlist("grams[]")
        quantities_list = request.POST.getlist("quantity[]")
        discounts_list = request.POST.getlist("discount[]")

        # Process the order
        total_price = Decimal("0")
        new_orders = []

        for i in range(len(products_list)):
            product_id = products_list[i]
            try:
                product = Product.objects.get(id=product_id)
                grams_val = Decimal(grams_list[i]) if grams_list[i] else Decimal("0")
                quantity_val = int(quantities_list[i]) if quantities_list[i] else 0
                discount_val = (
                    Decimal(discounts_list[i]) if discounts_list[i] else Decimal("0")
                )

                row_price = (
                    product.price_per_gram
                    * grams_val
                    * quantity_val
                    * (Decimal("1") - discount_val / Decimal("100"))
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
                new_orders.append(order)
            except (Product.DoesNotExist, ValueError):
                pass

        new_orders = CustomerOrder.objects.filter(id__in=[o.id for o in new_orders])
        serializer = CustomerOrderSerializer(new_orders, many=True)
        serialized_orders = serializer.data

        context = {
            "orders": serialized_orders,
            "total_price": total_price,
        }
        return JsonResponse({"success": True, "context": context})

    else:  # For GET request
        products = Product.objects.all()
        orders = CustomerOrder.objects.all()
        context = {"products": products, "orders": orders}
        return render(request, "order_form.html", context)
