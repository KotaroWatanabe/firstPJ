from django.db import models

# Create your models here.


class Friend(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    gender = models.BooleanField()
    age = models.IntegerField(default=0)
    birthday = models.DateField()

    def __str__(self):
        return '<Friend:id=' + str(self.id) + ')>' +\
            self.name + '(' + str(self.age) + ')>'

# --------------------追記start

#----------------#
#項目マスタ        #
#----------------#


class KOUMOKUM(models.Model):
    ITEMID = models.CharField(max_length=10)  # 項目ID
    ITEMNM = models.CharField(max_length=100)  # 項目名

    # ここから下テキトー
    def __str__(self):
        return self.ITEMID

#----------------#
#ユーザーテーブル    #
#----------------#


class USERTBL(models.Model):
    USERID = models.CharField(max_length=8)  # ユーザーID
    USERNM = models.CharField(max_length=10)  # ユーザー名
    PASS = models.CharField(max_length=10)  # パスワード
    COUNTRYID = models.ForeignKey(KOUMOKUM, on_delete=models.CASCADE,
                                  related_name='KOUMOKUM_COUNTRY')  # 国籍ID
    NAME = models.CharField(max_length=20)  # 氏名
    BIRTHDAY = models.DateTimeField()  # 生年月日
    TEL = models.IntegerField(default=00000000000)  # 電話番号
    UNIV = models.CharField(max_length=20)  # 大学名
    ADDRESSID = models.ForeignKey(KOUMOKUM, on_delete=models.CASCADE,
                                  related_name='KOUMOKUM_ADDRESS')  # 居住地ID
    WORKID = models.ForeignKey(KOUMOKUM, on_delete=models.CASCADE,
                               related_name='KOUMOKUM_WORK')  # 職業ID
    FREESPACE = models.CharField(max_length=500)  # 自己紹介欄
    MAIL = models.EmailField(max_length=50)  # メールアドレス
    RANKID = models.CharField(max_length=1)  # 現在評価ランク

    # ここから下テキトー
    def __str__(self):
        return self.USERID

#----------------#
#案件テーブル      #
#----------------#


class ANKENTBL(models.Model):
    ANKENID = models.CharField(max_length=10)  # 案件ID(自動採番)
    ANKENNM = models.CharField(max_length=25)  # 案件名
    CONTENTS = models.CharField(max_length=500)  # 案件詳細内容
    REQUESTDATE = models.DateTimeField(auto_now_add=True)  # 掲載日
    RECRUITDATE = models.DateTimeField()  # 掲載期限
    MINPAY = models.IntegerField(default=100)  # 最低金額
    MAXPAY = models.IntegerField(default=10000)  # 最高金額
    DELIVE = models.DateTimeField()  # 納期
    MIDFILENM = models.CharField(max_length=30)  # 中間成果物ファイル名
    MDCOMMENT = models.CharField(max_length=200)  # 中間成果物コメント
    MDMONEY = models.IntegerField(default=3)  # 中間出来高(※初期値は3)
    FNLFILENM = models.CharField(max_length=30)  # 最終成果物ファイル名
    FNLCOMMENT = models.CharField(max_length=200)  # 最終成果物コメント
    FNLMONEY = models.IntegerField(default=3)  # 最終出来高(※初期値は3)
    HTUID = models.ForeignKey(USERTBL, on_delete=models.CASCADE,
                              related_name='ANKENTBL_HTUID')  # 発注ユーザーID
    JYUID = models.ForeignKey(USERTBL, on_delete=models.CASCADE,
                              related_name='ANKENTBL_JYUID')  # 受注者ID
    STID = models.ForeignKey(KOUMOKUM, on_delete=models.CASCADE)  # ステータスID

    # ここから下テキトー
    def __str__(self):
        return self.ANKENID

#----------------#
#案件詳細テーブル   #
#----------------#
# class ANKENDTLTBL(models.Model):
#     ANKENDTLID = models.OneToOneField(ANKENTBL, )#案件詳細ID
#     CONTENTS = models.CharField( max_length=500)#案件詳細内容
#     MINPAY = models.IntegerField( default=100)#最低金額
#     MAXPAY = models.IntegerField( default=10000)#最高金額
#     DELIVE = models.DateTimeField()#納期
#     HTUID = models.CharField( max_length=8)#発注者ID
#     JYUID = models.CharField( max_length=8)#受注者ID
#     MIDFILENM = models.CharField( max_length=30)#中間成果物ファイル名
#     MDCOMMENT = models.CharField( max_length=200)#中間成果物コメント
#     MDMONEY = models.IntegerField( default=3)#中間出来高(※初期値は3)
#     FNLFILENM = models.CharField( max_length=30)#最終成果物ファイル名
#     FNLCOMMENT = models.CharField( max_length=200)#最終成果物コメント
#     FNLMONEY = models.IntegerField( default=3)#最終出来高(※初期値は3)

    # ここから下テキトー
    # def __str__(self):
    #     return self.ANKENDTLID

#-------------------#
#応募_候補一覧テーブル #
#-------------------#


class ICHIRANTBL(models.Model):
    ANKENID = models.ForeignKey(ANKENTBL, on_delete=models.CASCADE)  # 案件ID
    HTUID = models.ForeignKey(USERTBL, on_delete=models.CASCADE,
                              related_name='ICHIRANTBL_HTUID')  # 発注ユーザーID
    JYUID = models.ForeignKey(USERTBL, on_delete=models.CASCADE,
                              related_name='ICHIRANTBL_JYUID')  # 受注者ID
    STID = models.ForeignKey(KOUMOKUM, on_delete=models.CASCADE)  # ステータスID

    # ここから下テキトー
    def __str__(self):
        return self.ANKENID

#----------------#
#評価テーブル      #
#----------------#


class HYOKATBL(models.Model):
    ANKENID = models.ForeignKey(ANKENTBL, on_delete=models.CASCADE)  # 案件ID
    HTUID = models.ForeignKey(ICHIRANTBL, on_delete=models.CASCADE,
                              related_name='HYOKATBL_HTUID')  # 発注者ID
    JYUID = models.ForeignKey(ICHIRANTBL, on_delete=models.CASCADE,
                              related_name='HYOKATBL_JYUID')  # 受注者ID
    LINE = models.CharField(max_length=1)  # 方向
    HYOUKARK = models.CharField(max_length=1)  # 評価ランク
    HYOUKACMID = models.CharField(max_length=10)  # 評価コメントID(自動採番)
    HYOUKACM = models.CharField(max_length=500)  # 評価コメント

    # ここから下テキトー
    def __str__(self):
        return self.ANKENID
