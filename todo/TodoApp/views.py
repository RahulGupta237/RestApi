from django.shortcuts import render,redirect, get_object_or_404
from TodoApp.serializers import UserRegistrationSerializer, UserLoginSerializer
from TodoApp.models import User,TodoList,Item
from TodoApp.forms import CustomUserForm,UserLogin, EditProfileForm,EditAdminProfileForm,TodoList,TodoListForm,ItemForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test


from django.contrib.auth import authenticate,login,logout

from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def user_signup(request):
    if request.method == 'GET':
        serializer = UserRegistrationSerializer()
        print("i am working rahul")
        is_admin = request.POST.get('id_admins')
        print("rahul",is_admin)
        return render(request,'UserApp/signup.html', {'forms':CustomUserForm()})
    elif request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)

        print("rahul",dict(request.data))
        

        if serializer.is_valid():
            serializer.save()

            print(serializer.data)
            return HttpResponseRedirect('login')
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return render(request,'UserApp/signup.html', {'forms':CustomUserForm()})
    


def xuser_signup(request):
    fm=CustomUserForm()

    if request.method=="POST":
        # fm=CustomUserForm(request.POST)
        fm = UserRegistrationSerializer(data=request.data)
        if fm.is_valid():
            fm.save()
            print("data successfullya saved")
            messages.success(request,"Congratullation your account successfully created")
            return HttpResponseRedirect('login')

    else:
        if request.user.is_authenticated:
            logout(request)
        else:
            fm=CustomUserForm()
            print("get the form data")

    return render(request,'UserApp/signup.html',{"forms":fm})

def user_login(request):

    fm=UserLogin()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)
        user = authenticate(request,email=email, password=password)
        print(user)
        if user is not None:
            print("i am login")
            # Authentication successful, log the user in
            login(request, user,backend='django.contrib.auth.backends.ModelBackend')
            print("i am login")
            print(request.user)
            messages.success(request,"successfully login")
            return HttpResponseRedirect('/profile/')
            # return redirect('home') # Redirect to home page or any other page
        else:
            # Authentication failed, show an error message
            print("you are fake")
            messages.error(request,f"wrong credential for {email}")
    else:
         
            fm=UserLogin()
            print("i am user")
    return render(request,"UserApp/login.html",{"forms":fm})
    return render(request, 'login.html')
def fguser_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/profile/')
    
    else:
        
        if request.method=='POST':
            fm=UserLogin(request.POST)
            print(fm)
            if fm.is_valid():
                uname=fm.cleaned_data['email']
                upass=fm.cleaned_data['password']
                print(uname,upass)
                user=authenticate(email=uname,password=upass)
                if user is not None:
                    #login(request,user)
                    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                    print("i am login rahul")
                    messages.success(request,"successfully login")
                    return HttpResponseRedirect('/profile/')
                else:
                    print("you are fake")
                    messages.error(request,f"wrong credential for {uname}")
        else:
            fm=UserLogin()
            print("i am user")
        return render(request,"UserApp/login.html",{"forms":fm})
@login_required
def user_profile(request):
  
    if request.user.is_authenticated:
        fm =CustomUserForm()
     
        return render(request,'UserApp/Home.html',{"name":request.user.name,'forms':fm})
    else:
        return HttpResponseRedirect('/login/')
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required
@api_view(['GET', 'POST'])
def add_user(request):
    user=User.objects.all()
    if request.method == 'GET':
        serializer = UserRegistrationSerializer()
        print("i am working rahul")
        is_admin = request.POST.get('id_admins')
        print("rahul",is_admin)
        return render(request,'UserApp/admin.html', {'forms':CustomUserForm(),"users":user})
    elif request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)

        print("rahul",dict(request.data))
        

        if serializer.is_valid():
            serializer.save()

            print(serializer.data)
            messages.success(request,"Successfullly user added")
            return redirect('add_user')
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            user=User.objects.all()
            return render(request,'UserApp/admin.html', {'forms':CustomUserForm(),"users":user})
    






