from django.shortcuts import render
from .models import Contacts


# Create your views here.
def index(request):
    if request.method == "POST":
        post = request.POST
        if post.get("fav"):
            fav = True
        else:
            fav = False
        Contacts.objects.create(
            # user=request.user,
            name=post.get("name"),
            phone=post.get("phone"),
            email=post.get("email"),
            address=post.get("addr"),
            ppic=request.FILES.get("ppic"),
            fav=fav,
        )
    contacts = Contacts.objects.all()
    context = {"contacts":contacts}
    return render(request, "index.html",context=context)
