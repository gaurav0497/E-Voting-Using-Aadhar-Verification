from django.shortcuts import render


def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        state = request.POST.get('state')
        date = request.POST.get('date')
        sex = request.POST.get('sex')
        print(name, mobile, state, date, sex)

    return render(request,'register.html')