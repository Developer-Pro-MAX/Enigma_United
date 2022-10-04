from django.shortcuts import render
from django.http import HttpResponse 
from cryptography.fernet import Fernet

def index(request):
    # return HttpResponse("Home Page")
    return render(request, 'Home.html')

def encrypt(request):
    return render(request, "Encryption.html")

def result(request):
    message = request.POST.get('text','Nothing To Display Folk!') 
    key = Fernet.generate_key()
    encoded = message.encode()
    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    params = {'purpose':key, 'analysed_text': encrypted}
    return render(request, "Result.html",params)


def decrypt(request):
    return render(request, 'Decrypt.html')

def Decryption(request):
    key = request.POST.get('text1','Nothing To Display Folk!') 
    message = request.POST.get('text2', 'Nothing To Display Folk!')
    f2 = Fernet(key)
    decrypted = f2.decrypt(message)
    origin = decrypted.decode()
    params = {"Result":origin}
    return render(request, 'result_d.html',params)