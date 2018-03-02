# Wordcloud Bot

Written by Hannah Gooden, 3/2/18  
This is a submission to the General Motors-Aggie Coding Club Bot Contest held on 2/16/18.  
I can be contacted at hannah.goodenn@gmail.com or hannah.gooden@tamu.edu.  
All wordclouds produced by the bot will be tweeted at @wordcloud_fun: https://twitter.com/wordcloud_fun/with_replies  
**To preserve privacy, the api tokens have been hidden on this github

## Getting Started

This is my first time using Python so I apologize if I am unclear in my instructions for how to run this bot! Feel free to contact me if you have trouble. I used Python 3.4.3 to test. Simply download the two files, main.py and secrets.py, to a machine with Python installed. Install the dependencies with "pip install tweepy", "pip install wordcloud", and "pip install matplotlib".

## Running

Run "python main.py" to start the program. You will be prompted for a twitter name. Enter any twitter name you'd like. Capitalization doesn't matter, but ignore the "@". If the twitter user does not exist, the API will throw the error "Sorry, that page does not exist." Otherwise, the program will proceed with downloading all tweets by that user, creating a wordcloud, and tweeting it at @wordcloud_fun. The page can be found at https://twitter.com/wordcloud_fun/with_replies. It will also download a local copy of the wordcloud under "tweets.png". 

### Modules

* [Tweepy](http://www.tweepy.org/) - To access the twitter api
* [Wordcloud](https://github.com/amueller/word_cloud) - Creates the wordcloud

## Acknowledgments

* Reused some code for scraping tweets found here: https://gist.github.com/yanofsky/5436496
