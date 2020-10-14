from django.shortcuts import render,redirect # 　追加
from .forms import InputForm

# import joblib
import numpy as np
import pandas as pd
import MeCab
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from .models import Customer

# データの読み込み
df = pd.read_csv('model/skat_data.csv')

# オプションに -Owakatiを使用
def wakati(word):
    mecab = MeCab.Tagger('-Owakati')
    text = mecab.parse(word)
    ret = text.strip().split()
    return ret

# モデルの読み込み
model = Doc2Vec.load('model/doc2vec.model')

def index(request):
    return render(request, 'index.html')

def input_form(request):
    # 下記追加
    if request.method == "POST": # Formの入力があった時、、
        form = InputForm(request.POST) # 入力データの取得
        if form.is_valid(): # Formの記載の検証
            form.save() # 入力を保存
            return redirect('result') # indexのページを表示するように仮置き
    else:
        form = InputForm()
        return render(request, 'input_form.html', {'form':form})


def result(request):

    # 最新の登録者のデータを取得
    data = Customer.objects.order_by('id').reverse().values_list('copy') # 学習させたカラムの順番

    document = data[0][0]

    rank = 1
    result = []

    for i in model.docvecs.most_similar([model.infer_vector(wakati(document))]):
        result.append(['第{}位'.format(rank),  i[1], df.iloc[i[0]][6], 'ID:{}'.format(i[0])])
        rank += 1
    df_result = pd.DataFrame(result, columns=['順位','類似度','キャッチコピー','ID'])

    # 推論結果をHTMLに渡す
    return render(request, 'result.html', {'df_result':df_result, 'copy':document})