@login_required
def user_edit_profile(request):
    if request.user.is_authenticated:
     
        if request.method=="POST":

               if request.user.is_superuser==True:
                fm=EditAdminProfileForm(request.POST,instance=request.user)
                user=User.objects.all()
                print("i am admin user",user)
            
               else:
                user=None
                fm =EditProfileForm(request.POST,instance=request.user)
                print("i am normal user")
               if fm.is_valid():
                   fm.save()
                   print("i am save admin user")
                   print(fm)
                   messages.success(request,"profile successfully edited")
                   return HttpResponseRedirect('/profile/')
        else:

            if request.user.is_superuser==True:
                fm=EditAdminProfileForm(instance=request.user)
                user=User.objects.all()
                print(user)
             
            else:

                fm=EditProfileForm(instance=request.user)
                user=None # if is not there show unbounded local error before assignment

        return render(request,'UserApp/edit_profile.html',{"name":request.user,'forms':fm,'users':user})
    else:
        return HttpResponseRedirect('/login/')
@login_required
def user_detail(request,id):
    if request.user.is_authenticated:
        pi=User.objects.get(pk=id)
        fm =EditAdminProfileForm(instance=pi)
        return render(request,'UserApp/user_detail.html',{'forms':fm})


    else:
        return HttpResponseRedirect('/login/')





# Helper function to check if user is admin
def is_admin(user):
    return user.is_superuser

# Create new TodoList
@login_required
def create_todo_list(request):
    form = TodoListForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.user = request.user
            todo_list.save()
            print("Success fully ")
            return redirect('List_todo')
    return render(request, 'UserApp/create_todo_list.html', {'forms': form})

@login_required
def create_item_list(request):
  
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.user = request.user
            todo_list.save()
            print("i am here")
            return redirect('items_todo')
    return render(request, 'UserApp/item_list_todo.html', {'forms': form})

# Edit TodoList
def edit_todo_list(request, id):
    todo_list = get_object_or_404(TodoList, pk=id)
    form = TodoListForm(request.POST or None, instance=todo_list)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('List_todo')
 
    return render(request, 'UserApp/create_todo_list.html', {'forms': form, 'todo_list': todo_list})

def edit_items_list(request, id):
    todo_list = get_object_or_404(Item, pk=id)
    form = ItemForm(request.POST or None, instance=todo_list)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,"Items of todolist successfully edited")
            if request.user.is_staff:
                return redirect('add_user')
            return redirect('items_todo')
 
    return render(request, 'UserApp/item_list_todo.html', {'forms': form, 'todo_list': todo_list})



# Delete TodoList
def delete_todo_list(request,id):
    todo_list = get_object_or_404(TodoList, pk=id)
    todo_list.delete()
    return redirect('List_todo')

# Delete Items of TodoList
def delete_item_list(request,id):
    todo_list = get_object_or_404(Item, pk=id)
    todo_list.delete()
    if request.user.is_staff:
        return redirect("add_user")
    return redirect('items_todo')


# Activate/Deactivate TodoList
@user_passes_test(is_admin)
def activate_deactivate_todo_list(request,id):
    todo_list = get_object_or_404(TodoList, pk=id)
    Flage="Successfully Activate"
    if todo_list.is_active:
        todo_list.is_active = False
        Flage= "Successfully DeActivate"
    else:
        todo_list.is_active = True
    todo_list.save()
    x=messages.success(request,f"sucess fully {Flage} ")
    return redirect(f"todo_user/{todo_list.user.id}")

@login_required
def todo_list(request):
    # user = User.objects.get(id=1)  # replace 1 with the ID of the user you want to retrieve the to-do list for

    todo_items = TodoList.objects.filter(user=request.user) # Retrieve all ToDoItem objects from the database
    context = {'todo_items': todo_items} # Create a context dictionary with the retrieved objects
    return render(request, 'UserApp/dashboard.html', context)


@login_required
def items_todo_list(request):
    todo_lists = TodoList.objects.filter(user_id=request.user.id)

# Retrieve all the Item objects associated with the TodoList objects above
    items = Item.objects.filter(todo__in=todo_lists)
    # todo_items = Item.objects.all() # Retrieve all ToDoItem objects from the database
    # todo_items = Item.objects.filter(user=request.user)
    context = {'todo_items':items} # Create a context dictionary with the retrieved objects
    return render(request, 'UserApp/itemsdashboard.html', context)



