from django.shortcuts import render
from django.http import JsonResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import *

# Create your views here.
def main(request):
    page = Webdata.objects.first()
    client = Client.objects.all()
    fact = Facts.objects.first()
    service = Service.objects.all()
    skillright = SkillRight.objects.all()
    skillleft = SkillLeft.objects.all()
    education = Education.objects.all()
    experience = Experience.objects.all()
    portfolio = Portfolio.objects.all()
    service = Service.objects.all()
    client = Client.objects.all()


    return render(request, 'MyResume/index.html',{
        'pages': page,
        'client': client,
        'fact': fact,
        'service': service,
        'skillright': skillright,
        'skillleft': skillleft,
        'education':education,
        'experience':experience,
        'portfolio': portfolio,
        'service': service,
        'client': client,
        })

# def home(request):
#     return render(request, 'shareafric_app/test.html')


# def about(request):
#     webdata = Webdata.objects.first()
#     team_members = theTeam.objects.all()
#     services = service.objects.all()
#     return render(request, 'pages/about.html',{
#         'webdata': webdata,
#         'team_members': team_members,
#         'services': services,
        
#         })

def contactUs(request):
    if request.method == 'POST':
        # Process the form data here
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message= request.POST.get('message')

        # Data validation
        if not name and not email and not subject and not message:
            response = {'message': 'Please provide all info necessary to contact me!'}
            return JsonResponse(response, status=400)

        # Save the form data to a model
        form_data = ContactUs(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        form_data.save()

        context = {'user': name, 'message': message}
        html_message = render_to_string('shareafric_app/info.html', context)
        html_message2 = render_to_string('shareafric_app/info2.html', context)
        send_mail('Welcome to Wisteen Technology', '', 'wisteen.technology@shareafric.com', [email], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')
        send_mail('Hello Wisdom Some one have contacted you!', '', 'wisteen.technology@shareafric.com', ["wisdomisaac168@gmail.com", "okuwisdom8@gmail.com"], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')

        # Return a success JSON response
        response = {'message': 'Form submitted successfully We will get back throught your email'}
        return JsonResponse(response)
    else:
        return render(request, 'MyResume/index.html')  # Render the form template initially


# def sme_form(request):
#     if request.method == 'POST':
#         # Process the form data here
#         smeFirstName = request.POST.get('smeFirstName')
#         smeLastName = request.POST.get('smeLastName')
#         smeEmail = request.POST.get('smeEmail')
#         smeCapital= request.POST.get('smeCapital')
#         smeProject= request.POST.get('smeProject')
#         smeProjectDuration= request.POST.get('smeProjectDuration')
#         smeTractions= request.POST.get('smeTractions')
#         smeAddress= request.POST.get('smeAddress')
#         smePhone= request.POST.get('smePhone')
#         smeBusinessRegistrationDate= request.POST.get('smeBusinessRegistrationDate')
#         smeFundsInvestment= request.POST.get('smeFundsInvestment')
#         smeRegistrationNo= request.POST.get('smeRegistrationNo')
#         smeStartupStage= request.POST.get('smeStartupStage')
        
#         smePitchDeck= request.FILES.get('smePitchDeck')
#         smeCACDocuments= request.FILES.get('smeCACDocuments')
#         smeValuationReport= request.FILES.get('smeValuationReport')
#         smeFinancialModel= request.FILES.get('smeFinancialModel')

#         # Data validation
#         if not smeFirstName:
#             response = {'message': 'Please provide both name and email'}
#             return JsonResponse(response, status=400)

#         # Save the form data to a model
#         form_data = SMERegistration(
#             first_name=smeFirstName,
#             last_name=smeLastName,
#             email=smeEmail,
#             phone=smePhone,
#             registration_no=smeRegistrationNo,
#             address=smeAddress,
#             project=smeProject,
#             project_duration=smeProjectDuration,
#             tractions=smeTractions,
#             startup_stage=smeStartupStage,
#             capital= smeCapital,
#             funds_investment= smeFundsInvestment,
#             pitch_deck= smePitchDeck,
#             financial_model= smeFinancialModel,
#             cac_documents= smeCACDocuments,
#             valuation_report= smeValuationReport,
#             business_registration_date= smeBusinessRegistrationDate,
#         )

#         form_data.save()

#         context = {'user': smeFirstName}
#         html_message = render_to_string('shareafric_app/info.html', context)
#         send_mail('Welcome to shareafric', '', 'wisteen.technology@shareafric.com', [smeEmail], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')

#         # Return a success JSON response
#         response = {'message': 'Form submitted successfully'}
#         return JsonResponse(response)
#     else:
#         return render(request, 'shareafric_app/test.html')  # Render the form template initially






# def corporate_form(request):
#     if request.method == 'POST':
#         # Process the form data here
#         corporateFirstName = request.POST.get('corporateFirstName')
#         corporateLastName = request.POST.get('corporateLastName')
#         corporateEmail = request.POST.get('corporateEmail')
#         corporatePhone= request.POST.get('corporatePhone')
#         corporateRegistrationNo= request.POST.get('corporateRegistrationNo')
#         corporateAddress= request.POST.get('corporateAddress')
#         corporateProject= request.POST.get('corporateProject')
#         corporateProjectDuration= request.POST.get('corporateProjectDuration')
#         corporateTractions= request.POST.get('corporateTractions')
#         corporateStartupStage= request.POST.get('corporateStartupStage')
#         corporateCapital= request.POST.get('corporateCapital')
#         corporateFundsInvestment1= request.POST.get('corporateFundsInvestment1')
#         corporateBusinessRegistrationDate= request.POST.get('corporateBusinessRegistrationDate')
        
#         corporatePitchDeck= request.FILES.get('corporatePitchDeck')
#         corporateCACDocuments= request.FILES.get('corporateCACDocuments')
#         corporateFinancialModel= request.FILES.get('corporateFinancialModel')
#         corporateValuationReport= request.FILES.get('corporateValuationReport')

#         # Data validation
#         if not corporateFirstName and not corporateLastName:
#             response = {'message': 'Please provide both name and email'}
#             return JsonResponse(response, status=400)

#         # Save the form data to a model
#         form_data = CorporateRegistration(
#             first_name=corporateFirstName,
#             last_name=corporateLastName,
#             email=corporateEmail,
#             phone=corporatePhone,
#             registration_no=corporateRegistrationNo,
#             address=corporateAddress,
#             project=corporateProject,
#             project_duration=corporateProjectDuration,
#             tractions=corporateTractions,
#             startup_stage=corporateStartupStage,
#             capital= corporateCapital,
#             funds_investment= corporateFundsInvestment1,
#             pitch_deck= corporatePitchDeck,
#             financial_model= corporateFinancialModel,
#             cac_documents= corporateCACDocuments,
#             valuation_report= corporateValuationReport,
#             business_registration_date= corporateBusinessRegistrationDate,
#         )

#         form_data.save()

#         context = {'user': corporateFirstName}
#         html_message = render_to_string('shareafric_app/info.html', context)
#         send_mail('Welcome to shareafric', '', 'wisteen.technology@shareafric.com', [corporateEmail], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')

#         # Return a success JSON response
#         response = {'message': 'Form submitted successfully'}
#         return JsonResponse(response)
#     else:
#         return render(request, 'shareafric_app/test.html')  # Render the form template initially





# def mentor_form(request):
#     if request.method == 'POST':
#         # Process the form data here
#         mentorName = request.POST.get('mentorName')
#         mentorCountry = request.POST.get('mentorCountry')
#         mentorRegion = request.POST.get('mentorRegion')
#         mentorInterest= request.POST.get('mentorInterest')
#         mentorSector= request.POST.getlist('mentorSector')
#         mentorAdditionalInfo= request.POST.get('mentorAdditionalInfo')
#         mentorEmail= request.POST.get('mentorEmail')
#         mentorPhone= request.POST.get('mentorPhone')
#         mentorLinkedIn= request.POST.get('mentorLinkedIn')
#         mentorFacebook= request.POST.get('mentorFacebook')
#         mentorInstagram= request.POST.get('mentorInstagram')

#         # Data validation
#         if not mentorName:
#             response = {'message': 'Please provide both name and email'}
#             return JsonResponse(response, status=400)

#         # Save the form data to a model
#         form_data = MentorRegistration(
#             full_name=mentorName,
#             email=mentorEmail,
#             phone=mentorPhone,
#             organization=mentorInterest,
#             country= mentorCountry,
#             region= mentorRegion,
#             sector=mentorSector,
#             area_of_expertise_and_title=mentorAdditionalInfo,
#             linkedin= mentorLinkedIn,
#             facebook=mentorFacebook,
#             instagram=mentorInstagram,
#         )

#         form_data.save()

#         context = {'user': mentorName}
#         html_message = render_to_string('shareafric_app/info.html', context)
#         send_mail('Welcome to shareafric', '', 'wisteen.technology@shareafric.com', [mentorEmail], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')

#         # Return a success JSON response
#         response = {'message': 'Form submitted successfully'}
#         return JsonResponse(response)
#     else:
#         return render(request, 'shareafric_app/test.html')  # Render the form template initially


# def elearning_form(request):
#     if request.method == 'POST':
#         # Process the form data here
#         elearningFirstName = request.POST.get('elearningFirstName')
#         elearningLastName = request.POST.get('elearningLastName')
#         elearningEmail = request.POST.get('elearningEmail')
#         elearningUsername = request.POST.get('elearningUsername')
#         elearningPassword= request.POST.get('elearningPassword')
#         elearningInterest= request.POST.getlist('elearningInterest')
#         elearningAreas= request.POST.get('elearningAreas')
#         elearningCompany= request.POST.get('elearningCompany')
#         elearningInterests= request.POST.get('elearningInterests')
#         elearningCountry= request.POST.get('elearningCountry')
#         elearningRegion= request.POST.get('elearningRegion')
#         elearningContact= request.POST.get('elearningContact')
#         elearningPhone = request.POST.get('elearningPhone')
#         # Data validation
#         if not elearningFirstName and not elearningLastName and not elearningEmail:
#             response = {'message': 'Please provide both name and email'}
#             return JsonResponse(response, status=400)

#         # Save the form data to a model
#         form_data = ElearningRegistration(
#             first_name=elearningFirstName,
#             last_name=elearningLastName,
#             email=elearningEmail,
#             username=elearningUsername,
#             password=elearningPassword,
#             elearning_interest=elearningInterest,
#             areas_of_study=elearningAreas,
#             company=elearningCompany,
#             interests_to_communicate=elearningInterests,
#             country= elearningCountry,
#             region= elearningRegion,
#             contact_options= elearningContact,
#             phone_number = elearningPhone,
#         )

#         form_data.save()

#         context = {'user': elearningFirstName}
#         html_message = render_to_string('shareafric_app/info.html', context)
#         send_mail('Welcome to shareafric', '', 'wisteen.technology@shareafric.com', [elearningEmail], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')

#         # Return a success JSON response
#         response = {'message': 'Form submitted successfully'}
#         return JsonResponse(response)
#     else:
#         return render(request, 'shareafric_app/test.html')  # Render the form template initially






# def tourist(request):
#     if request.method == 'POST':
#         # Process the form data here
#         touristName = request.POST.get('touristName')
#         touristCountry = request.POST.get('touristCountry')
#         touristRegion = request.POST.get('touristRegion')
#         touristInterest = request.POST.getlist('touristInterest')  # Retrieve selected values as a list
#         touristSector = request.POST.getlist('touristSector')  # Retrieve selected values as a list
#         touristInfo = request.POST.get('touristInfo')
#         touristEmail = request.POST.get('touristEmail')
#         touristPhone = request.POST.get('touristPhone')
#         touristLinkedIn = request.POST.get('touristLinkedIn')
#         touristFacebook = request.POST.get('touristFacebook')
#         touristInstagram = request.POST.get('touristInstagram')
        
#         # Data validation
#         if not touristName and not touristCountry and not touristEmail:
#             response = {'message': 'Please provide both name, email, and country'}
#             return JsonResponse(response, status=400)

#         # Save the form data to a model
#         form_data = TouristRegistration(
#             name=touristName,
#             phone_number=touristPhone,
#             email=touristEmail,
#             country=touristCountry,
#             region=touristRegion,
#             additional_info=touristInfo,
#             linkedin_profile=touristLinkedIn,
#             facebook_profile=touristFacebook,
#             instagram_handle=touristInstagram,
#         )

#         form_data.save()

#         # Associate the selected interests with the model instance
#         for interest_name in touristInterest:
#             interest = TouristInterest.objects.get(name=interest_name)
#             form_data.interests.add(interest)

#         # Associate the selected sectors of interest with the model instance
#         for sector_name in touristSector:
#             sector = SectorOfInterest.objects.get(name=sector_name)
#             form_data.sector_of_interest.add(sector)

#         context = {'user': touristName}
#         html_message = render_to_string('shareafric_app/info.html', context)
#         send_mail('Welcome to shareafric', '', 'wisteen.technology@shareafric.com', [touristEmail], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')

#         # Return a success JSON response
#         response = {'message': 'Form submitted successfully'}
#         return JsonResponse(response)
#     else:
#         return render(request, 'shareafric_app/test.html')  # Render the form template initially

# def register_agreco(request):
#     if request.method == 'POST':
#         # Process the form data here
#         registrationType = request.POST.get('registrationType')
#         form = request.FILES.get('form')
#         geo = request.FILES.get('geo')
#         list1 = request.FILES.get('list1')  # Retrieve selected values as a list
#         mem = request.FILES.get('mem')  # Retrieve selected values as a list
#         deed = request.FILES.get('deed')
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         your_email = request.POST.get('your_email')
#         phone = request.POST.get('phone')
#         country = request.POST.get('country')
#         state = request.POST.get('state')
#         Comment = request.POST.get('Comment')
#         # Data validation
#         if not registrationType and not firstname and not lastname and not state and not your_email:
#             response = {'message': 'Please provide both fullname, email, and country'}
#             return JsonResponse(response, status=400)
#         form_data = AgrecoRegistration(
#             registrationType=registrationType,
#             form=form,
#             geo=geo,
#             list1=list1,
#             mem=mem,
#             deed=deed,
#             firstname=firstname,
#             lastname=lastname,
#             your_email=your_email,
#             phone=phone,
#             country=country,
#             state=state,
#             Comment=Comment,
#         )

#         form_data.save()
#         context = {'user': firstname}
#         html_message = render_to_string('shareafric_app/info.html', context)
#         send_mail('Welcome to Agreco', '', 'wisteen.technology@shareafric.com', [your_email], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')
#         send_mail('Please attend to a new registration from Agreco', '', 'wisteen.technology@shareafric.com', ["wisdomisaac168@gmail.com"], html_message=html_message, auth_user='wisteen.technology@shareafric.com', auth_password='royrex123%%')

#         # Return a success JSON response
#         response = {'message': 'Form submitted successfully'}
#         return JsonResponse(response)
#     return render(request, 'agreco/index.html')
