import pandas as pd
import requests
import io
from openpyxl import load_workbook
import streamlit as st # pip install streamlit

df = pd.read_excel('/content/DAN_Empty.xlsx')

file2 = st.file_uploader('Upload Book file ', type='xlsx')
file3 = st.file_uploader('Upload Clinics type file', type = 'xlsx')

if file2 and file3 :
  book = pd.read_excel(file2)
  f = pd.read_excel(file3)
  st.success('تم رفع الملفات بنجاح')

  merged_data = pd.merge(book, f, on='CLINIC_NAME', how='left')
  date_col_name = merged_data.columns[2]
  merged_data[date_col_name] = pd.to_datetime(merged_data[date_col_name]).dt.strftime('%d/%m/%y')

  rows_count = len(merged_data)
  df.iloc[:rows_count,0] = merged_data.iloc[:,0].values
  df.iloc[:rows_count,1]= 'Speciality Clinics'
  df.iloc[:rows_count,2] = merged_data.iloc[:,4].values
  df.iloc[:rows_count,3] = merged_data.iloc[:,5].values
  df.iloc[:rows_count,4] = merged_data.iloc[:, 2].values
  df.iloc[:rows_count, 5] = merged_data.iloc[:, 3].replace({'F': 'Follow up', 'N': 'New'}).values
  df.iloc[:rows_count,6] = 'No'
  df.iloc[:rows_count,7] = ''
  df.iloc[:rows_count,8] = 'Yes'
  df.iloc[:rows_count,9] = 'Other'

  st.write('النتيجة النهائية')
  st.dataframe(df.head())

  st.download_button(label='تحميل الملف القابل للنسخ ')
  data = df.to_excel('Ready_to_Copy.xlsx', index=False, header=False)




