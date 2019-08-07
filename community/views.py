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

            context = {
                'd_state' : d_state
            }
        else:
            d_state = '당신과 같은 질환을 앓는 사람의 암 발생확률은 ' + str(score * 100) + '% 였습니다.'
            d_str = ''
            d_care = ''
            h_str = ''
            h_care = ''
            l_str = ''
            l_care = ''
            if disease1 != "off":
                d_str = "당뇨 치료 필요"
                d_care = "당뇨 관리의 최우선 요소는 올바른 식단입니다. 단 음식, 가당 음료, 술을 삼가도록 합니다. 보리나 콩 위주로 밥을 짓어 먹습니다. 꾸준한 운동으로 혈당을 조절하는 것이 가장 중요합니다."
            if disease2 != "off":
                h_str = "고혈압 치료 필요"
                h_care = "신선한 채소와 과일, 저지방 유제품은 충분히 먹습니다. 붉은색 살코기와 기름기가 많은 식품, 설탕이 들어간 식품은 멀리 합니다. 무리한 운동을 삼가고 자신의 최대 운동 능력 상태에서 절반 정도 강도의 운동을 합니다."
            if disease3 != "off":
                l_str = "간질환 치료 필요"
                l_care = "정확한 간질환 종류를 진단받아 간질환의 원인을 제거합니다. 모든 원인에 의한 간질환 및 간경병은 음주는 금물입니다. 균형 잡힌 식사를 하며 민간요법을 하지 않습니다."

            context = {
                'd_state': d_state,
                'd_str': d_str,
                'h_str': h_str,
                'l_str': l_str,
                'd_care': d_care,
                'h_care': h_care,
                'l_care': l_care
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
        diab = request.POST["diab"]
        heart = request.POST["heart"]

        info = mh.MH(age, weight, waist, AST, GTP, TGS, HDL, hemo)
        info.setBMI(int(weight), int(height))
        result = mh.runModel(info)

        if (int(diab) < 126):
            diab_str = '공복혈당은 정상입니다.'
        else:
            diab_str = '당신은 당뇨 위험군에 속합니다.'

        if (int(heart) < 140):
            heart_str = '혈압은 정상입니다.'
        else:
            heart_str = '당신은 고혈압 위험군에 속합니다.'

        if (result < 0):
            default_str = '간질환은 정상입니다. 간질환이 발생할 확률은 매우 희박합니다.'
        else:
            default_str = '당신의 간질환 발생확률은 ' + str(result[0].round(2)) + '%입니다.'

        context = {
            'diab_str' : diab_str,
            'heart_str' : heart_str,
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