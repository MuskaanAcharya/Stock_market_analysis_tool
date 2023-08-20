import streamlit as st
import pandas as pd
import mysql.connector
import datetime

cnx = mysql.connector.connect(
    host='127.0.0.1',
    database='stock5',
    user='root',
    password='root',
    auth_plugin='mysql_native_password'
)
cursor = cnx.cursor()

base_query = """
    SELECT d.id, d.FinInstrmNm, d.TckrSymb, f.dstock_id, f.TradDt, f.OpnPric, f.HghPric, f.LwPric, f.ClsPric, f.LastPric             
    FROM d_stock AS d
    INNER JOIN f_stock AS f ON d.id = f.dstock_id
"""

cursor.execute(base_query)
data = cursor.fetchall()
columns = [desc[0] for desc in cursor.description]

df = pd.DataFrame(data, columns=columns)

st.title("📈 Stock Market Tool")

font_style = "font-family: Arial, sans-serif;"
font_size = "font-size: 20px;"

st.sidebar.title("📊 Stock Name")
st.sidebar.markdown(f"<p style='{font_style} {font_size}'>Select a stock:</p>", unsafe_allow_html=True)
selected_stock = st.sidebar.selectbox("", options=df['TckrSymb'].unique())

st.sidebar.title("🗓️ Date Range")
today = datetime.datetime.now()
current_year = today.year
jan_1 = datetime.date(current_year, 1, 1)
dec_31 = datetime.date(current_year, 12, 31)

st.sidebar.markdown(f"<p style='{font_style} {font_size}'>Select start date:</p>", unsafe_allow_html=True)
start_date = st.sidebar.date_input("Start Date", jan_1, jan_1, dec_31, format="MM.DD.YYYY")

st.sidebar.markdown(f"<p style='{font_style} {font_size} '>Select end date:</p>", unsafe_allow_html=True)
end_date = st.sidebar.date_input("End Date", dec_31, jan_1, dec_31, format="MM.DD.YYYY")

#filtered_data = df[(df['TckrSymb'] == selected_stock) & (df['TradDt'] >= start_date) & (df['TradDt'] <= end_date)]
#filtered_data['ClsPric'] = filtered_data['ClsPric'].astype(float)

clause_where = f"""
    WHERE d.TckrSymb = '{selected_stock}'
    AND f.TradDt >= '{start_date}'
    AND f.TradDt <= '{end_date}'
"""
clause_query = base_query + clause_where

cursor.execute(clause_query)
clause_data = cursor.fetchall()
clause_columns = [desc[0] for desc in cursor.description]
cursor.close()

df = pd.DataFrame(clause_data, columns=clause_columns)
price_column = ['OpnPric', 'HghPric', 'LwPric', 'ClsPric', 'LastPric']
df[price_column] = df[price_column].astype(float)
#df['ClsPric'] = df['ClsPric'].astype(float)

st.sidebar.title("Price Type")
st.sidebar.markdown(f"<p style='{font_style} {font_size}'>Select a price type:</p>", unsafe_allow_html=True)
selected_price = st.sidebar.radio("", price_column)

#st.write("Line Chart - ClsPric:")
#st.line_chart(df.set_index('TradDt')['ClsPric'])

st.markdown(f"<p style='{font_style} {font_size}'>📉 Line Chart - {selected_price}:</p>", unsafe_allow_html=True)
st.line_chart(df.set_index('TradDt')[selected_price])

st.markdown(f"<p style='{font_style} {font_size}'>📊 Fetched Data:</p>", unsafe_allow_html=True)
st.dataframe(df)

cursor = cnx.cursor()

st.title("📰 Display News")
display_news_query = """
    SELECT news, news_date
    FROM dstock_news
    WHERE dstock_id = (SELECT id FROM d_stock WHERE TckrSymb = %s)
    AND news_date >= %s
    AND news_date <= %s
"""
cursor.execute(display_news_query, (selected_stock, start_date, end_date))
display_news_data = cursor.fetchall()

if display_news_data:
    display_news_df = pd.DataFrame(display_news_data, columns=['News', 'Date'])
    st.dataframe(display_news_df)
else:
    st.info("No news to display.")

st.title("📥 Input News")
news_input = st.text_area("Enter your news:", height=200, key="news_input")

news_date = st.date_input("News Date:")

if st.button("Submit News"):
    if news_input and news_date:
        insert_query = """
            INSERT INTO dstock_news (news, dstock_id, news_date)
            VALUES (%s, (SELECT id FROM d_stock WHERE TckrSymb = %s), %s)
        """
        cursor.execute(insert_query, (news_input, selected_stock, news_date))
        cnx.commit()
        st.success("News submitted successfully!")

st.title("🗑️ Delete News")

if not display_news_data:
    st.info("No news to delete.")
else:
    news_to_delete = st.selectbox("Select news to delete:", display_news_df['News'], key="news_to_delete")

    if st.button("Delete News"):
        if news_to_delete:
            delete_query = """
                DELETE FROM dstock_news
                WHERE news = %s
            """
            cursor.execute(delete_query, (news_to_delete,))
            cnx.commit()
            st.success("News deleted successfully!")
            
cnx.close()