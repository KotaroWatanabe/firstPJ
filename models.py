from django.db import models

# Create your models here.
class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()
    
    def __str__(self):
        return '<Friend:id=' +str(self.id) + ')>' +\
            self.name + '(' +str(self.age) +')>'    
    
#--------------------追記start
            
#----------------#
#案件テーブル      #
#----------------#
class ANNKENTBL(models.Model):
    ANNKENID = models.CharField( max_length=10)#案件ID(自動採番)   
    ANNKENNM = models.CharField( max_length=25)#案件名
    ANNKENDTLID = models.CharField( max_length=10)#案件詳細ID(自動採番)
#    REQUESTDATE = models.DateTimeField(auto_now_add=True)#掲載日
    REQUESTDATE = models.DateTimeField()#掲載日
    RECRUITDATE = models.DateTimeField()#掲載期限
    USERID = models.CharField( max_length=10)#発注ユーザーID
    STID = models.CharField( max_length=10)#ステータスID
      
    ##ここから下テキトー
    def __str__(self):
        return self.ANNKENID
    
#----------------#
#案件詳細テーブル   #
#----------------#
class ANNKENDTLTBL(models.Model):
    ANNKENDTLID = models.CharField( max_length=10)#案件詳細ID
    CONTENTS = models.CharField( max_length=500)#案件詳細内容
    MINPAY = models.IntegerField( default=100)#最低金額
    MAXPAY = models.IntegerField( default=10000)#最高金額
    DELV = models.DateTimeField()#納期
    HTUID = models.CharField( max_length=8)#発注者ID
    JYUID = models.CharField( max_length=8)#受注者ID
    MIDFILENM = models.CharField( max_length=30)#中間成果物ファイル名
    MDCOMMENT = models.CharField( max_length=200)#中間成果物コメント
    MDMONEY = models.IntegerField( default=3)#中間出来高(※初期値は3)
    FNLFILENM = models.CharField( max_length=30)#最終成果物ファイル名
    FNLCOMMENT = models.CharField( max_length=200)#最終成果物コメント
    FNLMONEY = models.IntegerField( default=3)#最終出来高(※初期値は3)
       
    ##ここから下テキトー
    def __str__(self):
        return self.ANKENDTLID
    
#-------------------#
#応募_候補一覧テーブル #
#-------------------#
class ICHIRANTBL(models.Model):
#    ANNKENID = models.CharField( max_length=10)#案件ID
    ANNKENID = models.ForeignKey(ANNKENTBL, on_delete=models.CASCADE)#案件ID    
    JYUID = models.CharField( max_length=8)#受注者ID
    HTUID = models.CharField( max_length=8)#発注者ID
    STID = models.CharField( max_length=10)#ステータスID
    
    ##ここから下テキトー
    def __str__(self):
        return self.ANNKENID
    
#----------------#
#ユーザーテーブル    #
#----------------#
class USERTBL(models.Model):
    USERID = models.CharField( max_length=8)#ユーザーID
    USERNM = models.CharField( max_length=10)#ユーザー名
    PASS = models.CharField( max_length=10)#パスワード
    COUNTRYID = models.IntegerField( default=0000000000)#国籍ID
    NAME = models.CharField( max_length=20)#氏名
    BIRTHDAY = models.DateTimeField()#生年月日
    TEL = models.IntegerField( default=00000000000000000000)#電話番号
    UNIV = models.CharField( max_length=20)#大学名
    ADDRESSID = models.IntegerField( default=0000000000)#居住地
    WORKID = models.IntegerField( default=0000000000)#職業
    FREESPACE = models.CharField( max_length=500)#自己紹介欄
    MAIL = models.CharField( max_length=50)#メールアドレス
    RANKID = models.CharField( max_length=1)#現在評価ランク
       
    ##ここから下テキトー
    def __str__(self):
        return self.USERID
       
#----------------#
#評価テーブル      #
#----------------#
class HYOKATBL(models.Model):
#    ANNKENID = models.CharField( max_length=10)#案件ID
    ANNKENID = models.ForeignKey(ANNKENTBL, on_delete=models.CASCADE)#案件ID    
#    HTUID = models.CharField( max_length=8)#発注者ID
    HTUID = models.ForeignKey(ICHIRANTBL, on_delete=models.CASCADE,\
                              related_name = HTUID)#発注者ID    
#    JYUID = models.CharField( max_length=8)#受注者ID
    JYUID = models.ForeignKey(ICHIRANTBL, on_delete=models.CASCADE,\
                              related_name = JYUID)#受注者ID    
    LINE = models.CharField( max_length=1)#方向
    HYOUKARK = models.CharField( max_length=1)#評価ランク
    HYOUKACMID = models.CharField( max_length=10)#評価コメントID(自動採番)
    HYOUKACM = models.CharField( max_length=500)#評価コメント
    
    ##ここから下テキトー
    def __str__(self):
        return self.ANNKENID
       
#----------------#
#項目マスタ        #
#----------------#
class KOUMOKUM(models.Model):
    ITEMID = models.CharField( max_length=10)#項目ID
    ITEMNM = models.CharField( max_length=100)#項目名
      
    ##ここから下テキトー
    def __str__(self):
        return self.ITEMID
    
    