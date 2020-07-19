from django.shortcuts import render
from django.http import HttpResponse
import random
import string
# Create your views here.
def home(request):
    return render(request,'generator/home.html')
def password(request):

    lowchar= list(string.ascii_lowercase) # a list of lowercase characters

    numbers = list(string.digits)# list of numbers

    symbols = list(string.punctuation)

    upcase = list(string.ascii_uppercase) # list of uppercase letters

    length = int(request.GET.get('length')) #here were getting the length put in by the user

    thepassword = ''

    if request.GET.get('uppercase'): #if they want uppercase letters we add uppercase letters to the list
        lowchar.extend(upcase)
    if request.GET.get('numbers'): #if they want numbers we add numbers  to the list
        lowchar.extend(numbers)
    if request.GET.get('special'): #if they want symbols we add symbols to the list
        lowchar.extend(symbols)


    for x in range(length):  # this is a loop that loops through the range and adds a character each time
            thepassword += random.choice(lowchar)
    return render(request, 'generator/password.html',{'password': thepassword })

def about(request):
    return render(request,'generator/about.html')