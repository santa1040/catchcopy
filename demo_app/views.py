from django.shortcuts import render,redirect # 　追加
from .forms import InputForm

def index(request):
    return render(request, 'index.html')

def input_form(request):
    # 下記追加
    if request.method == "POST": # Formの入力があった時、、
        form = InputForm(request.POST) # 入力データの取得
        if form.is_valid(): # Formの記載の検証
            form.save() # 入力を保存
            return redirect('index') # indexのページを表示するように仮置き
    else:
        form = InputForm()
        return render(request, 'input_form.html', {'form':form})