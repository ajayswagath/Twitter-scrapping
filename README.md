<h1>Twitter web scraping using snscrape and GUI using Streamlit</h1>
<h2>Problem statement</h2>
Data is dispersed throughout the world nowadays. There may be a significant amount of data on Facebook, Instagram, Youtube, Twitter, and other social media platforms, 
particularly. As opposed to Facebook and Twitter, this includes images and videos on YouTube and Instagram.In order to understand we twitter data we should scrape the 
data from Twitter in order to obtain the actual facts about Twitter.we must scrape information from Twitter, such as the [date, id, url, tweet text, user, reply count, 
retweet count, language, source, like count,etc.]
<h2>Approach</h2>
<ul>
<li>Scrape the Twitter data from Twitter Reference using the "snscrape" Library.Make a dataframe that includes the following information: 
 [date, id, url, tweet content, user, reply and retweet count, language, source, and like count.]</li>
<li>Each data should be saved as a document in MongoDB together with the hashtag or search term we used to scrape Twitter.
For instance: ("Scraped Term" : "Elon Musk", "Scraped Date" : February 15, 2023, "Scraped Data" : "1000 Scraped data from the preceding 100 days").</li>
<li>Build a GUI using streamlit that has the ability to limit the number of tweets that need to be scraped, choose the date range, and enter the keyword 
or hashtag to be searched. Following scraping, the information must be shown on the website with a button to upload it to a database and download 
it in CSV and Json formats.</li>  
</ul>
<h2>Libraries</h2>
<ol>
<li>Snscrape</li>
<li>Streamlit</li>
<li>Pandas</li>
<li>MongoDB</li>
<li>Json</li>  
</ol>
