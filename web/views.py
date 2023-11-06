from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User, auth
from . models import *
from . forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

from django.conf import settings

# Create your views here.
# @login_required(login_url='signin')
def admin(request):
    return render(request, 'web/admin.html')
def signup(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, f"Email {email} Already Taken")
                return redirect('signup')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, f"Username {username} Already Taken")
                return redirect('signup')
            else:
                user = MyUser.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
                user.save()
                # messages.info(request, 'Registered succesefull.')
                return redirect('signupsucces')
        else:
            messages.info(request, 'The Two Passwords Not Matching')
            return redirect('signup')

    else:
        return render(request, 'web/signup.html')

def signin(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            # messages.info(request, 'Loged in succesefull.')
            return redirect('home')
        else:
            messages.info(request, 'Username or password is incorrect')
            return redirect('signin')

    else:
        return render(request, 'web/signin.html')

def logout(request):
    auth.logout(request)
    # messages.info(request, 'Loged out succesefull.')
    return redirect('logedout')


def home(request):
    return render(request, 'web/home.html')
def aboutus(request):
    return render(request, 'web/aboutus.html')
def base(request):
    return render(request, 'web/base.html')
def contactus(request):
    return render(request, 'web/contactus.html')
def contactpost(request):
    contactpost = ContactForm()
    if request.method == "POST":
        Full_Name = request.POST.get('name')
        Subject = request.POST.get('subject')
        Email = request.POST.get('email')
        Message = request.POST.get('message')
        Phone = request.POST.get('phone')
        contactpost = ContactForm(request.POST, files=request.FILES)
        if contactpost.is_valid():
            contactpost.save()
            messages.info(request, 'Message sent succesefull.')
            return redirect('contactpost')
    context={
        "contactpost":contactpost
    }
    return render(request, 'web/contactpost.html',context)
@login_required(login_url='signin')
def contactlist(request):
    contactlist = Contact.objects.all()
    countmessage= Contact.objects.all().count()
    context={
        "contactlist":contactlist,
        "countmessage":countmessage
    }
    return render(request, 'web/contactlist.html', context)
@login_required(login_url='signin')
def viewcontact(request, id):
    contact = Contact.objects.get(id=id)
    
    context = {"contact":contact}
    return render(request, 'web/viewcontact.html', context)
@login_required(login_url='signin')
def deletecontact(request, id):
    contact = Contact.objects.get(id=id)
    if request.method == "POST":
        contact.delete()
        messages.info(request, 'Message deleted succesefull.')
        return redirect('contactlist')
    
    context = {"contact":contact}
    return render(request, 'web/deletecontact.html', context)


@login_required(login_url='signin')
def dashboard(request):
    return render(request, 'web/dashboard.html')

def services(request):
    return render(request, 'web/services.html')

# courses to be tought
@login_required(login_url='signin')
def computercs(request):
    return render(request, 'web/computercs.html')
@login_required(login_url='signin')
def computereng(request):
    return render(request, 'web/computereng.html')
@login_required(login_url='signin')
def electrical(request):
    return render(request, 'web/electrical.html')
@login_required(login_url='signin')
def civil(request):
    return render(request, 'web/civil.html')
@login_required(login_url='signin')
def mechanical(request):
    return render(request, 'web/mechanical.html')
@login_required(login_url='signin')
def artificial(request):
    return render(request, 'web/artificial.html')
@login_required(login_url='signin')
def softwareeng(request):
    return render(request, 'web/softwareeng.html')
@login_required(login_url='signin')
def embeded(request):
    return render(request, 'web/embeded.html')
@login_required(login_url='signin')
def website(request):
    return render(request, 'web/website.html')
@login_required(login_url='signin')
def mobileapp(request):
    return render(request, 'web/mobileapp.html')
@login_required(login_url='signin')
def virtualreality(request):
    return render(request, 'web/virtualreality.html')
@login_required(login_url='signin')
def security(request):
    return render(request, 'web/security.html')
@login_required(login_url='signin')
def desktopapp(request):
    return render(request, 'web/desktopapp.html')
@login_required(login_url='signin')
def multmedia(request):
    return render(request, 'web/multmedia.html')
@login_required(login_url='signin')
def graphics(request):
    return render(request, 'web/graphics.html')
@login_required(login_url='signin')
def iot(request):
    return render(request, 'web/iot.html')
@login_required(login_url='signin')
def security(request):
    return render(request, 'web/security.html')
@login_required(login_url='signin')
def nertworking(request):
    return render(request, 'web/nertworking.html')

# views for success message
def signupsucces(request):
    return render(request, 'web/signupsucces.html')
def logedout(request):
    return render(request, 'web/logedout.html')

# for website frontend development
@login_required(login_url='signin')
def wfrontend(request):
    return render(request, 'web/wfrontend.html')

@login_required(login_url='signin')
def htmlcss(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/htmlcss.html',context)

@login_required(login_url='signin')
def javascript(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/javascript.html',context)

@login_required(login_url='signin')
def reactjs(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/reactjs.html',context)

@login_required(login_url='signin')
def vuejs(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/vuejs.html',context)

@login_required(login_url='signin')
def bootstrap(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/bootstrap.html',context)

@login_required(login_url='signin')
def angularjs(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/angularjs.html',context)

# for website backend development
@login_required(login_url='signin')
def wbackend(request):
    return render(request, 'web/wbackend.html')

@login_required(login_url='signin')
def django(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/django.html',context)

@login_required(login_url='signin')
def flask(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/flask.html',context)

@login_required(login_url='signin')
def php(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/php.html',context)

@login_required(login_url='signin')
def laravel(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/laravel.html',context)

@login_required(login_url='signin')
def rub(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/rub.html',context)

# for full stack website development
@login_required(login_url='signin')
def wfullstack(request):
    return render(request, 'web/wfullstack.html')

@login_required(login_url='signin')
def djangohtml(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/djangohtml.html',context)

@login_required(login_url='signin')
def flaskhtml(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/flaskhtml.html',context)

@login_required(login_url='signin')
def phphtml(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/phphtml.html',context)

@login_required(login_url='signin')
def laravelhtml(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/laravelhtml.html',context)

@login_required(login_url='signin')
def djangoreact(request):
    website = Website.objects.all()
    context={
        "website":website
    }
    return render(request, 'web/djangoreact.html',context)

# for mobile application frontend
@login_required(login_url='signin')
def mfrontend(request):
    return render(request, 'web/mfrontend.html')

@login_required(login_url='signin')
def reactnative(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/reactnative.html',context)

@login_required(login_url='signin')
def kivy(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/kivy.html',context)
@login_required(login_url='signin')
def fluter(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/fluter.html',context)

#for mobile application backnd development
@login_required(login_url='signin')
def mbackend(request):
    return render(request, 'web/mbackend.html')

@login_required(login_url='signin')
def mdjango(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/django.html',context)

@login_required(login_url='signin')
def mflask(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/flask.html',context)

@login_required(login_url='signin')
def mfirebase(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/firebase.html',context)

#for mobile application full stack development
@login_required(login_url='signin')
def mfullstack(request):
    return render(request, 'web/mfullstack.html')

@login_required(login_url='signin')
def reactnativedjango(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/reactnativedjango.html',context)

@login_required(login_url='signin')
def reactnativeflask(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/reactnativeflask.html',context)

@login_required(login_url='signin')
def reactnativefirebase(request):
    mobile = Mobile.objects.all()
    context={
        "mobile":mobile
    }
    return render(request, 'web/reactnativefirebase.html',context)

# for desktop application
@login_required(login_url='signin')
def cdeskapp(request):
    desktop = Desktop.objects.all()
    context={
        "desktop":desktop
    }
    return render(request, 'web/cdeskapp.html',context)
@login_required(login_url='signin')
def pdeskapp(request):
    desktop = Desktop.objects.all()
    context={
        "desktop":desktop
    }
    return render(request, 'web/pdeskapp.html',context)

@login_required(login_url='signin')
def kdeskapp(request):
    desktop = Desktop.objects.all()
    context={
        "desktop":desktop
    }
    return render(request, 'web/kdeskapp.html',context)

# for embeded system
@login_required(login_url='signin')
def cembeded(request):
    embeded = Embeded.objects.all()
    context={
        "embeded":embeded
    }
    return render(request, 'web/cembeded.html',context)
@login_required(login_url='signin')
def aembeded(request):
    embeded = Embeded.objects.all()
    context={
        "embeded":embeded
    }
    return render(request, 'web/aembeded.html',context)

@login_required(login_url='signin')
def pembeded(request):
    embeded = Embeded.objects.all()
    context={
        "embeded":embeded
    }
    return render(request, 'web/pembeded.html',context)

@login_required(login_url='signin')
def mpembeded(request):
    embeded = Embeded.objects.all()
    context={
        "embeded":embeded
    }
    return render(request, 'web/mpembeded.html',context)

# for graphics designing
@login_required(login_url='signin')
def photoshop(request):
    graphics = Graphics.objects.all()
    context={
        "graphics":graphics
    }
    return render(request, 'web/photoshop.html',context)

@login_required(login_url='signin')
def illustrator(request):
    graphics = Graphics.objects.all()
    context={
        "graphics":graphics
    }
    return render(request, 'web/illustrator.html',context)

# template download
@login_required(login_url='signin')
def webtemplate(request):
    return render(request, 'web/webtemplate.html')

@login_required(login_url='signin')
def htmlcsstemplate(request):
    websitetemplate = Websitetemplate.objects.all()
    context={
        "websitetemplate":websitetemplate
    }
    return render(request, 'web/htmlcsstemplate.html',context)

@login_required(login_url='signin')
def reacttemplate(request):
    websitetemplate = Websitetemplate.objects.all()
    context={
        "websitetemplate":websitetemplate
    }
    return render(request, 'web/reacttemplate.html',context)


@login_required(login_url='signin')
def mobiletemplate(request):
    return render(request, 'web/mobiletemplate.html')

@login_required(login_url='signin')
def reactnativetemplate(request):
    mobiletemplate = Mobiletemplate.objects.all()
    context={
        "mobiletemplate":mobiletemplate
    }
    return render(request, 'web/reactnativetemplate.html',context)


@login_required(login_url='signin')
def desktoptemplate(request):
    return render(request, 'web/desktoptemplate.html')

@login_required(login_url='signin')
def kivytemplate(request):
    desktoptemplate = Desktoptemplate.objects.all()
    context={
        "desktoptemplate":desktoptemplate
    }
    return render(request, 'web/kivytemplate.html',context)

@login_required(login_url='signin')
def pyqttemplate(request):
    desktoptemplate = Desktoptemplate.objects.all()
    context={
        "desktoptemplate":desktoptemplate
    }
    return render(request, 'web/pyqttemplate.html',context)

@login_required(login_url='signin')
def ctemplate(request):
    desktoptemplate = Desktoptemplate.objects.all()
    context={
        "desktoptemplate":desktoptemplate
    }
    return render(request, 'web/ctemplate.html',context)

@login_required(login_url='signin')
def tkintertemplate(request):
    desktoptemplate = Desktoptemplate.objects.all()
    context={
        "desktoptemplate":desktoptemplate
    }
    return render(request, 'web/tkintertemplate.html',context)


@login_required(login_url='signin')
def microsofttemplate(request):
    return render(request, 'web/microsofttemplate.html')

@login_required(login_url='signin')
def wordtemplate(request):
    microsofttemplate = Microsofttemplate.objects.all()
    context={
        "microsofttemplate":microsofttemplate
    }
    return render(request, 'web/wordtemplate.html',context)

@login_required(login_url='signin')
def excelltemplate(request):
    microsofttemplate = Microsofttemplate.objects.all()
    context={
        "microsofttemplate":microsofttemplate
    }
    return render(request, 'web/excelltemplate.html',context)

@login_required(login_url='signin')
def powerpointtemplate(request):
    microsofttemplate = Microsofttemplate.objects.all()
    context={
        "microsofttemplate":microsofttemplate
    }
    return render(request, 'web/powerpointtemplate.html',context)

@login_required(login_url='signin')
def publishertemplate(request):
    microsofttemplate = Microsofttemplate.objects.all()
    context={
        "microsofttemplate":microsofttemplate
    }
    return render(request, 'web/publishertemplate.html',context)


@login_required(login_url='signin')
def adobetemplate(request):
    return render(request, 'web/adobetemplate.html')

@login_required(login_url='signin')
def photoshoptemplate(request):
    adobetemplate = Adobetemplate.objects.all()
    context={
        "adobetemplate":adobetemplate
    }
    return render(request, 'web/photoshoptemplate.html',context)

@login_required(login_url='signin')
def primiertemplate(request):
    adobetemplate = Adobetemplate.objects.all()
    context={
        "adobetemplate":adobetemplate
    }
    return render(request, 'web/primiertemplate.html',context)

@login_required(login_url='signin')
def illustratortemplate(request):
    adobetemplate = Adobetemplate.objects.all()
    context={
        "adobetemplate":adobetemplate
    }
    return render(request, 'web/illustratortemplate.html',context)
    
# download image


# for posting the course and the template to the website
@login_required(login_url='signin')
def websitepost(request):
    websitepost = WebsiteForm()
    if request.method == "POST":
        websitepost = WebsiteForm(request.POST, files=request.FILES)
        if websitepost.is_valid():
            websitepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('websitepost')
    context={
        "websitepost":websitepost
    }
    return render(request, 'web/websitepost.html',context)

@login_required(login_url='signin')
def mobilepost(request):
    mobilepost = MobileForm()
    if request.method == "POST":
        mobilepost = MobileForm(request.POST, files=request.FILES)
        if mobilepost.is_valid():
            mobilepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('mobilepost')
    context={
        "mobilepost":mobilepost
    }
    return render(request, 'web/mobilepost.html',context)

@login_required(login_url='signin')
def desktoppost(request):
    desktoppost = DesktopForm()
    if request.method == "POST":
        desktoppost = DesktopForm(request.POST, files=request.FILES)
        if desktoppost.is_valid():
            desktoppost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('desktoppost')
    context={
        "desktoppost":desktoppost
    }
    return render(request, 'web/desktoppost.html',context)

@login_required(login_url='signin')
def embededpost(request):
    embededpost = EmbededForm()
    if request.method == "POST":
        embededpost = EmbededForm(request.POST, files=request.FILES)
        if embededpost.is_valid():
            embededpost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('embededpost')
    context={
        "embededpost":embededpost
    }
    return render(request, 'web/embededpost.html',context)

@login_required(login_url='signin')
def graphicspost(request):
    graphicspost = GraphicsForm()
    if request.method == "POST":
        graphicspost = GraphicsForm(request.POST, files=request.FILES)
        if graphicspost.is_valid():
            graphicspost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('graphicspost')
    context={
        "graphicspost":graphicspost
    }
    return render(request, 'web/graphicspost.html',context)

# for posting template
@login_required(login_url='signin')
def websitetemplatepost(request):
    websitetemplatepost = WebsitetemplateForm()
    if request.method == "POST":
        websitetemplatepost = WebsitetemplateForm(request.POST, files=request.FILES)
        if websitetemplatepost.is_valid():
            websitetemplatepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('websitetemplatepost')
    context={
        "websitetemplatepost":websitetemplatepost
    }
    return render(request, 'web/websitetemplatepost.html',context)

@login_required(login_url='signin')
def mobiletemplatepost(request):
    mobiletemplatepost = MobiletetemplateForm()
    if request.method == "POST":
        mobiletemplatepost = MobiletetemplateForm(request.POST, files=request.FILES)
        if mobiletemplatepost.is_valid():
            mobiletemplatepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('mobiletemplatepost')
    context={
        "mobiletemplatepost":mobiletemplatepost
    }
    return render(request, 'web/mobiletemplatepost.html',context)

@login_required(login_url='signin')
def desktoptemplatepost(request):
    desktoptemplatepost = DesktoptemplateForm()
    if request.method == "POST":
        desktoptemplatepost = DesktoptemplateForm(request.POST, files=request.FILES)
        if desktoptemplatepost.is_valid():
            desktoptemplatepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('desktoptemplatepost')
    context={
        "desktoptemplatepost":desktoptemplatepost
    }
    return render(request, 'web/desktoptemplatepost.html',context)

@login_required(login_url='signin')
def microsofttemplatepost(request):
    microsofttemplatepost = MicrosofttemplateForm()
    if request.method == "POST":
        microsofttemplatepost = MicrosofttemplateForm(request.POST, files=request.FILES)
        if microsofttemplatepost.is_valid():
            microsofttemplatepost.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('microsofttemplatepost')
    context={
        "microsofttemplatepost":microsofttemplatepost
    }
    return render(request, 'web/microsofttemplatepost.html',context)

@login_required(login_url='signin')
def adobeposttemplate(request):
    adobeposttemplate = AdobetemplateForm()
    if request.method == "POST":
        adobeposttemplate = AdobetemplateForm(request.POST, files=request.FILES)
        if adobeposttemplate.is_valid():
            adobeposttemplate.save()
            messages.info(request, 'Uploaded succesefull.')
            return redirect('adobeposttemplate')
    context={
        "adobeposttemplate":adobeposttemplate
    }
    return render(request, 'web/adobeposttemplate.html',context)

# for viewing the course and the template to the website
class viewwebsite(DetailView):
    model = Website
    template_name = 'web/viewwebsite.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form = CommentwebsiteForm

    def post(self, request, *args, **kwargs):
        form = CommentwebsiteForm(request.POST)
        if form.is_valid():
            Title = self.get_object()
            form.instance.user = request.user
            form.instance.Title = Title
            form.save()

            return redirect(reverse("viewwebsite", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments = Commentwebsite.objects.all().filter(Title=self.object.id)
        
        #zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form':self.form,
                'post_comments':post_comments,
                # 'post_comments_count':post_comments_count,
            })
        return context


class viewmobile(DetailView):
    model = Mobile
    template_name = 'web/viewmobile.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form = CommentmobileForm

    def post(self, request, *args, **kwargs):
        form = CommentmobileForm(request.POST)
        if form.is_valid():
            Title = self.get_object()
            form.instance.user = request.user
            form.instance.Title = Title
            form.save()

            return redirect(reverse("viewmobile", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments = Commentmobile.objects.all().filter(Title=self.object.id)
        
        #zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form':self.form,
                'post_comments':post_comments,
                # 'post_comments_count':post_comments_count,
            })
        return context


class viewdesktop(DetailView):
    model = Desktop
    template_name = 'web/viewdesktop.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form = CommentdesktopForm

    def post(self, request, *args, **kwargs):
        form = CommentdesktopForm(request.POST)
        if form.is_valid():
            Title = self.get_object()
            form.instance.user = request.user
            form.instance.Title = Title
            form.save()

            return redirect(reverse("viewdesktop", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments = Commentdesktop.objects.all().filter(Title=self.object.id)
        
        #zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form':self.form,
                'post_comments':post_comments,
                # 'post_comments_count':post_comments_count,
            })
        return context


class viewembeded(DetailView):
    model = Embeded
    template_name = 'web/viewembeded.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form = CommentembededForm

    def post(self, request, *args, **kwargs):
        form = CommentembededForm(request.POST)
        if form.is_valid():
            Title = self.get_object()
            form.instance.user = request.user
            form.instance.Title = Title
            form.save()

            return redirect(reverse("viewembeded", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments = Commentembeded.objects.all().filter(Title=self.object.id)
        
        #zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form':self.form,
                'post_comments':post_comments,
                # 'post_comments_count':post_comments_count,
            })
        return context


class viewgraphics(DetailView):
    model = Graphics
    template_name = 'web/viewgraphics.html'
    # count_hit = True
    # HII NI CODES KWA AJILI YA POST DETAIL PAGE KWA KUTUMIA CLASS VIEW ZINAISHIA HAPA

#SASA HIZI ZINAZOANZIA HAPA NI KWA AJILI YA COMMENT KWENYE POST HUSIKA
    form = CommentgraphicsForm

    def post(self, request, *args, **kwargs):
        form = CommentgraphicsForm(request.POST)
        if form.is_valid():
            Title = self.get_object()
            form.instance.user = request.user
            form.instance.Title = Title
            form.save()

            return redirect(reverse("viewgraphics", kwargs={
                    'pk':Title.pk

                }))
    def get_context_data(self, **kwargs):
        #kwa ajili ya kudisplay comment huo mstari wa chini
        post_comments = Commentgraphics.objects.all().filter(Title=self.object.id)
        
        #zinaendelea za kupost comment kwa admin
        context = super().get_context_data(**kwargs)
        #context["form"] = self.form
        context.update({
                'form':self.form,
                'post_comments':post_comments,
                # 'post_comments_count':post_comments_count,
            })
        return context


@login_required(login_url='signin')
def viewwebsitetemplate(request, id):
    Websitetemplateview = Websitetemplate.objects.get(id=id)
    
    context = {"Websitetemplateview":Websitetemplateview}
    return render(request, 'web/viewwebsitetemplate.html', context)

@login_required(login_url='signin')
def viewmobiletemplate(request, id):
    mobiletemplateview = Mobiletemplate.objects.get(id=id)
    
    context = {"mobiletemplateview":mobiletemplateview}
    return render(request, 'web/viewmobiletemplate.html', context)

@login_required(login_url='signin')
def viewdesktoptemplate(request, id):
    desktoptemplateview = Desktop.objects.get(id=id)
    
    context = {"desktoptemplateview":desktoptemplateview}
    return render(request, 'web/viewdesktoptemplate.html', context)

@login_required(login_url='signin')
def viewmicrosofttemplate(request, id):
    microsofttemplateview = Microsofttemplate.objects.get(id=id)
    
    context = {"microsofttemplateview":microsofttemplateview}
    return render(request, 'web/viewmicrosofttemplate.html', context)

@login_required(login_url='signin')
def viewadobetemplate(request, id):
    adobetemplateview = Adobetemplate.objects.get(id=id)
    
    context = {"adobetemplateview":adobetemplateview}
    return render(request, 'web/viewadobetemplate.html', context)

# views for deleting the course
@login_required(login_url='signin')
def deletewebsite(request, id):
    websitedelete = Website.objects.get(id=id)
    if request.method == "POST":
        websitedelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('website')
    
    context = {"websitedelete":websitedelete}
    return render(request, 'web/deletewebsite.html', context)

@login_required(login_url='signin')
def deletemobile(request, id):
    mobiledelete = Mobile.objects.get(id=id)
    if request.method == "POST":
        mobiledelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('mobileapp')
    
    context = {"mobiledelete":mobiledelete}
    return render(request, 'web/deletemobile.html', context)

@login_required(login_url='signin')
def deletedesktop(request, id):
    desktopdelete = Desktop.objects.get(id=id)
    if request.method == "POST":
        desktopdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('desktopapp')
    
    context = {"desktopdelete":desktopdelete}
    return render(request, 'web/deletedesktop.html', context)

@login_required(login_url='signin')
def deleteembeded(request, id):
    embededdelete = Embeded.objects.get(id=id)
    if request.method == "POST":
        embededdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('embeded')
    
    context = {"embededdelete":embededdelete}
    return render(request, 'web/deleteembeded.html', context)

@login_required(login_url='signin')
def deletegraphics(request, id):
    graphicsdelete = Graphics.objects.get(id=id)
    if request.method == "POST":
        graphicsdelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('graphics')
    
    context = {"graphicsdelete":graphicsdelete}
    return render(request, 'web/deletegraphics.html', context)


# views for deleting template
@login_required(login_url='signin')
def deletewebsitetemplate(request, id):
    Website = Websitetemplate.objects.get(id=id)
    if request.method == "POST":
        Website.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('Website')
    
    context = {"Website":Website}
    return render(request, 'web/deletewebsitetemplate.html', context)

@login_required(login_url='signin')
def deletemobiletemplate(request, id):
    mobiletemplatedelete = Mobiletemplate.objects.get(id=id)
    if request.method == "POST":
        mobiletemplatedelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('mobiletemplate')
    
    context = {"mobiletemplatedelete":mobiletemplatedelete}
    return render(request, 'web/deletemobiletemplate.html', context)

@login_required(login_url='signin')
def deletedesktoptemplate(request, id):
    desktoptemplatedelete = Desktoptemplate.objects.get(id=id)
    if request.method == "POST":
        desktoptemplatedelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('desktoptemplate')
    
    context = {"desktoptemplatedelete":desktoptemplatedelete}
    return render(request, 'web/deletedesktoptemplate.html', context)

@login_required(login_url='signin')
def deletemicrosofttemplate(request, id):
    microsofttemplatedelete = Microsofttemplate.objects.get(id=id)
    if request.method == "POST":
        microsofttemplatedelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('microsofttemplate')
    
    context = {"microsofttemplatedelete":microsofttemplatedelete}
    return render(request, 'web/deletemicrosofttemplate.html', context)

@login_required(login_url='signin')
def deleteadobetemplate(request, id):
    adobetemplatedelete = Adobetemplate.objects.get(id=id)
    if request.method == "POST":
        adobetemplatedelete.delete()
        messages.info(request, 'Deleted succesefull.')
        return redirect('adobetemplate')
    
    context = {"adobetemplatedelete":adobetemplatedelete}
    return render(request, 'web/deleteadobetemplate.html', context)


# views for the updating course and templates
@login_required(login_url='signin')
def updatewebsite(request, id):
    a = Website.objects.get(id=id)
    website = WebsiteForm(instance=a)
    if request.method == "POST":
        website = WebsiteForm(request.POST, files=request.FILES, instance=a)
        if website.is_valid():
            website.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('website')
    context = {"website":website}
    return render(request, 'web/updatewebsite.html', context)

@login_required(login_url='signin')
def updatemobile(request, id):
    b = Mobile.objects.get(id=id)
    mobile = MobileForm(instance=b)
    if request.method == "POST":
        mobile = MobileForm(request.POST, files=request.FILES, instance=b)
        if mobile.is_valid():
            mobile.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('mobileapp')
    context = {"mobile":mobile}
    return render(request, 'web/updatemobile.html', context)

@login_required(login_url='signin')
def updatedesktop(request, id):
    c = Desktop.objects.get(id=id)
    desktop = DesktopForm(instance=c)
    if request.method == "POST":
        desktop = DesktopForm(request.POST, files=request.FILES, instance=c)
        if desktop.is_valid():
            desktop.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('desktopapp')
    context = {"desktop":desktop}
    return render(request, 'web/updatedesktop.html', context)

@login_required(login_url='signin')
def updateembeded(request, id):
    d = Embeded.objects.get(id=id)
    embeded = EmbededForm(instance=d)
    if request.method == "POST":
        embeded = EmbededForm(request.POST, files=request.FILES, instance=d)
        if embeded.is_valid():
            embeded.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('embeded')
    context = {"embeded":embeded}
    return render(request, 'web/updateembeded.html', context)

@login_required(login_url='signin')
def updategraphics(request, id):
    j = Graphics.objects.get(id=id)
    graphics = GraphicsForm(instance=j)
    if request.method == "POST":
        graphics = GraphicsForm(request.POST, files=request.FILES, instance=j)
        if graphics.is_valid():
            graphics.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('graphics')
    context = {"graphics":graphics}
    return render(request, 'web/updategraphics.html', context)

# views for updating template
@login_required(login_url='signin')
def updatewebsitetemplate(request, id):
    e = Websitetemplate.objects.get(id=id)
    websitetemplate = WebsitetemplateForm(instance=e)
    if request.method == "POST":
        websitetemplate = WebsitetemplateForm(request.POST, files=request.FILES, instance=e)
        if websitetemplate.is_valid():
            websitetemplate.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('websitetemplate')
    context = {"websitetemplate":websitetemplate}
    return render(request, 'web/updatewebsitetemplate.html', context)

@login_required(login_url='signin')
def updatemobiletemplate(request, id):
    f = Mobiletemplate.objects.get(id=id)
    mobiletemplate = MobiletetemplateForm(instance=f)
    if request.method == "POST":
        mobiletemplate = MobiletetemplateForm(request.POST, files=request.FILES, instance=f)
        if mobiletemplate.is_valid():
            mobiletemplate.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('mobiletemplate')
    context = {"mobiletemplate":mobiletemplate}
    return render(request, 'web/updatemobiletemplate.html', context)

@login_required(login_url='signin')
def updatedesktoptemplate(request, id):
    g = Desktoptemplate.objects.get(id=id)
    desktoptemplate = DesktoptemplateForm(instance=g)
    if request.method == "POST":
        desktoptemplate = DesktoptemplateForm(request.POST, files=request.FILES, instance=g)
        if desktoptemplate.is_valid():
            desktoptemplate.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('desktoptemplate')
    context = {"desktoptemplate":desktoptemplate}
    return render(request, 'web/updatedesktoptemplate.html', context)

@login_required(login_url='signin')
def updatemicrosofttemplate(request, id):
    h = Microsofttemplate.objects.get(id=id)
    microsofttemplate = MicrosofttemplateForm(instance=h)
    if request.method == "POST":
        microsofttemplate = MicrosofttemplateForm(request.POST, files=request.FILES, instance=h)
        if microsofttemplate.is_valid():
            microsofttemplate.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('microsofttemplate')
    context = {"microsofttemplate":microsofttemplate}
    return render(request, 'web/updatemicrosofttemplate.html', context)

@login_required(login_url='signin')
def updateadobetemplate(request, id):
    i = Adobetemplate.objects.get(id=id)
    adobeposttemplate = AdobetemplateForm(instance=i)
    if request.method == "POST":
        adobeposttemplate = AdobetemplateForm(request.POST, files=request.FILES, instance=i)
        if adobeposttemplate.is_valid():
            adobeposttemplate.save()
            messages.info(request, 'Updated succesefull.')
            return redirect('adobeposttemplate')
    context = {"adobeposttemplate":adobeposttemplate}
    return render(request, 'web/updateadobetemplate.html', context)




