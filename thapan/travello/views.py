from django.shortcuts import render,redirect
from .models import destination
from .forms import destinationform
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import destinationSerializer

# Create your views here.
#List of all destination or create a destination
class destinationList(APIView):
    queryset =  destination.objects.all()
    

    def get(self,request):
        
        destinations = destination.objects.all()
        serializer = destinationSerializer(destinations,many=True)
        
        return Response(serializer.data)

    def post(self):
        pass














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
    print(str(dests.query))# if u want to see query use this 
    # one = destination.objects.get(pk=1) # we can get using (pk primary contact) but not workig check later
    # print(one)
    # destination.objects.filter(name ='Jaipur').delete() # Used to delete the data in database
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



# from django.db import models

# class Blog(models.Model):
#     name = models.CharField(max_length=100)
#     tagline = models.TextField()

#     def __str__(self):
#         return self.name

# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name

# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField()
#     authors = models.ManyToManyField(Author)
#     n_comments = models.IntegerField()
#     n_pingbacks = models.IntegerField()
#     rating = models.IntegerField()

#     def __str__(self):
#         return self.headline