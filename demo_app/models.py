from django.db import models
from datetime import date


# こちらでテーブルの中身を定義します
class Customer(models.Model):


    # DBのカラムに相当する部分の定義
    id = models.AutoField(primary_key=True)
    copy = models.CharField('キャッチコピー', max_length=3000)

    # # 管理画面に表示方法を定義：必須項目が入っているかどうかで表示内容を分ける
    # # %s:文字列,%d:数値
    # def __str__(self):
    #     if self.proba == 0.0:
    #         return self.copy
    #     else:
    #         return self.copy