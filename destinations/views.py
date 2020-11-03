from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Destination
from django.utils import timezone

# Create your views here.


def get_destination(request):
    destinations = Destination.objects
    return render(request, 'destinations/destinations.html',{'destinations': destinations})

def home(request):
    destinations = Destination.objects
    return render(request, 'destinations/home.html',{'destinations': destinations})


@login_required(login_url="/accounts/signup")
def create(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['description'] and request.POST['url'] and request.FILES['icon'] and request.FILES['image']:
            product = Destinations()
            product.title = request.POST['title']
            product.body = request.POST['description']
            # append http if not present in the url
            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
                # TODO add lower case conversion of the url too
            product.icon = request.FILES['icon']
            product.image = request.FILES['image']
            product.pub_date = timezone.datetime.now()
            # product.votes_total = 1
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))
        else:
            return render(request, 'products/create.html', {'error': "All fields are required"})
    else:
        return render(request, 'products/create.html')

def detail(request, destination_id):
    destination = get_object_or_404(Destination, pk=destination_id)
    return render(request, 'destinations/detail.html', {'destination':destination})