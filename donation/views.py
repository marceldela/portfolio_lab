from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.db.models import Sum, Count
from django.forms import MultipleChoiceField
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import auth, messages

from donation.forms import CustomUserCreationForm, EditProfileForm
from donation.models import Donation, Institution, Category



class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('/')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Error wrong mail/password')
        return redirect('/')


class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated:
            auth.logout(request)
        return render(request, 'logout.html')

class RegisterView(View):
    def get(self, request):
        form = CustomUserCreationForm()
        return render(request, 'register.html', {'form': form})

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")


class IndexView(View):

   def get(self, request,):
        quantities = Donation.objects.aggregate(Sum('quantity'))['quantity__sum']
        institutions = Donation.objects.aggregate(sum=Count('institution_id', distinct=True))

        fundations = Institution.objects.filter(type='FUNDACJA')
        paginator = Paginator(fundations, 5)
        page = request.GET.get('page')
        fundationsp = paginator.get_page(page)

        organizations = Institution.objects.filter(type='ORGANIZACJA POZARZĄDOWA')
        paginatororg = Paginator(organizations, 5)
        p = request.GET.get('p')
        poo = paginatororg.get_page(p)

        locals = Institution.objects.filter(type='ZBIÓRKA LOKALNA')
        paginatorloc = Paginator(locals, 5)
        pp = request.GET.get('pp')
        localsp = paginatorloc.get_page(pp)

        return render(request, 'index.html', {'quantities': quantities, 'institutions': institutions,
                                              'fundationsp': fundationsp, 'fundations':fundations,
                                              'organizations': organizations, 'locals': locals,
                                              'sp': poo, 'localsp': localsp})





class UserView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        donations = Donation.objects.filter(user=user)
        return render(request, 'user.html', {'user': user, 'donations': donations})

class EditProfile(View):
    def get(self, request):
        user = request.user
        return render(request, 'edit_profile.html', {'user': user})

    def post(self, request):
        user = request.user
        success = user.check_password(request.POST.get('password'))
        if success:
            user.email = request.POST.get('username')
            user.first_name = request.POST.get('first_name')
            user.last_name = request.POST.get('last_name')
            user.save()
            message = 'Dane zostały pomyślnie zmienione'
        else:
            message = 'Wprowadź poprawne hasło'
        return render(request, 'edit_profile.html', {'user': user, 'message': message})

class ChangePassword(View):
    def get(self, request):
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {'form': form})

    def post(self, request):
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect(reverse_lazy('edit_profile'))

class FormView(View):
    def get(self, request):
        if request.user.is_authenticated:
            categories = Category.objects.all()
            institutions = Institution.objects.all()
            return render(request, 'form.html', {'categories': categories,
                                                 'institutions': institutions})
        return redirect(reverse_lazy('login'))

    def post(self, request):
        quantity = request.POST.get('bags')
        category = request.POST.getlist('category')
        institution = Institution.objects.get(pk=request.POST.get('organization'))
        address = request.POST.get('address')
        phone_number = request.POST.get('phone')
        city = request.POST.get('city')
        zip_code = request.POST.get('postcode')
        pick_up_date = request.POST.get('date')
        pick_up_time = request.POST.get('time')
        pick_up_comment = request.POST.get('more_info')
        user = User.objects.get(pk=request.user.id)
        donation = Donation.objects.create(quantity=quantity, institution=institution,
                                           address=address, phone_number=phone_number, city=city, zip_code=zip_code,
                                           pick_up_date=pick_up_date, pick_up_time=pick_up_time,
                                           pick_up_comment=pick_up_comment,
                                           user=user)
        donation.save()
        for element in category:
            donation.categories.add(element)
        return redirect("/donation_confirmed/")

class DonationConfirmation(View):
    def get(self, request):
        return render(request, 'form-confirmation.html')










