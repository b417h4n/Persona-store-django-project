
from app1.models import Toy
from app1.models import Orders
from django.shortcuts import render


def index_page(request):

    print()
    # get image and info for section2 by status filtering
    section2 = Toy.objects.filter(status="section2").first()
    section2_toy_info = Toy.objects.filter(toy_name=section2.toy_name).filter(status='').first()

    # get all toys except one that belongs to section 2
    all_toys = Toy.objects.filter(status="")
    print(all_toys)

    # processing form data
    if request.method == 'POST':
        customer_name = request.POST.get('customer_name')
        customer_email = request.POST.get('customer_email')
        customer_ph_num = request.POST.get('customer_ph_number')
        customer_address = request.POST.get('customer_address')
        try:
            # Create an instance of the model
            customer = Orders(customer_name=customer_name, customer_email=customer_email,
                              customer_ph_number=customer_ph_num, customer_address=customer_address)
            customer.save()
            # Save the instance to the database

        except Exception as e:
            # If an error occurs, print the error message
            print(f"Error: {e}")

    # toys after 'soon' will be displayed in that range that will
    soon_count_range = 3 - len(all_toys) % 3

    context = {
        "get_toys": all_toys,
        "section2": section2,
        "range_of_soon": range(soon_count_range),
        "metis": section2_toy_info
    }
    return render(request, 'index.html', context)
