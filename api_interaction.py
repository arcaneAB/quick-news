import streamlit as st
from PIL import Image
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def fetch_news(topic=None,type=None):
    src='https://news.google.com/news/rss'
    if(type=='custom'):
        src = f'https://news.google.com/rss/search?q={topic}'
    elif(type=='category'):
        src = f'https://news.google.com/news/rss/headlines/section/topic/{topic}'
    op = urlopen(src)
    data = op.read()
    op.close()
    sp_pg = soup(data,'xml')
    news_list = sp_pg.find_all('item')
    return news_list


def fetch_poster(img_src):
    try:
        u = urlopen(img_src)
        raw_img = u.read()
        img = Image.open(io.BytesIO(raw_img))
        st.image(img,use_column_width=True)
    except:
        u = urlopen('https://archive.org/download/placeholder-image/placeholder-image.jpg')
        raw_img = u.read()
        img = Image.open(io.BytesIO(raw_img))
        st.image(img,use_column_width=True)
