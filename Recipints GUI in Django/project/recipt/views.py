import uuid
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def gen_pdf(request):
    if request.method =='POST':
        # Generate a random and unique bill number
        bill = str(uuid.uuid4().int)[:8]
        
        Others = request.POST['Others']
        Algo = request.POST['Algo']
        FF = request.POST['FF']
        DSA = request.POST['DSA']
        dt = request.POST['dt']
        
        Others_rt = 50
        Algo_rt = 100
        FF_rt = 350
        DSA_rt = 550
        total = (int(Others)*Others_rt + int(Algo)*Algo_rt + int(FF)*FF_rt + int(DSA)*DSA_rt)
        
        return render(request, 'pdf.html', {'Bill': bill, 'Others': Others, 'Algo': Algo, 'FF': FF, 'DSA': DSA, 'dt': dt, 'total': total})
    
    return render(request, 'index.html')
