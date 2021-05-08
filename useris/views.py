from django.views.generic import FormView, ListView, UpdateView, DetailView, DeleteView
from useris.models import Users
from useris.forms import UserAddForm, UserForm


class UserView(ListView):
    model = Users
    template_name = "index_new.html"


class AddUserView(FormView):

    form_class = UserAddForm
    template_name = "add_user_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.save()

        response = super().form_valid(form)

        return response


class UserUpdateView(UpdateView):
    model = Users
    fields = ['name', 'email']
    template_name = 'edit_user_new.html'
    success_url = "/"


class GetUser(DetailView):
    model = Users
    template_name = 'get_user_new.html'


class UserDeleteView(DeleteView):
    model = Users
    template_name = 'delete_user_new.html'
    success_url = "/"