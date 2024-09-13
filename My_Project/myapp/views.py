from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .forms import *

# Create your views here.

def myfirstpage(request):
    return render(request, 'index.html')

def mysecondpage(request):
    return render(request, 'second.html')

def mythirdpage(request):
    var = "hello world"
    greetings = "hey how are you"
    fruits = ['apple','mango','banana']
    num1, num2 = 10, 7
    ans = num1 > num2
    # print(ans)
    mydictionary = {
        "var": var,
        "msg": greetings,
        "myfruits": fruits,
        "num1": num1,
        "num2": num2,
        "ans": ans
    }
    return render(request, 'third.html', context=mydictionary)

def myimagepage(request):
    return render(request, 'imagepage.html')

def myimagepage2(request):
    return render(request, 'imagepage2.html')

def myform(request):
    return render(request, 'myform.html')

def submitmyform(request):
    mydictionary = {
        "var1" : request.POST['mytext'],
        "var2" : request.POST['mytextarea'],
        "method" : request.method
    }
    return JsonResponse(mydictionary)

def myform2(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            email = request.POST['email']
            mydictionary = {
                "form" : FeedbackForm()
            }
            errorflag = False
            Errors = []
            if title != title.upper():
                errorflag = True
                errormsg = "Title should be in Capital"
                Errors.append(errormsg)

            import re
            regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            if not re.search(regex,email):
                errorflag = True
                errormsg = "Not a Valid Email Address"
                Errors.append(errormsg)

            if errorflag != True:
                mydictionary["success"] = True
                mydictionary["successmsg"] = "Form Submitted"

            mydictionary["error"] = errorflag
            mydictionary['errors'] = Errors
            print(mydictionary)
            return render(request,'myform2.html', context=mydictionary)

          
          
          
            # print(title)
        #     print(subject)
        #     var = str("Form Submitted " + str(request.method))
        #     return HttpResponse(var)
        # else:
        #     mydictionary = {
        #         "form" : form
        #     }
        #     return render(request,'myform2.html', context=mydictionary)


    elif request.method == 'GET':
        form = FeedbackForm()
        mydictionary = {
            "form" : form
        }
        return render(request,'myform2.html', context=mydictionary)