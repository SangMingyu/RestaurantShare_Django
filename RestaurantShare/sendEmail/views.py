from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def sendEmail(request):
    try:
        checked_res_list = request.POST.getlist('checks')
        inputReceiver = request.POST['inputReceiver']
        inputTitle = request.POST['inputTitle']
        inputContent = request.POST['inputContent']
        restaurants = []
        for checked_res_id in checked_res_list:
            restaurants.append( Restaurant.objects.get(id = checked_res_id) )

        content = {'inputContent': inputContent, 'restaurants':restaurants}

        msg_html = render_to_string('sendEmail/email_format.html',content)

        msg = EmailMessage(subject = inputTitle, body=msg_html, from_email="ssangmg@gmail.com", bcc=inputReceiver.split(','))
        msg.content_subtype = 'html'
        msg.send()
        return render(request, 'sendEmail/sendSuccess.html')
        # return HttpResponseRedirect(reverse('index'))
    except:
        return render(request, 'sendEmail/sendFail.html')

'''
def sendEmail(request):
    checked_res_list = request.POST.getlist('checks')
    inputReceiver = request.POST['inputReceiver']
    inputTitle = request.POST['inputTitle']
    inputContent = request.POST['inputContent']
    print(checked_res_list,"/",inputReceiver,"/",inputTitle,"/",inputContent)
    return HttpResponseRedirect(reverse('index'))
'''