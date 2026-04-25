import pandas as pd
import streamlit as st
import plotly.express as px
pd.set_option('display.max_columns',None)
pd.set_option('display.max_colwidth',None)
try:
    df=pd.read_excel("data.xlsx",engine="openpyxl")
    st.success("Excel读取成功！")
except Exception as e:
    st.error(f"读取Excel失败:{e}")
    st.stop()
df["D值"]=df["L"]*df["E"]*df["C"]
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
pd.set_option('display.width', 200)

    

def draw_pie(workshop_name):
    df_ws = df[df["电池工厂"] == workshop_name]
    level_counts = df_ws["危险等级"].value_counts().reset_index()
    level_counts.columns = ["危险等级", "数量"]
    fig = px.pie(level_counts, 
                 values="数量", 
                 names="危险等级", 
                 title=f"{workshop_name} 风险等级分布",
                 color="危险等级",
                 color_discrete_map={
                     "重大风险": "red",
                     "高度风险": "orange",
                
                     "一般风险": "blue",
                     "低风险": "green"
                 })
    st.plotly_chart(fig, use_container_width=True)
keyword=st.text_input("危险源：")
if keyword:
    result=df[df["危险源"].str.contains(keyword,na=False)]
    if result.empty:
        st.warning("待扩展....")
    else:          
        st.dataframe(result[["危险源","可能后果","危险等级","D值","控制措施"]])
else:
    st.info("请输入关键词")
workshops=["配料车间","涂布车间","辊压车间","分切车间","叠片车间","装配车间","注液车间","化成车间","分容车间","模组装配车间","PACK总装车间","电池包测试车间"]
cols = st.columns(4)
for i, ws in enumerate(workshops):
    with cols[i % 4]:
        if st.button(ws, use_container_width=True):
            draw_pie(ws)
