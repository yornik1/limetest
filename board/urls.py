from django.urls import path
from board.views import Board, CardEdit, SignUpView, CardCreate, delete_card, change_status

urlpatterns = [
    path('signup/', SignUpView.as_view(template_name='registration/signup.html'), name='signup'),
    path('board/', Board.as_view(), name='board'),
    path('', Board.as_view(), name='board'),
    path('card/edit/<pk>', CardEdit.as_view(), name='editcard'),
    path('card/create/', CardCreate.as_view(template_name='board/create.html'), name='addcard'),
    path('card/status/', change_status, name='status'),
    path('card/delete/', delete_card, name='delete'),
]
