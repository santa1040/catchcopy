from django.shortcuts import render,redirect # 　追加
from .forms import InputForm

import pandas as pd
import MeCab
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from .models import Customer

# データの読み込み
df = pd.read_csv('model/skat_data.csv')

# オプションに -Owakatiを使用
def wakati(word):
    mecab = MeCab.Tagger('-Owakati')
    # mecab = MeCab.Tagger('-d /app/.linuxbrew/lib/mecab/dic/ipadic')
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
        result.append([df.iloc[i[0]][6],  i[1]])
        rank += 1

    res1_copy = result[0][0]
    res1_sim = result[0][1]
    res2_copy = result[1][0]
    res2_sim = result[1][1]
    res3_copy = result[2][0]
    res3_sim = result[2][1]
    res4_copy = result[3][0]
    res4_sim = result[3][1]
    res5_copy = result[4][0]
    res5_sim = result[4][1]
    res6_copy = result[5][0]
    res6_sim = result[5][1]
    res7_copy = result[6][0]
    res7_sim = result[6][1]
    res8_copy = result[7][0]
    res8_sim = result[7][1]
    res9_copy = result[8][0]
    res9_sim = result[8][1]
    res10_copy = result[9][0]
    res10_sim = result[9][1]

    # 推論結果をHTMLに渡す
    return render(request, 'result.html', {'res1_copy':res1_copy,
                                            'res1_sim':res1_sim,
                                            'res2_copy':res2_copy,
                                            'res2_sim':res2_sim,
                                            'res3_copy':res3_copy,
                                            'res3_sim':res3_sim,
                                            'res4_copy':res4_copy,
                                            'res4_sim':res4_sim,
                                            'res5_copy':res5_copy,
                                            'res5_sim':res5_sim,
                                            'res6_copy':res6_copy,
                                            'res6_sim':res6_sim,
                                            'res7_copy':res7_copy,
                                            'res7_sim':res7_sim,
                                            'res8_copy':res8_copy,
                                            'res8_sim':res8_sim,
                                            'res9_copy':res9_copy,
                                            'res9_sim':res9_sim,
                                            'res10_copy':res10_copy,
                                            'res10_sim':res10_sim,
                                            'copy':document})