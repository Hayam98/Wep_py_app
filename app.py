import streamlit as st
import pandas as pd

st.write('# Excel Processor')

# واجهة لرفع الملفات الثلاثة
file1 = st.file_uploader('ارفع الملف الأول', type='xlsx')
file2 = st.file_uploader('ارفع الملف الثاني', type='xlsx')
file3 = st.file_uploader('ارفع الملف الثالث', type='xlsx')

# نتأكد إن المستخدم رفع كل الملفات قبل ما نبدأ
if file1 and file2 and file3:
    # قراءة الملفات وتحويلها إلى DataFrames
    df1 = pd.read_excel(file1)
    df2 = pd.read_excel(file2)
    df3 = pd.read_excel(file3)
    
    st.success('تم رفع جميع الملفات بنجاح!')
    
    # هنا تقدرين تعرضين جزء من البيانات عشان تتأكدين
    st.write('### معاينة بيانات الملف الأول:')
    st.dataframe(df1.head()) 
    
    # هنا تحطين الكود حقك اللي يدمجهم (مثل كود دمج بيانات المرضى اللي اشتغلتي عليه)
    # result = df1.merge(df2, on='ID') ... إلخ
