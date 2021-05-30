import streamlit as st
import time
st.title('Streamlit入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(1,101):
  latest_iteration.text(f'Iteration {i}')
  bar.progress(i)
  time.sleep(0.1)

'Done!!'

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここ→絡む')

for i in range(1,6):
  expander = st.beta_expander('問合せ'+str(i))
  expander.write('解答' + str(i))
# option = st.text_input('貴方の趣味は？')
# condition=st.slider('あなたの調子は？',0,100,50)
# 'あなたの趣味は、',option,'です'
# 'コンディション：',condition
# if st.checkbox('Show Image'):
#   img = Image.open('hiroyuki.jpg')

#   st.image(img, caption='hiroyuki',use_column_width=True)


# """
# # 章
# ## 節
# ### 項
# Python
# import streamlit as st
# import numpy as np
# import pandas as pd
# """