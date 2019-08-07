from django.shortcuts import render
from community.forms import  *

# Create your views here.
from django.http import HttpResponse
from django.template import loader
import community.model_hospital as mh
import community.model_self as ms
# 주소에 대한 함수 처리

def write(request) :
    # POST 방식일 경우
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:# form을 생성
        form = Form()

    return render(request, 'write.html', {'form':form})

def index(request) :
    template = loader.get_template('index.html')
    context = {
        'latest_question_list' : 'test',
    }
    return render(request, 'index.html')

def pabout(request) :
    template = loader.get_template('about.html')

    if request.method == 'POST':
        age = request.POST["age"]
        gender = request.POST["gender"]
        height = request.POST["height"]
        weight = request.POST["weight"]
        waist = request.POST["waist"]

        disease1 = request.POST.get("disease1", "off")
        disease2 = request.POST.get("disease2", "off")
        disease3 = request.POST.get("disease3", "off")

        info = ms.MS(disease1, disease3, disease2, gender, int(age), height, weight, waist)
        info.get_score()
        score = ms.return_state(info, info.score)

        if score == -1:
            d_state = '당신이 암에 걸릴 확률은 매우 희박합니다. 정상입니다.'
        else:
            d_state = '당신과 같은 질환을 앓는 사람의 암 발생확률은 ' + str(score * 100) + '% 였습니다.'
        context = {
            'd_state' : d_state
        }

        return HttpResponse(template.render(context, request))
    else:
        return render(request, 'about.html')

def about(request) :
    template = loader.get_template('about.html')
    default_str = '진단을 먼저 시작해 주세요'
    context = {
        'default_str': default_str,
    }
    return HttpResponse(template.render(context, request))

def phospital(request) :
    template = loader.get_template('hospital.html')

    if request.method == 'POST':
        age = request.POST.get("age", "남")
        height = request.POST["height"]
        weight = request.POST["weight"]
        waist = request.POST["waist"]
        AST = request.POST["AST"]
        GTP = request.POST["GTP"]
        TGS = request.POST["TGS"]
        HDL = request.POST["HDL"]
        hemo = request.POST["hemo"]

        info = mh.MH(age, weight, waist, AST, GTP, TGS, HDL, hemo)
        info.setBMI(int(weight), int(height))
        result = mh.runModel(info)
        if (result < 0):
            default_str = '당신은 정상입니다. 간질환이 발생할 확률은 매우 희박합니다.'
        else:
            default_str = '당신의 간질환 발생확률은 ' + str(result[0].round(2)) + '%입니다.'

        context = {
            'default_str' : default_str
        }

        return HttpResponse(template.render(context, request))
    else:
        return render(request, 'hospital.html')

def hospital(request) :
    template = loader.get_template('hospital.html')
    default_str = '진단을 먼저 시작해 주세요'
    context = {
        'default_str': default_str,
    }
    return HttpResponse(template.render(context, request))

def contact(request) :
    template = loader.get_template('contact.html')

    context= {
        '' : '',
    }
    return HttpResponse(template.render(context, request))