def xadd_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User created successfully.')
            return redirect('add_user')
    else:
         if request.user.is_superuser==True:
            form = CustomUserForm()

            user=User.objects.all()
            print("Hi i am super user ",user)
         else:
             
             form=None
             user=None

    return render(request, 'UserApp/admin.html', {"name":request.user,'forms': form, "users":user})

@login_required
def delete_user(request,id):
   
    if request.user.is_authenticated:
        user = get_object_or_404(User,pk=id)
        if request.method=='POST':
            user.delete()
            messages.success(request,'Successfully deleted')
            return redirect('add_user')

    else:
        return HttpResponseRedirect('/login/')

@login_required
def edit_user(request,id):
    user = get_object_or_404(User, pk=id)

    if request.method == 'POST':
        print(user.email)
        user.email = request.POST.get('email',user.email)
        user.name=request.POST.get('name',user.name)
        user.mobile_number=request.POST.get('mobile_number',user.mobile_number)
        user.save()
        # redirect to the user detail page or some other relevant page
        messages.success(request,"Sucessfully Updated")
        return redirect(add_user)
      
    else:
        form=CustomUserForm(instance=user)
    return render(request,'UserApp/signup.html', {'forms':CustomUserForm()})

    # render your template and pass the user object as a context variable
@login_required
def all_user_todoitems(request,id):
    x=TodoList.objects.filter(user__id=id)
    return render(request,"UserApp/dashboard.html",{"todo_items":x})
@login_required
def all_userItems_todoitems(request,id):
    todo_lists = TodoList.objects.filter(user_id=id)

# Retrieve all the Item objects associated with the TodoList objects above
    items = Item.objects.filter(todo__in=todo_lists)
    
    # x = Item.objects.all()
    return render(request,"UserApp/itemsdashboard.html",{"todo_items":items})


@user_passes_test(lambda u: u.is_superuser)
@login_required
def admin_todo_list(request,id):
   
    user = get_object_or_404(User, id=id)
    form = TodoListForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            todo_list = form.save(commit=False)
            todo_list.user = user
            todo_list.save()
            print("i am here of admin")
            print(f"Successfully add todo for {User.objects.get(id=id).name}")
            messages.success(request,f"Successfully add todo for {User.objects.get(id=id).name}")
            return redirect('add_user')
    return render(request, 'UserApp/user_todo_list.html', {'forms': form})

@user_passes_test(lambda u: u.is_superuser)
@login_required
def admin_items_todo_list(request,id):
    print(id)
   # Retrieve the TodoList objects associated with the user
    todo_list = get_object_or_404(TodoList,pk=id)
    print(todo_list)
    # user = get_object_or_404(TodoList, user__id=id)
    form = ItemForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            list = form.save(commit=False)
            list.todo = todo_list
            list.save()
            print("i am here of so sweets admin")
            print(f"Successfully add todo for {User.objects.get(id=id).name}")
            messages.success(request,f"Successfully add todo for {User.objects.get(id=id).name}")
            return redirect('add_user')
    return render(request, 'UserApp/user_iems_todo_list.html', {'forms': form})



# from django.contrib.auth.decorators import login_required
# from django.contrib.admin.views.decorators import staff_member_required
# from django.shortcuts import get_object_or_404, render
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
# from myapp.models import TodoList, Item
# from myapp.forms import ItemForm

# @staff_member_required(login_url=reverse_lazy('login'))
# @login_required
# def add_item_to_todolist(request, user_id, todolist_id):
#     # Retrieve the TodoList object associated with the specified user
#     todo_list = get_object_or_404(TodoList, user_id=user_id, id=todolist_id)

#     if request.method == 'POST':
#         form = ItemForm(request.POST)
#         if form.is_valid():
#             # Save the new Item object with the specified TodoList object
#             item = form.save(commit=False)
#             item.todo = todo_list
#             item.save()
#             return redirect('todolist_detail', user_id=user_id, todolist_id=todolist_id)
#     else:
#         form = ItemForm()

#     return render(request, 'add_item_to_todolist.html', {'form': form})