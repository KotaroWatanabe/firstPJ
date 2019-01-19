from django import forms
from.models import Friend,ANNKENTBL,ANNKENDTLTBL,ICHIRANTBL,USERTBL,HYOKATBL,KOUMOKUM
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
        fields = ['name','mail','gender','age','birthday']

#----START
        
class ANNKENTBLForm(forms.ModelForm):
    class Meta:
        model = ANNKENTBL
        fields = ['ANNKENID','ANNKENNM','ANNKENDTLID','REQUESTDATE','RECRUITDATE','USERID','STID']
    
class ANNKENDTLTBLForm(forms.ModelForm):
    class Meta:
        model = ANNKENDTLTBL
        fields = ['ANNKENDTLID','CONTENTS','MINPAY','MAXPAY',\
                  'DELV','HTUID','JYUID','MIDFILENM','MDCOMMENT','MDMONEY','FNLFILENM',\
                  'FNLCOMMENT','FNLMONEY']
        
class ICHIRANTBLForm(forms.ModelForm):
    class Meta:
        model = ICHIRANTBL
        fields = ['ANNKENID','JYUID','HTUID','STID']
        
class USERTBLForm(forms.ModelForm):
    class Meta:
        model = USERTBL
        fields = ['USERID','USERNM','PASS','NAME','BIRTHDAY','TEL','UNIV','ADDRESSID','WORKID',\
                  'FREESPACE','MAIL','RANKID']
        
class HYOKATBLForm(forms.ModelForm):
    class Meta:
        model = HYOKATBL
        fields = ['ANNKENID','HTUID','JYUID','LINE','HYOUKARK','HYOUKACMID','HYOUKACM']
        
class KOUMOKUMForm(forms.ModelForm):
    class Meta:
        model = KOUMOKUM
        fields = ['ITEMID','ITEMNM']
        
class mainForm(forms.Form):
    main = form.CharField(label='一覧出力',)
        









