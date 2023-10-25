from django.http import HttpResponse, HttpResponseRedirect 
from  django.shortcuts import render
from .forms import usersForm
from service.models import Service

def home(request):
    servicesData = Service.objects.all()
    # for a in servicesData:
    #     print(a.service_icon)
    # desh(-) before column mean descending order without (-) without - mean ascending
    data={
        'servicesData': servicesData
        }
    return render(request, "index.html", data)
    # data={
    #     'title':'Home New',
    #     'bdata': 'hello',
    #     'clist': ['PHP', 'Java', 'Django'],
    #     'number': [10, 20, 30, 40, 50],
    #     'student_details':[
    #         {'name':'pradeep', 'phone':9826459320},
    #         {'name':'testing', 'phone':8719058468}
    #     ]
    # }
    # return render(request, "index.html", data)
   
def aboutUs(request):
    if request.method =="GET":
        output = request.GET.get('output')
    return render(request, "about.html", {'output':output})
def course(request):
    return render(request, "base.html")

def courseDetails(request, courseid):
    return HttpResponse(courseid)

def marksheet(request):
   
    if request.method=='POST':
        s1 = eval(request.POST.get('n1'))
        s2 = eval(request.POST.get('n2'))
        s3 = eval(request.POST.get('n3'))
        s4 = eval(request.POST.get('n4'))
        
        t = s1+s2+s3+s4
        p = t*100/400
        if p>=60:
            d="First Division"
        elif p>=40:
            d="Second Division"
        elif p>=35:
            d="Third Division"
        else:
            d="Fail"
        data={
            'total':t,
            'per':p,
            'div': d
        }
        return render(request,'marksheet.html', data)

def service(request):
    c =''
    return render(request, "service.html")

def  evenodd(request):
    c=''
    if request.POST.get('num1')=="":
        return render(request, "evenodd.html", {'error':True})
    
    
    if request.method =="POST":
        n = eval(request.POST.get('num1'))
        if n%2==0:
            c="Even Number"
        else:
            c = "Odd Number"
    return render(request, "evenodd.html", {'c':c})
def contact(request):
    return render(request, 'contact.html')
def userForm(request):
    finalans = 0
    fn = usersForm()
    data={'form':fn}
    try:
        if request.method=='POST':
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1+n2
            data={
                'form':fn,
                'output': finalans
            
            # 'n1': n1,
            # 'n2': n2,
            }
            url ="/about-us/?output={}".format(finalans)
            # return HttpResponseRedirect(url)
            return redirect(url)
            
        # n1 = int(request.GET['num1'])
        # n2 = int(request.GET['num2'])
        # n1 = int(request.GET.get('num1'))
        # n2 = int(request.GET.get('num2'))
        # print(n1+n2)
    except:
        pass
    # return render(request, 'user-form.html', {'output': finalans})
    return render(request, 'user-form.html', data) 
def submitform(request):
     try:
        if request.method=='POST':
            n1 = int(request.POST.get('num1'))
            n2 = int(request.POST.get('num2'))
            finalans = n1+n2
            data={
            'n1': n1,
            'n2': n2,
            'output': finalans
            }
            return HttpResponse(finalans)
     except:
        pass
    # return render(request, 'user-form.html', {'output': finalans})
   


def calculator(request):
    c = ''
    try:
        if request.method == "POST":
            n1 = eval(request.POST.get('num1'))
            n2 = eval(request.POST.get('num2'))
            opr = request.POST.get('opr')
            if opr == "+":
                c = n1 + n2
            elif opr == "-":
                c = n1 - n2
            elif opr == "*":  # Fixed the duplicated condition
                c = n1 * n2
            elif opr == "/":
                c = n1 / n2
    except:
        c = "Invalid opr.............."
    return render(request, "calculator.html", {'c': c})

