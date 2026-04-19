import pandas as pd
import streamlit as st
pd.set_option('display.max_columns',None)
pd.set_option('display.max_colwidth',None)
df=pd.read_excel("data.xlsx",engine="openpyxl")

df["D值"]=df["L"]*df["E"]*df["C"]
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 200)

keyword=st.text_input("危险源：")
result=df[df["危险源"].str.contains(keyword,na=False)]
if result.empty:
    print("待扩展....")
else:          
    print(result[["危险源","可能后果","危险等级","D值","控制措施"]])

