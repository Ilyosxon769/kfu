from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from .models import Talaba,Yonal

def main(request):
    yonal=Yonal.objects.all()
    context={'yonal':yonal}
    if request.method=='POST':
        familiya=request.POST['familiya']
        ism=request.POST['ism']
        ota_ism=request.POST['ota_ism']
        phone=request.POST['phone']
        talim=request.POST['talim']
        yonaltitle=request.POST['yonal']
        diplom=request.POST['diplom']
        pasport=request.POST['pasport']
        if 'pasport_image' in request.FILES:
            pasport_image=request.FILES['pasport_image']
            diplom_image=request.FILES['diplom_image']
            image_3x4=request.FILES['image_3x4']
            yonal=Yonal.objects.get(title=yonaltitle)
            data=Talaba(familiya=familiya,ism=ism,ota_ism=ota_ism,phone=phone,talim=talim,yonal=yonal,diplom=diplom,pasport=pasport,pasport_image=pasport_image,diplom_image=diplom_image,image_3x4=image_3x4)
            data.save()
            context['msg']='success'
    return render(request,'kfu.html',context)
def api(request):
    if request.method == 'GET':
        print(request.GET)
        if 'dip' in request.GET:
            diplom=request.GET['dip']
            javob=Talaba.objects.filter(diplom=diplom)
            if javob:
                return JsonResponse({'diplom':'yes'})
            else:
                return JsonResponse({'diplom':'no'})
            print(javob)
        elif  'pas' in request.GET:
            pasport=request.GET['pas']
            javob=Talaba.objects.filter(pasport=pasport)
            if javob:
                return JsonResponse({'pasport':'yes'})
            else:
                return JsonResponse({'pasport':'no'})
    return JsonResponse({'status':'success'})