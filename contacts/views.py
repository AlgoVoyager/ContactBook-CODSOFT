from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from .models import Contacts
# from faker import Faker
# import random


# Create your views here.
def index(request):
    if request.method == "POST":
        post = request.POST
        if post.get("fav"):
            fav = True
        else:
            fav = False
        if request.FILES.get("ppic") is None:
            dp = "default.jpg"
        else:
            dp = request.FILES.get("ppic")

        Contacts.objects.create(
            # user=request.user,
            name=post.get("name"),
            phone=post.get("phone"),
            email=post.get("email"),
            address=post.get("addr"),
            ppic=  dp ,
            fav=fav,
        )
        return redirect("index")

    contacts = Contacts.objects.all().order_by('-id')
    mode = fav = keyw = None
    if request.GET.get("search") or request.GET.get("search") == "":
        keyw=request.GET.get("search")
        mode = request.GET.get("mode")
        if request.GET.get("fav"):
            fav=True
            contacts=contacts.filter(fav=True)
        else:
            fav=False
        if mode == "name":
            contacts=contacts.filter(name__icontains=keyw)
        elif mode == "phone":
            contacts=contacts.filter(phone__icontains=keyw)
        else:
            contacts=contacts.filter(email__icontains=keyw)


        paginator = Paginator(contacts, 10)
    else:
        paginator = Paginator(contacts, 10)

    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)

    context = {
        "contacts":page_obj,
        "total":contacts.count(),
        "fav":contacts.filter(fav=True).count(),
        "mode":mode,
        "fav_on":fav,
        "keyw":keyw

    }
    return render(request, "index.html",context=context)


def contact_details(request,id):
    contact = Contacts.objects.get(id=id)
    context = {'contact':contact}
    return render(request,'contact_details.html',context)


def delete_contact(request,id):
    contact= Contacts.objects.get(id=id)
    contact.delete()
    return redirect('/')


def edit_contact(request,id):
    contact = Contacts.objects.get(id=id)
    if request.method == "POST":
        post = request.POST
        if post.get("fav"):
            fav = True
        else:
            fav = False
        if request.FILES.get("ppic"):
            dp = request.FILES.get("ppic")
            contact.ppic = dp
            print(dp)

        name=post.get("name")
        phone=post.get("phone")
        email=post.get("email")
        address=post.get("addr")
        fav=fav
        contact.name =name
        contact.phone=phone
        contact.email=email
        contact.address=address

        contact.fav=fav
        contact.save()
        return redirect('/contact_details/'+id)

    context={'contact':contact}
    return render(request,'edit_contact.html',context)


# # Initialize Faker
# fake = Faker()
#
# # Function to populate contacts
# def populate_contacts(request):
#     # Get a user, assuming you have one available
#     user = User.objects.first()
#
#     for _ in range(30):
#         contact = Contacts.objects.create(
#             user=user,
#             name=fake.name(),
#             phone=fake.phone_number(),
#             email=fake.email(),
#             address=fake.address(),
#             fav=random.choice([True, False])
#         )
#         # Save the contact
#         contact.save()
#     return redirect('/')