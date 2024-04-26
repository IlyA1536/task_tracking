from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect


class UserIsOwnerMixin():
    def dispatch(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.creator != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        return redirect('tasks:login')
