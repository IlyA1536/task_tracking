from django.shortcuts import redirect, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, View
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils import timezone
from tasks.models import Task, Comment
from tasks.forms import Task, TaskForm, TaskFilterForm, Comment, CommentForm
from tasks.mixins import CustomLoginRequiredMixin, UserIsOwnerMixin


class TasksListView(ListView):
    model = Task
    context_object_name = "tasks"
    template_name = "tasks/tasks_list.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get("status", "")
        priority = self.request.GET.get("priority", "")

        if status:
            queryset = queryset.filter(status=status)

        if priority:
            queryset = queryset.filter(priority=priority)

        return queryset.order_by('status', 'priority')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskFilterForm(self.request.GET)
        return context


class TaskDetailView(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "tasks/task_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm
        context['large_number'] = 12345.67
        context['current_date'] = timezone.now()
        return context

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST, request.FILES)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.task = self.get_object()
            comment.save()
            return redirect('tasks:task-detail', pk = comment.task.pk)
        else:
            raise ValidationError("Bad input")


class TaskCreateView(CustomLoginRequiredMixin, CreateView):
    model = Task
    template_name = "tasks/task_create.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:tasks-list")

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskDeleteView(CustomLoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:tasks-list")


class TaskUpdateView(CustomLoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:tasks-list")


class TaskCompleteView(View):
    model = Task

    def get_object(self):
        task_id = self.kwargs.get("pk")
        return get_object_or_404(Task, pk=task_id)

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        task.status = "done"
        task.save()
        return HttpResponseRedirect(reverse_lazy('tasks:tasks-list'))


class CommentUpdateView(CustomLoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Comment
    fields = ['content']

    def form_valid(self, form):
        comment = self.get_object()
        if comment.author == self.request.user:
            return super().form_valid(form)
        raise PermissionError('You do not have permissions')

    def get_success_url(self):
        return reverse_lazy('tasks:task-detail', kwargs={'pk': self.object.task.id})


class CommentDeleteView(CustomLoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Comment

    def get_success_url(self):
        return reverse_lazy('tasks:task-detail', kwargs={'pk': self.object.task.id})


class CustomLoginView(LoginView):
    template_name = "tasks/login.html"
    redirect_authenticated_user = True


class CustomLogoutView(LogoutView):
    next_page = "tasks:login"


class RegisterView(CreateView):
    template_name = "tasks/register.html"
    form_class = UserCreationForm

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(reverse_lazy("tasks:login"))
