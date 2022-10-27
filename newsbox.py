import streamlit as st
from api_interaction import fetch_news,fetch_poster
from newspaper import Article
import io
import nltk
nltk.download('punkt')

def display_news(list_of_news,news_quantity):
    c = 0
    for news in list_of_news:
        c += 1
        st.write(f'**({c}) {news.title.text}**')
        news_data = Article(news.link.text)
        try:
            news_data.download()
            news_data.parse()
            news_data.nlp()
        except Exception as e:
            st.error(e)
        fetch_poster(news_data.top_image)
        with st.expander(news.title.text):
            st.markdown(
                '''<h6 style='text-align:justify;'>"{}"</h6>'''.format(news_data.summary),unsafe_allow_html=True
            )
            st.markdown("[Read more at {}...]({})".format(news.source.text,news.link.text))
        st.success("Published Date: " + news.pubDate.text)
        if c>=news_quantity:
            break
