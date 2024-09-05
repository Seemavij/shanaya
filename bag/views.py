from django.shortcuts import render, redirect,reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from products.models import Product


def view_bag(request):
    """ A view to render the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, bag_item_id):
    """ Add  item to bag """

    # item = get_object_or_404(product, pk=bag_item_id)
    item = get_object_or_404(Product, pk=bag_item_id)
    quantity = 1

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if bag_item_id in list(bag.keys()):
        messages.error(request, f"The requested quantity is not available")
    else:
        bag[bag_item_id] = quantity
        messages.success(request, f"Added {item.name} to your bag")

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, bag_item_id):
    """ Remove item from bag """

    item = get_object_or_404(Product, pk=bag_item_id)
    # Corrected model reference to Product
    bag = request.session.get('bag', {})

    if bag_item_id in bag:
        bag.pop(bag_item_id)
        messages.success(request, f"{item.name} has been successfully removed")
    else:
        messages.error(request, "Item was not found in the bag.")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))
