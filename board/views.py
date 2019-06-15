from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from board.models import Card
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from board.forms import SignUpForm


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/login/'


class Board(LoginRequiredMixin, ListView):
    model = Card


class CardEdit(LoginRequiredMixin, UpdateView):
    model = Card
    fields = '__all__'
    success_url = '/board/'


class CardCreate(LoginRequiredMixin, CreateView):
    model = Card
    fields = '__all__'
    success_url = '/board/'


@login_required
def change_status(request):
    try:
        card = Card.objects.get(id=request.POST.get('id', 0))
    except Exception as e:
        return JsonResponse({'success': '0'})
    else:
        card.status = request.POST.get('status')
        card.save()
        return JsonResponse({'success': '1'})


@login_required
def delete_card(request):
    try:
        card = Card.objects.get(id=request.POST.get('id', 0))
    except Card.DoesNotExist:
        return JsonResponse({'success': '0'})
    else:
        card.delete()
        return JsonResponse({'success': '1'})
