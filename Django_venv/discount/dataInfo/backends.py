from .models import Customer,Staff
from django.conf import settings
# when AuthBackend is called ?
# answer: it is called in login method.authenticate()
# what is object?
class CustomerAuthBackend(object):
    # question 1: where to call the authenticate method?(solved)
    # answer: it is called in login method.authenticate()
    # Tip: http://stackoverflow.com/questions/23095951/django-authentication-backends-import-error
    # For example:
    # def login(request):
    #   discover username and password
    #   authenticate(username=username, password=password, request=request)
    #   continue as normal

    # question 2: where username and password come from?(solved)
    # answer: parameters pass from login method
    def authenticate(self, name=None, password=None):
        try:
            # TODO : check User is None
            user = Customer.objects.get(name=name)
            # why return user at this place?
            # return user

            # question 1: where the password is got from ?
            # answer: from login 
            # question 2: how authenticate work and be called? 
            # answer: from login
            # question 3: How can I know password is mathced
            # answer:  1. getattr(model, field_name) (solved)
            #          2. user._meta.get_field('password') (may not)
            #          
            
            # Issue: not sure the type of getattr(user,'password') and password is matched
            if password == getattr(user,'password'):
                # Authentication success by returning the user
                # activate user
                user.is_active = True
                # print "is_active: %s" %user.is_active
                return user
            else:
                # Authentication fails if None is returned
                return None
        except Customer.DoesNotExist:
            return None
    # question: how can I pass the user_id as a paramter?    
    # answer: request part that is from parmeter of login view.
    def get_user(self, user_id):
        try:
            return Customer.objects.get(pk=user_id)
        # TODO: may delete
        except Customer.DoesNotExist:
            return None

class StaffAuthBackend(object):
    
    def authenticate(self, name=None, password=None):
        try:
            # TODO : check User is None
            user = Staff.objects.get(name=name)
            
            if password == getattr(user,'password'):
                
                Staff.is_active = True
                
                return user
            else:

                return None
        except Staff.DoesNotExist:
            return None
    # purpose to Use get_user()
    def get_user(self, user_id):
        try:
            return Staff.objects.get(pk=user_id)
        # TODO: may delete
        except Staff.DoesNotExist:
            return None



