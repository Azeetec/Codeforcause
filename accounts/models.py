from django.db import models
from django.contrib.auth.models import PermissionsMixin,UserManager
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import RegexValidator
from django.core import validators
import re
from django.utils.translation import gettext as _
from django.contrib.auth.base_user import BaseUserManager
import uuid



# Create your models here.

class Master_Role(models.Model):
    class Meta:
        db_table = 'master_role'
    id         = models.AutoField(primary_key=True)
    role_name  = models.CharField(max_length=50, null=True, blank=True)
    is_active  = models.BooleanField(('active'), default=True )
    is_deleted = models.BooleanField(('delete'), default=False)

    def __str__(self):
        return self.role_name


class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
       db_table = "auth_user"

    id = models.UUIDField(primary_key = True,default = uuid.uuid4 ,editable = False)
    username = models.CharField(_('username'), max_length=75, unique=True, help_text=_('Required. 30 characters or fewer. Letters, numbers and @/./+/-/_ characters'), validators = [ validators.RegexValidator(re.compile('^[\w.@+-]+$'), _('Enter a valid username.'), 'invalid') ])
    first_name = models.CharField(('first_name'),validators=[RegexValidator("^[a-zA-Z]{1,50}")], max_length=50, null=True,blank=True)
    last_name = models.CharField(('last_name'),validators=[RegexValidator("^[a-zA-Z]{1,50}")], max_length=50,null=True,blank=True)
    email = models.EmailField(max_length=70,blank=True, null= True, unique= True)
    is_staff = models.BooleanField(default=0)
    is_active = models.BooleanField(('active'), default=True, help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.'))
    phone = models.CharField(max_length=12, null=True,blank=True)
    role_instance = models.ForeignKey(Master_Role, on_delete = models.CASCADE, null = True, blank = True)
    image = models.ImageField(null= True ,blank = True,upload_to='users/')
    skills = models.CharField(max_length=1500,null=True,blank=True)
    description = models.TextField(null=True,blank=True)


    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True,)
    updated_on = models.DateTimeField(auto_now=True,blank=True, null=True,)

    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def get_full_name(self):
        return self.first_name+" "+self.last_name

    def get_short_name(self):
        return self.first_name

        
    def __unicode__(self):
        return self.email



class Project(models.Model):

    class Meta:
       db_table = "project_model"

    id = models.UUIDField(primary_key = True,default = uuid.uuid4 ,editable = False)
    title = models.CharField(max_length=50)
    description = models.TextField()
    user_instance = models.ForeignKey(User, on_delete = models.CASCADE)
    is_active = models.BooleanField(default = True)
    timeframe = models.CharField(max_length=50)
    is_deliver = models.BooleanField(default = False)
    files = models.FileField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True,)
    updated_on = models.DateTimeField(auto_now=True,blank=True, null=True,)



class ProjectBidders(models.Model):

    class Meta:
       db_table = "project_bidders"

    id = models.UUIDField(primary_key = True,default = uuid.uuid4 ,editable = False)
    user_instance = models.ForeignKey(User, on_delete = models.CASCADE)
    project_instance = models.ForeignKey(Project, on_delete = models.CASCADE)
    is_selected = models.BooleanField(default = False)
    timeframe = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True,)
    updated_on = models.DateTimeField(auto_now=True,blank=True, null=True,)
    description = models.TextField()



class OrderProjected(models.Model):

    class Meta:
       db_table = "order_projected"

    id = models.UUIDField(primary_key = True,default = uuid.uuid4 ,editable = False)
    user_instance = models.ForeignKey(User, on_delete = models.CASCADE)
    project_instance = models.ForeignKey(Project, on_delete = models.CASCADE)
    is_deliver = models.BooleanField(default = False)
    is_cancelled = models.BooleanField(default = False)
    files = models.FileField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True,blank=True, null=True,)
    updated_on = models.DateTimeField(auto_now=True,blank=True, null=True,)
    description = models.TextField()
    is_completed = models.BooleanField(default = False)
    is_revision = models.BooleanField(default = False)



class ThreadManager(models.Manager):
    '''Demonstrate docstring for informing that this python based function is used for making an thread and checking weather it is exist or not through websocket'''

    def by_user(self, user):
        qlookup = Q(first=user) | Q(second=user)
        qlookup2 = Q(first=user) & Q(second=user)
        qs = self.get_queryset().filter(qlookup).exclude(qlookup2).distinct()
        return qs

    def get_or_new(self, user, other_username): # get_or_create
        username = user.username
        if username == other_username:
            return None
        qlookup1 = Q(first__username=username) & Q(second__id=other_username)
        qlookup2 = Q(first__id=other_username) & Q(second__username=username)
        qs = self.get_queryset().filter(qlookup1 | qlookup2).distinct()
        print("qss", qs)
        if qs.count() == 1:
            return qs.first(), False
        elif qs.count() > 1:
            return qs.order_by('timestamp').first(), False
        else:
            Klass = user.__class__
            user2 = Klass.objects.get(id=other_username)
            print(user2)
            if user != user2:
                obj = self.model(
                        first=user, 
                        second=user2
                    )
                obj.save()
                return obj, True
            return None, False

class ParticularThread(models.Model):

    '''Demonstrate docstring for informing that this model is used for storing an thread of two user which two users are doing chat'''

    first        = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_thread_first')
    second       = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chat_thread_second')
    project_instance  = models.ForeignKey(Project, on_delete=models.CASCADE, null = True, blank = True)

    updated      = models.DateTimeField(auto_now=True)
    timestamp    = models.DateTimeField(auto_now_add=True)
    
    objects      = ThreadManager()

    @property
    def room_group_name(self):
        return f'chat_{self.id}'

    def broadcast(self, msg=None):
        if msg is not None:
            broadcast_msg_to_chat(msg, group_name=self.room_group_name, user='admin')
            return True
        return False


class ChatMessages(models.Model):

    '''Demonstrate docstring for informing that this model is used for storing an message and thread id of user and recruiter'''

    thread      = models.ForeignKey(ParticularThread, null=True, blank=True, on_delete=models.SET_NULL)
    user        = models.ForeignKey(User, verbose_name='sender', on_delete=models.CASCADE)
    message     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)
