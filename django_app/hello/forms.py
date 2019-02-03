from django import forms
from.models import Friend
from.models import ANKENTBL
# from.models import Friend,ANKENTBL,ICHIRANTBL,USERTBL,HYOKATBL,KOUMOKUM
#from django.contrib.auth.models import User


class HelloForm(forms.Form):

    name = forms.CharField(label='Name')
    mail = forms.CharField(label='Email')
    gender = forms.BooleanField(label='Gender', required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']

# ----START


class ANKENTBLForm(forms.ModelForm):
    class Meta:
        model = ANKENTBL
        fields = ['ANKENID', 'ANKENNM', 'CONTENTS', 'REQUESTDATE',
                  'RECRUITDATE', 'MINPAY', 'MAXPAY', 'DELIVE', 'HTUID', 'STID']

# class ANKENDTLTBLForm(forms.ModelForm):
#     class Meta:
#         model = ANKENDTLTBL
#         fields = ['ANKENDTLID','CONTENTS','MINPAY','MAXPAY',\
#                   'DELV','HTUID','JYUID','MIDFILENM','MDCOMMENT','MDMONEY','FNLFILENM',\
#                   'FNLCOMMENT','FNLMONEY']

# class ICHIRANTBLForm(forms.ModelForm):
#     class Meta:
#         model = ICHIRANTBL
#         fields = ['ANKENID','JYUID','HTUID','STID']

# class USERTBLForm(forms.ModelForm):
#     class Meta:
#         model = USERTBL
#         fields = ['USERID','USERNM','PASS','NAME','BIRTHDAY','TEL','UNIV','ADDRESSID','WORKID',\
#                   'FREESPACE','MAIL','RANKID']

# class HYOKATBLForm(forms.ModelForm):
#     class Meta:
#         model = HYOKATBL
#         fields = ['ANKENID','HTUID','JYUID','LINE','HYOUKARK','HYOUKACMID','HYOUKACM']

# class KOUMOKUMForm(forms.ModelForm):
#     class Meta:
#         model = KOUMOKUM
#         fields = ['ITEMID','ITEMNM']

# class mainForm(forms.Form):
#     main = form.CharField(label='一覧出力',)
