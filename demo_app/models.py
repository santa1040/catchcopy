from django.db import models

class SkatList(models.Model):

    # DBのカラムに相当する部分の定義
    company = models.CharField('名字', max_length=30)
    page = models.IntegerField('ページ', default=0)
    award = models.CharField('受賞', max_length=10)
    name = models.CharField('名前', max_length=10)
    adress = models.CharField('都道府県', max_length=5)
    copy1 = models.CharField('コピー（改行あり）', max_length=200)
    copy2 = models.CharField('コピー（改行なし）', max_length=200)

    # def __str__(self):
    #     return self.company, self.award, self.copy2