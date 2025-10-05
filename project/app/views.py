from django.shortcuts import render
def pow(request):
    P = None
    I = None
    R = None
    if request.method == 'POST':
         
        I = int(request.POST.get('intensity',0))
        R = int(request.POST.get('resistance',0))
        P = (I**2)*R
    return render(request, 'app/math.html' ,{"P":P})


