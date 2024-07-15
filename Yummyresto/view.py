from django.shortcuts import render,redirect
from django.core.mail import send_mail
from menu.models import starter,breakfast,lunch,dinner
from testimonials.models import testimonial
from Table_Reservation.models import tablereservation
from Client_Feedback.models import clientfeedback
from .forms import ReservationForm,Sendmessage
from CHEFS.models import chefs


def homepage(request):
    starterdata=starter.objects.all()
    breakfastdata=breakfast.objects.all()
    lunchdata=lunch.objects.all()
    dinnerdata=dinner.objects.all()
    testimonialdata=testimonial.objects.all()[:5]
    Chefsdata=chefs.objects.all()[:3]
    form = ReservationForm()
    form2=Sendmessage()
    data={"starterdata":starterdata,
          "breakfastdata":breakfastdata,
          "lunchdata":lunchdata,
          "dinnerdata":dinnerdata,
          "testimonialdata":testimonialdata,
          "Chefsdata":Chefsdata,
          "usrform":form,
          "sendform":form2,
          }
    
    return render(request, 'index.html',data)     
    

def reservationtable(request):
    form = ReservationForm()
    if request.method=="POST":
        #saving data in database
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        date=request.POST.get('date')
        time=request.POST.get('time')
        people=request.POST.get('people')
        message=request.POST.get('comments')
        # Convert time_of_day into corresponding time value
        if time == 'morning':
                time = '08:00:00-12:00:00'  # Example morning time
        elif time == 'afternoon':
                time = '12:00:00-18:00:00'  # Example afternoon time
        else:
                time = '18:00:00-23:00:00'  # Example evening time
        rt=tablereservation(name=name,email=email,phone=phone,date=date,time=time,people=people,message=message)
        rt.save()
        
        
        #sending email to register email 
        subject = "New Reservation Submission"
        email_content = f"Name: {name}<br>Email: {email}<br>Phone: {phone}<br>Date: {date}<br>Time: {time}<br>No. Of People: {people}<br>Message:{message}" 
        # Set the email addresses
        from_email = 'example@gmail.com'
        recipient_list = ['example@gmail.com']
        # Send the email
        send_mail(subject, "", from_email, recipient_list, html_message=email_content)
        rtpage = f"/thankyou/?usrform{form}"
        return redirect(rtpage)
        
    return render(request, "thankyou.html")


def thankpage(request):
    return render(request, "thankyou.html")
     
             
def chooseus(request): 
    return render(request,"chooseus.html")     

def mthankpage(request):
    return render(request,"mthank.html")  

def clfeedback(request):
    form2 = Sendmessage()
    if request.method == 'POST':
        #saving data in database
        name=request.POST.get('name')
        email=request.POST.get('email')
        subjects=request.POST.get('subject')
        message=request.POST.get('comments')
        cl=clientfeedback(name=name,email=email,subject=subjects,message=message)
        cl.save()
        
        #sending email to register email 
        subject = "New Client Feedback"   
        email_content = f"Name: {name}<br>Email: {email}<br>Subject: {subjects}<br>Message: {message}" 
        # Set the email addresses
        from_email = 'example@gmail.com'
        recipient_list = ['example@gmail.com']
        #send email 
        send_mail(subject, "", from_email, recipient_list, html_message=email_content)
        stpage = f"/mthank/?sendform={form2}"
        return redirect(stpage)
        
    return render(request,"mthank.html")
