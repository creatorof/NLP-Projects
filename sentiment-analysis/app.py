import streamlit as st
import pandas as pd
import base64
import snscrape.modules.twitter as sntwitter
import itertools
from LSTM import *

def convert_df(df):
    return df.to_csv().encode('utf-8')


def get_csv_download_link(csv, filename):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """

    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}" download="{filename}.csv">Download csv file</a>'
    return href

st.subheader('''
    Sentiment Analysis of twitter
''')
model = LSTM()
with open("LSTM_TreeBank.pt",'wb') as f:
    pickle.dump(model,f)

with st.form(key='Twitter_form'):
    search_term = st.text_input('What do you want to search for?')
    #output_csv = st.radio('Save as CSV file?',['Yes','No'])
    #file_name = st.text_input('Save file as:')
    submit_button = st.form_submit_button(label='Search')
    if submit_button:
        scraped_tweets = sntwitter.TwitterSearchScraper(search_term).get_items()
        # slicing the generator to keep only the first 100 tweets
        sliced_scraped_tweets = itertools.islice(scraped_tweets, 200)
        # convert to a DataFrame and keep only relevant columns
        df = pd.DataFrame(sliced_scraped_tweets)[['date', 'rawContent','lang']]
        data = df[df['lang'] == 'en']
        #print(data)
        #print(output_csv)