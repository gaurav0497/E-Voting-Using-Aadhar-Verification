from django.shortcuts import render,HttpResponse
from .models import Candidate,Voter,Official
import pytesseract
import cv2
import numpy as np
import base64
from PIL import Image
import io

def index(request):
    return render(request,'index.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        state = request.POST.get('state')
        date = request.POST.get('date')
        sex = request.POST.get('sex')
        base64 = request.POST.get('image')
        print(name, mobile, state, date, sex, base64)
    # pytesseract.pytesseract.tesseract_cmd = r'C:/Users/thaku/Tesseract-OCR/tesseract.exe'
    # base64_data = ""
    # image = np.array(Image.open(io.BytesIO(base64.b64decode(base64_data))))
    # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # print(pytesseract.image_to_string(image))
    return render(request,'register.html')

def login(request):
    video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    img = ''
    flag = True
    if video.isOpened():
        i=0
        while i<8:
            status, img = video.read()
            i+=1
    video.release()
    pytesseract.pytesseract.tesseract_cmd = r'C:/Users/thaku/Tesseract-OCR/tesseract.exe'
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print(pytesseract.image_to_string(img))
    return render(request,'voting.html',{'flag':flag})

def officerlogin(request):
    usn,pwd = '',''
    flag = False
    if request.method == "POST":
        usn = request.POST.get('usn')
        pwd = request.POST.get('pwd')
    usn = Official.objects.filter(username=usn)
    pwd = Official.objects.filter(password=pwd)
    if ((len(usn)!=0) and (len(pwd)!=0)):
        flag = True
        return render(request,'register.html',{'flag':flag})
    else:
        return render(request, 'officer.html')
    return render(request, 'officer.html')