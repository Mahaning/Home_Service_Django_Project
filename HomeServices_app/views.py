from datetime import datetime
import random
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.db import transaction
from .models import Response, State, workers, users, ServiceCatogarys, Country, City, Feedback, ServiceRequests
from .forms import stateform



class Commenlib:
    def __init__(self):
        self.DEFAULT_REDIRECT_PATH={'ROOT':'/'}

common_lib = Commenlib()

# Create your views here.
class Login(View):
    def get(self, request):
        return render(request, 'login.html')
    def post(self,request):
        username = request.POST['uname']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        print(user)
        # print(user.username)

        if user is not None:
            login(request, user)
            if user.is_superuser and user.is_staff:
                return  HttpResponseRedirect('/admmin_home')
                # return render(request, 'adminhome.html')

            elif user.is_staff:
                return HttpResponseRedirect('/workers_home')
            else:
                return HttpResponseRedirect('/index')
        else:
            return render(request, 'login.html', {'error_msg': "Invalid credentials."})

def logout_view(request):
    logout(request)
    # return redirect('login')
    return redirect('login')

class User_Register(View):
    def get(self, request):
        return render(request, 'user_register.html')

    def post(self,request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        email = request.POST.get('email')
        contact_number = request.POST.get('contactnumber')
        address = request.POST.get('address')
        profile_pics = request.FILES.get('profile_pic')
        gender = request.POST.get('gender')
        # user_type = request.POST.get('usertype')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        # user_type= 3
        # Check if passwords match
        if password == cpassword:
            new_user = User.objects.create(
                username=email,
                email=email,
                password=make_password(password),
                first_name=first_name,
                last_name=last_name,
                is_active=True,
                is_staff=False,
            )


            users.objects.create(admin=new_user, Address=address, gender=gender, contact_number=contact_number,profile_pic=profile_pics)
            return render(request, 'login.html', {'msg': "Addd succsfully!"})


        else:
            return render(request, 'user_register.html', {'msg': "Passwords do not match!"})

        return render(request, 'user_register.html', {'msg': "Something went wrong"})




class Worker_Register(View):
    def get(self, request):
        designations=ServiceCatogarys.objects.all()
        contaxt={
            'designations':designations,
        }
        return render(request, 'workers_registration.html',contaxt)

    def post(self, request):
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        contactnumber = request.POST.get('contactnumber')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        city = request.POST.get('city')
        address = request.POST.get('address')
        designation = request.POST.get('designation')
        profile_pic = request.FILES.get('profile_pic')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        # user_type= 3
        # Check if passwords match
        if password == cpassword:
            new_user = User.objects.create(
                username=email,
                email=email,
                password=make_password(password),
                first_name=firstname,
                last_name=lastname,
                is_active=True,
                is_staff=True,
            )

            # For 'users'
            new_worker = workers(admin=new_user, contact_number=contactnumber, dob=dob, Address=address, city=city,
                                 gender=gender, designation=designation, profile_pic=profile_pic,
                                 acc_activation=False, avalability_status=True)
            new_worker.save()

            return render(request, 'login.html', {'msg': "Addd succsfully!"})

            # return render(request, 'user_register.html', {'msg': "Passwords do not match!"})


        else:
            return render(request, 'workers_registration.html', {'msg': "Passwords do not match!"})

        return render(request, 'workers_registration.html', {'msg': "Something went wrong"})




class home(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self, request):
        services = ServiceCatogarys.objects.all()
        feedbacks = Feedback.objects.select_related('User').all()
        all_services = list(ServiceCatogarys.objects.all())  # Convert QuerySet to a list
        selected_services = random.sample(all_services, 3)  # Select 6 random services
        print('services:', services)
        context = {
            'services': services,
            'feedbacks': feedbacks,
            'selected_services': selected_services,
        }
        return render(request, 'userpages/index.html', context)

class about(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        return render(request, 'userpages/about.html')
    
class services(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        services = ServiceCatogarys.objects.all()
        feedbacks = Feedback.objects.select_related('User').all()
        all_services = list(ServiceCatogarys.objects.all())  # Convert QuerySet to a list
         # Select 6 random services
        print('services:', services)
        context = {
            'services': services,
            'feedbacks': feedbacks,
        }
        return render(request,'userpages/service.html',context)
class bookservice(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request,id):
        services = ServiceCatogarys.objects.get(id=id)
        city=City.objects.all()
        print(services.Name)
        context = {
            'services': services,
            'city':city,
        }
        return render(request,'userpages/servicebook.html',context)
    def post(self,request,id):
        user_id = request.user.id
        user=users.objects.get(admin=user_id)
        print(user)
        problem_description = request.POST.get('Problem_Description')
        service_id = ServiceCatogarys.objects.get(id=id)
        # service_id = request.POST.get('service')
        address = request.POST.get('Address')
        city_id = request.POST.get('city')
        pin = request.POST.get('Pincode')
        house_no = request.POST.get('House_No')
        landmark = request.POST.get('landmark')
        contact = request.POST.get('contact')

        # Create a new ServiceRequests instance and save it
        service_request = ServiceRequests(
            user=user,
            Problem_Description=problem_description,
            service=service_id,
            Address=address,
            city_id=city_id,
            pin=pin,
            House_No=house_no,
            landmark=landmark,
            contact=contact,
        )
        service_request.save()

        # Redirect to a success page or any other page as needed
        return HttpResponse('success_page')

class admmin_home(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        total_requests = ServiceRequests.objects.count()
        completed_requests = Response.objects.filter(status=True).count()
        pending_requests = Response.objects.filter(status=False).count()
        total_users = users.objects.count()
        context = {
            'total_requests': total_requests,
            'completed_requests': completed_requests,
            'pending_requests': pending_requests,
            'total_users': total_users,
        }
        return render(request, 'adminpages/adminhompage.html',context)

class workers_home(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        total_requests = ServiceRequests.objects.count()
        completed_requests = Response.objects.filter(status=True).count()
        pending_requests = Response.objects.filter(status=False).count()
        total_users = users.objects.count()
        context = {
            'total_requests': total_requests,
            'completed_requests': completed_requests,
            'pending_requests': pending_requests,
            'total_users': total_users,
        }
        return render(request, 'workerpages/Workerhompage.html',context)
    
class contact(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        return render(request, 'userpages/contact.html')





class manageworker(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        workers_records=workers.objects.all()
        context={'workers_records':workers_records}
        return render(request,'adminpages/Manage_Workers.html',context)

class verify_worker(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request, action, id):
        btn = workers.objects.get(id=id)
        if action == 'active' and btn.acc_activation == False:
            workers.objects.filter(id=id).update(acc_activation=True)
            return HttpResponseRedirect('/manageworker')
        else:
            return HttpResponse("Something Went Wrong")
        
        return HttpResponseRedirect('/manageworker')

class manageusers(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        users_records=users.objects.all()
        context={'users_records':users_records}
        return render(request,'adminpages/View_Users.html',context)


class AddCountry(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self, request):
        return render(request, 'country.html')

    def post(self, request):
        country_name = request.POST.get('name')
        Country.objects.create(name=country_name)
        return HttpResponseRedirect('/ManageCountry')

class ManageCountry(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        Country_record=Country.objects.all()
        context={
            'Country_record':Country_record
        }
        return render(request,'adminpages/Manage_Country.html',context)
class DeleteCountry(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request,id):
        data=Country.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect('/ManageCountry')



class ManageState(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        State_record=State.objects.all()
        context={
            'State_record':State_record
        }
        return render(request,'adminpages/ManageState.html',context)

class AddState(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self, request):
        country_recorsd = Country.objects.all()
        return render(request, 'state.html', {'country_recorsd': country_recorsd})

    def post(self, request):
        form = stateform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/ManageState')
        else:
            # Handle the case where the form data is not valid
            country_records = State.objects.all()
            return render(request, 'state.html', {'form': form, 'country_records': country_records})

class DeleteState(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request,id):
        data=State.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect('/ManageState')

class managecity(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        city_records=City.objects.all()
        context={
            'city_records':city_records
        }
        return render(request,'adminpages/ManageCity.html',context)
    
class AddCity(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        states=State.objects.all()
        return render(request, 'city.html',{'state_recorsd':states})

    def post(self, request):
        city_name = request.POST.get('name')
        state=request.POST.get('state')
        City.objects.create(name=city_name,state=state)
        return HttpResponseRedirect('/managecity')
    
class DeleteCity(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request,id):
        data=City.objects.get(id=id)
        data.delete()
        return HttpResponseRedirect('/managecity')



class AddServices(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        return render(request,'adminpages/ServiceCatogry.html')
    def post(self,request):
        Name = request.POST.get('Name')
        Description = request.POST.get('Description')
        img = request.FILES.get('img')
        ServiceCatogarys.objects.create(Name=Name,Description=Description,img=img)

        return HttpResponseRedirect("/ManageServices")



class ManageServices(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        service_records=ServiceCatogarys.objects.all()
        context= {
            'services':service_records,
        }
        return render(request,'adminpages/Manage_Services.html',context)
    

        # form = ServiceCatogoryForm(request.POST,request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return HttpResponse("Ok")
        # else:
        #     return HttpResponse('wrong')

class DeleteServices(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request,id):
        data = ServiceCatogarys.objects.get(id=id)
        data.delete()

        service_records=ServiceCatogarys.objects.all()
        context= {
            'services':service_records,
        }
        return render(request,'adminpages/Manage_Services.html',context)
    
class EditServices(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self, request, id):
        service = get_object_or_404(ServiceCatogarys, id=id)
        return render(request,'adminpages/ServiceCatogry.html',{'record':service})
    
    def post(self, request, id):
        service = get_object_or_404(ServiceCatogarys, id=id)
        Name = request.POST.get('Name')
        Description = request.POST.get('Description')
        img = request.FILES.get('img')

        # Update the service category fields
        service.Name = Name
        service.Description = Description
        if img:
            service.img = img
        service.save()
        return HttpResponse("Update Successful")
    
class feedback_form(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        worker = workers.objects.all()
        return render(request, 'userpages/feedback_form.html', {'workers': worker})
    def post(self,request):
        rating = int(request.POST['rating'])
        description = request.POST['description']
        user = request.user  # Get the currently logged-in user instance
        employ_id = request.POST['employ']
        employ = workers.objects.get(id=employ_id)
        date = datetime.now()

        # Create a new Feedback instance and assign the user, employ, and date
        feedback = Feedback.objects.create(Rating=rating, Description=description, User=user, Employ=employ, Date=date)
        feedback.save()

        return HttpResponse('feedback_success')

class viewfeedbacks(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        feedback_records=Feedback.objects.all()
        context= {
            'feedback_records':feedback_records,
        }
        return render(request,'adminpages/View_feedbacks.html',context)

class ViewRequests(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        request_records=ServiceRequests.objects.all()
        context={
            'request_records':request_records,
        }
        return render(request, 'adminpages/View_request.html', context)



class ViewColleagues(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        workers_records = workers.objects.all()
        context = {'workers_records': workers_records}
        return render(request, 'workerpages/View_colleagues.html', context)

# class WorkerViewRequests(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
#     def get(self,request):
#         worker=request.user.id
#         print("worker_id",worker)
        
#         request_records=ServiceRequests.objects.all()
#         Response_record=Response.objects.all()
#         wo=workers.objects.filter(admin=worker)
#         asss = Response.objects.filter(assigned_worker__admin__id=worker)
#         print(asss)
#         # =Response_record.filter
#         context={
#             'request_records':request_records,
#             'Response_record':Response_record,
#         }
#         return render(request, 'workerpages/View_request.html', context)

class WorkerViewRequests(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self, request):
        worker_id = request.user.id
        print("worker_id", worker_id)
        assigned_responses = Response.objects.filter(assigned_worker__admin__id=worker_id)
        service_ids = [response.requests.service.id for response in assigned_responses]
        request_records = ServiceRequests.objects.filter(service__id__in=service_ids)

        context = {
            'request_records': request_records,
            'assigned_responses': assigned_responses,
        }
        return render(request, 'workerpages/View_request.html', context)


class viewworkerfeedbacks(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        feedback_records=Feedback.objects.all()
        context= {
            'feedback_records':feedback_records,
        }
        return render(request,'workerpages/View_feedbacks.html',context)


class viewrequests(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        worker=request.user
        print("worker_id",worker)
        request_records=ServiceRequests.objects.all()
        context= {
            'request_records':request_records,
        }
        return render(request,'adminpages/View_request.html',context)
    
class acceptrequest(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request,action,id):
        request_records=ServiceRequests.objects.get(id=id)
        
        if action == 'accept' and request_records.status == False:
            ServiceRequests.objects.filter(id=id).update(status=True)
            assigned_worker=request.user
            # worker_id=User.objects.get(username=assigned_worker)
            userid = request.user.id
            worker_id=workers.objects.get(admin=userid) 
            response=Response.objects.create(requests=request_records,assigned_worker=worker_id,status=False)
            return HttpResponseRedirect('/WorkerViewRequests')
        
        elif action == 'reject' and request_records.status == True:
            ServiceRequests.objects.filter(id=id).update(status=False)
            response=Response.objects.get(requests=request_records)
            response.delete()


            return HttpResponseRedirect('/WorkerViewRequests')
        
class viewresponse(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        Response_records=Response.objects.all()
        context= {
            'Response_records':Response_records,
        }
        return render(request,'adminpages/view_response.html',context)
    
class workerviewresponse(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        worker_id = request.user.id
        print("worker_id", worker_id)
        assigned_responses = Response.objects.filter(assigned_worker__admin__id=worker_id)
        Response_records=Response.objects.all()
        context= {
            'Response_records':assigned_responses,
        }
        return render(request,'workerpages/viewpending_task.html',context)


class Viewappointment_history(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self, request):
            # Get the logged-in user's ID
            user_id = request.user.id

            # Query request data for the logged-in user
            requests_data = ServiceRequests.objects.filter(user__admin_id=user_id)

            # Initialize lists to store request and response data
            request_list = []
            response_list = []

            for request_data in requests_data:
                # Check if a response exists for the request
                response = Response.objects.filter(requests=request_data).first()

                if response:
                    # If a response exists, add it to the response list
                    response_list.append(response)
                else:
                    # If no response exists, add the request to the request list
                    request_list.append(request_data)

            context = {
                'requests': request_list,
                'responses': response_list,
            }

            return render(request, 'userpages/appointment_history.html', context)
    


class CancelRequest(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request,id):
        if request.user.is_superuser:
            r_id=ServiceRequests.objects.get(id=id)
            r_id.delete()
            return HttpResponseRedirect('/ViewRequests')
        
        else:
            uid=request.user.id
            # admin=User.object.get(admin=uid)
            user=users.objects.get(admin=uid)
            user_id=user.id
            r_id=ServiceRequests.objects.get(Q(id=id) & Q(user=user_id))
            r_id.delete()
            return HttpResponseRedirect('/index')


class AssignWorker(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request,id):
        req=ServiceRequests.objects.get(id=id)
        service=req.service.Name
        print(service)

        workers_records=workers.objects.filter(designation=service)
        # print(worker)
        context={
            'req':req,
            'workers_records':workers_records,
        }
        return render(request, 'adminpages/assign_worker.html', context)

    def post(self,request,id):
        ServiceRequests.objects.filter(id=id).update(status=True)
        worker = request.POST.get('assigned_worker')
        req=ServiceRequests.objects.get(id=id)
        print(worker)
        assigned_worker=workers.objects.get(id=worker)
        print(assigned_worker)
        worker_id=workers.objects.get(id=worker) 
        response=Response.objects.create(requests=req,assigned_worker=worker_id,status=False)
        return HttpResponseRedirect('/viewresponse')
        
class userprofile(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):
        id=request.user.id
        data=users.objects.get(admin=id)
        context={
            'data':data,
        }
        return render(request,'userpages/user_profile.html',context)
    
class workerprofile(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request):

        user=request.user.id

        data=workers.objects.get(admin=user)
        context={
            'data':data,
        }
        return render(request,'workerpages/worker_profile.html',context)

class markcompleted(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self, request, action, id):
        try:
            if action == 'completed':
                Response.objects.filter(id=id, status=False).update(status=True)
                print("Response status updated successfully.")
            else:
                print("Action not 'completed' or status is already True.")

            return HttpResponseRedirect('/WorkerpendingTask')
        except Response.DoesNotExist:
            print(f"Response with id {id} does not exist.")
            return HttpResponse(status=404)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return HttpResponse(status=500)

class reject(LoginRequiredMixin, View):
    login_url = common_lib.DEFAULT_REDIRECT_PATH['ROOT']
    def get(self,request,action,id):
        response_record = Response.objects.get(id=id)
        request_record = response_record.requests
        r_id=request_record.id
        ServiceRequests.objects.filter(id=r_id).update(status=False)
    
        response_record.delete()
        return HttpResponseRedirect('/WorkerpendingTask')

        