from django.db import models


#各属性の制約は未実装
#間に合わせでかなり雑に定義しています
class User(models.Model):
    username = models.CharField(max_length=100)
    userID = models.CharField(max_length=100, primary_key=True)
    password = models.CharField(max_length=100)
    class Meta:
        db_table = 'ユーザ表'  #テーブル名："ユーザ表"
        
    def __str__(self):
        return self.userID
    
#verbose_nameで項目の名前を指定できる
#日付の入力形式は未実装
class Ledger(models.Model):
    fileID = models.BigIntegerField(primary_key=True)
    userID = models.ForeignKey(User, blank=True, null=True, verbose_name='user', on_delete=models.PROTECT)
    attachedField = models.CharField('属性', max_length=100)   #5パターンのいずれかに変更すべし
    
    IS_USED_CHOICES = (
        (False, '請求書'),
        (True, '領収書'),
    )
    #請求書、領収書の種別
    category = models.BooleanField('種別', choices=IS_USED_CHOICES, help_text='請求書ならfalse')
    
    input_date = models.DateField('日付', blank=True,null=True)
    client = models.CharField('相手先', max_length=100)#全角文字指定に変更すべし
    consumptionTax_rate = models.PositiveIntegerField('消費税率', default=10)
    consumptionTax = models.PositiveIntegerField('消費税', default=0)
    excludingTax = models.PositiveIntegerField('税抜金額', default=0)
    includingTax = models.PositiveIntegerField('税込金額', default=0)
#     note = models.TextField('備考', blank=True, null=True, max_length=1000, verbose_name='備考')
    registration_date = models.DateField('登録日時', blank=True,null=True)
    approval_date = models.DateField('承認日時', blank=True,null=True)
    image_url = models.URLField('画像url', blank=True, null=True)
    
    
    class Meta:
        db_table = '帳簿表'
    
#     def __str__(self):
#         return self.fileID

class RelatedDocument(models.Model):
    relatedFileID = models.BigIntegerField( primary_key=True)
    userID = models.ForeignKey(User, blank=True, null=True, verbose_name='user', on_delete=models.PROTECT)
    image_url = models.URLField('画像url', blank=True, null=True)
    
    class Meta:
        db_table = '関係書類表'  #テーブル名："ユーザ表"
        
#     def __str__(self):
#         return self.relatedFileID


class Shop(models.Model):
    name = models.CharField(max_length=100)
    shop_site= models.URLField(blank=True,null=True)
    
    def __str__(self):
        return self.name
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    item_url= models.URLField(blank=True,null=True)
    count = models.PositiveIntegerField(default=0)
    buy_date= models.DateField(blank=True,null=True)
    shop = models.ForeignKey(Shop,blank=True,null=True,verbose_name='shop', on_delete=models.PROTECT)
    buy = models.BooleanField(default=False)

    def __str__(self):
        return '{} ({})'.format(self.name, self.buy_date)
    