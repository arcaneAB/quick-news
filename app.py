import streamlit as st
from newsbox import display_news
from api_interaction import fetch_news,fetch_poster

st.set_page_config(
    page_icon="📰👓",
    page_title="Quick News",
    layout="centered"
)


def run():
    st.title("Quick News 📰👓")    
    category = ['--Select--','Trending News','Categories','Search Topic']
    cat_op = st.selectbox('Please select your choice',category)
    if cat_op == category[0]:
        st.warning("Please select your choice")
    elif cat_op == category[1]:
        st.subheader("Latest Trending News")
        no_of_news = st.slider('Number of news:',min_value=5, max_value=20,step=1)
        news_list = fetch_news()
        display_news(news_list,no_of_news)
    elif cat_op == category[2]:
        topics = ['--Select--','WORLD', 'NATION', 'BUSINESS', 'TECHNOLOGY', 'ENTERTAINMENT', 'SPORTS', 'SCIENCE','HEALTH']
        st.subheader("Please select a category")
        choice = st.selectbox('Choose a category',topics)
        if choice == topics[0]:
            st.warning('Please select category')
        else:
            st.subheader(f"Latest {choice.capitalize()} News")
            no_of_news = st.slider('Number of news:',min_value=5, max_value=20,step=1)
            news_list = fetch_news(topic=choice,type='category')
            display_news(news_list,no_of_news)
    elif cat_op == category[3]:
        user_topic = st.text_input("Enter news search topic")
        no_of_news = st.slider('Number of news:',min_value=5,max_value=20,step=1)
        
        if st.button("Search") and user_topic != '':
            user_topic_pr = user_topic.replace(' ','')
            news_list = fetch_news(topic=user_topic_pr,type='custom')
            if news_list:
                st.subheader(f"Latest {user_topic.capitalize()} News")
                display_news(news_list,no_of_news)
            else:
                st.error(f'No news found for {user_topic.capitalize()}')
        else:
            st.warning('Please search topic')

run()