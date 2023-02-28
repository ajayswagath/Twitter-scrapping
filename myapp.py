import streamlit as st
import pandas as pd
import snscrape.modules.twitter as sntwitter
import json
import pymongo


st.title("Twitter scrapping App")


text = st.text_input("enter your text","")
number = st.number_input("enter your number")

scraper=sntwitter.TwitterSearchScraper(text) 

tweets1=[]
tweets2=[]

for i,tweet in enumerate (scraper.get_items()):
    data1 = [tweet.date,tweet.id,tweet.url,tweet.content,tweet.user,tweet.replyCount,tweet.retweetCount,tweet.lang,tweet.source,tweet.likeCount] 
    data2=({#"date":tweet.date,
           "id":tweet.id,
           "url":tweet.url,
           "tweetcontent":tweet.content,
           #"user":tweet.user,
           "replycount":tweet.replyCount,
           "retweetcount":tweet.retweetCount,
           "language":tweet.lang,
           "source":tweet.source,
           "likecount":tweet.likeCount})
    if i>number:
        break
    tweets1.append(data1)
    tweets2.append(data2)

tweet_df = pd.DataFrame(tweets1,columns=["date","id","url","tweetcontent","user","replycount","retweetcount","language","source","likecount"]) 

st.dataframe(tweet_df)

def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(tweet_df)

st.download_button(
    label="Download data as CSV",
    data=csv,
    file_name='large_df.csv',
    mime='text/csv',
)


#st.json(tweets2)

json_string = json.dumps(tweets2)

st.json(json_string, expanded=True)

st.download_button(
    label="Download JSON",
    file_name="data.json",
    mime="application/json",
    data=json_string,
    )

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client['database']
collection = db['twitter']




if st.button('Upload the data into database'):
    x = db.twitter.insert_many(tweets2)
    st.balloons()


