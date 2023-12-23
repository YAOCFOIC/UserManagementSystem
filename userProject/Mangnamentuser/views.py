from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LogoutView
from .forms import CustomerCreateForm, CustomUserChangeForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from account.models import CustomUser
from django.core.paginator import Paginator
from reportlab.pdfgen import canvas
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, UserUpdateSerializer

# Create your views here.
def index(request):
    return render(request,'index.html')

def register_view(request):
    data = {
        'form': CustomerCreateForm()
    }
    if request.method == 'POST':
        send_form = CustomerCreateForm(data=request.POST)
        if send_form.is_valid():
            send_form.save()
            user = authenticate(username=send_form.cleaned_data["username"],password=send_form.cleaned_data["password1"])
            login(request, user)
            #messages.success(request,"Success Register")
            return redirect(to="home")
        data["form"] = send_form
    return render(request,"registration/register.html",data)

@method_decorator(login_required, name='dispatch')
class HomeView(ListView):
    model = CustomUser
    template_name = 'apps/home.html'
    context_object_name = 'users'
    paginate_by = 1
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return CustomUser.objects.filter(Q(username__icontains=query) | Q(email__icontains=query))
        return CustomUser.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_customer'] = CustomerCreateForm()
        paginator = context['paginator']
        page = context['page_obj']
        context['query'] = self.request.GET.get('q', '')

        context['users'] = page
        return context 
    
    def generate_pdf(self, user):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{user.username}_profile.pdf"'

        p = canvas.Canvas(response)
        p.drawString(100, 800, f"Username: {user.username}")
        p.drawString(100, 780, f"First Name: {user.first_name}")
        p.drawString(100, 760, f"Last Name: {user.last_name}")
        p.drawString(100, 740, f"Email: {user.email}")
        p.drawString(100, 720, f"Phone: {user.phone}")
        p.drawString(100, 700, f"Address: {user.address}")
        p.showPage()
        p.save()

        return response

    def render_to_response(self, context, **response_kwargs):
        if 'pdf' in self.request.GET:
            user_id = self.request.GET.get('pdf')
            user = CustomUser.objects.get(pk=user_id)
            return self.generate_pdf(user)
        return super().render_to_response(context, **response_kwargs)
    
@login_required
def edit_user(request, user_id):
    user = get_object_or_404(CustomUser, pk=user_id)

    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario editado exitosamente.')
            return redirect('home')
    else:
        form = CustomUserChangeForm(instance=user)

    return render(request, 'apps/home.html', {'form': form, 'user': user})

class UserListView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserUpdateView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserUpdateSerializer
    permission_classes = [IsAuthenticated]

