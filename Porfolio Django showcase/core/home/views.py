from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def gen_pdf(request):
    if request.method == "POST":
        name = request.POST.get('name', '')  # Accept any input as a string
        about = request.POST.get('about', '')  # Accept any input as a string
        pro1 = request.POST.get('pro1', '') 
        pd1 = request.POST.get('pd1', '') 
        pro2 = request.POST.get('pro2', '') 
        pd2 = request.POST.get('pd2', '') 
        pro3 = request.POST.get('pro3', '') 
        pd3 = request.POST.get('pd3', '') 
        ach1 = request.POST.get('ach1', '') 
        ad1 = request.POST.get('ad1', '') 
        ach2 = request.POST.get('ach2', '') 
        ad2 = request.POST.get('ad2', '') 
        ad3 = request.POST.get('ad3', '')
        ach3 = request.POST.get('ach3', '') 
        address = request.POST.get('address', '')
        number = request.POST.get('number', '')
        email = request.POST.get('email', '')

        return render(request, 'pdf.html', {'name': name, 'about': about, 'pro1':pro1, 'pd1':pd1,'pro2':pro2 , 'pd2':pd2, 'pro3':pro3, 'pd3':pd3, 'ach1':ach1 ,'ad1': ad1, 'ach2':ach2, 'ad2':ad2, 'ad3':ad3, 'ach3':ach3, 'address':address, 'number':number, 'email':email})

    return render(request, 'index.html')
