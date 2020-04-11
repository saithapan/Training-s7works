from django.shortcuts import render,redirect
from .models import destination
from .forms import destinationform
# Create your views here.
def index(request):
    # dest1 = destination()
    # dest1.name="Hyderabad"
    # dest1.desc="The city never sleeps"
    # dest1.img = "destination_1.jpg"
    # dest1.price =850
    # dest1.offer = True

    # dest2 = destination()
    # dest2.name="Bangalore"
    # dest2.desc="The city is nice"
    # dest2.img = "destination_2.jpg"
    # dest2.price =650
    # dest2.offer = False

    # dest3 = destination()
    # dest3.name="Delhi"
    # dest3.desc="The city is cool"
    # dest3.img = "destination_3.jpg"
    # dest3.price =450
    # dest3.offer = False

    # dests = [dest1,dest2,dest3]

    dests = destination.objects.all()
    form = destinationform()
    

    return render(request, 'index.html', {'dests':dests,'form':form})


# creating a form a taken that form here and mapping to model thing whenn user press submit 
# instead uploading from admin it is one kind of solution 

def post_destination(request):

    form = destinationform(request.POST,request.FILES)
    if form.is_valid():
        destinationfo = destination(name=form.cleaned_data['name'],
                                    img=form.cleaned_data['img'],
                                    price=form.cleaned_data['price'],
                                    desc=form.cleaned_data['desc'],
                                    offer=form.cleaned_data['offer']
                                    )
        destinationfo.save()
    return redirect("/")    




# def detail(request):
#     return render(request,'details.html')

# def detail(request,city_id):

#     city = destination.objects.get(id=city_id)
#     return render(request,'details.html',{'city':city})