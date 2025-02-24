import math
import time
import csv
import requests
import traceback


#----------------------------
#streamlit
#streamlit run app.py
#で起動
#----------------------------

import streamlit as st


st.title('さぷーアプリ')
st.caption('これはさぷーの動画用アプリです')

st.subheader('自己紹介')
st.text('pythonに関する需要法を発信しています\n'
'良ければチャンネル登録してください'
)

code='''
import streamlit as st

st.titile('サプーアプリ')
'''

st.code(code,language='python')

#=====================================================
#テキストボックス
name=st.text_input('名前')
#子の変数にテキストボックスに入力されている値を格納
#画面がリロードされたタイミングで取得

#ボタン
submit_btn=st.button('送信')
cancel_btn=st.button('キャンセル')
#ボタンが押されるとtrue,押されないとfalseを返す
#ボタンを押すとリロードされる
print(f'submit_btn:{submit_btn}')
print(f'cancel_btn:{cancel_btn}')

if submit_btn:
    st.text(f'ようこそ！ {name} さん')

#そのつどリロードは、入力項目が増えると時間がかかるにおで、
#たくさんある場合は、with句で、form を使う
#=====================================================

#with句formを使うと、form_submit_buttonが押されるまでリロードされない

with st.form(key='profile_form'):
    #テキストボックス
    name=st.text_input('名前')
    address=st.text_input('住所')

    #セレクトボックス 第1引数に項目目、第2引数にタプルで選択肢
    age_category=st.selectbox(
    '年齢層',
    ('子供（18歳未満）','大人（18歳以上)')
    )

    area_category=st.radio(
    'エリア選択',
    ('日本国内','国外')
    )

    #複数選択はマルチセレクト 戻り値は、選択分がリストで返される
    hobby=st.multiselect(
    '趣味',
    ('スポーツ','読書','プログラム','アニメ','散歩','アウトドア')
    )

    #ボタン
    submit_formbtn=st.form_submit_button('送信')
    cancel_formbtn=st.form_submit_button('キャンセル')

    if submit_formbtn:
        st.text(f'ようこそ！ {name} さん\n'
        f'住所：{address}ですね \n'
        f'年齢層：{age_category}ですね \n'
        f'エリア：{area_category}ですね \n'
        f'趣味：{",".join(hobby)}ですね ')
#=====================================================
