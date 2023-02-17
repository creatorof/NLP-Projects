import streamlit as st
import pandas as pd
import pytreebank
import snscrape.modules.twitter as sntwitter
import itertools
from LSTM import *
from torchtext.data.utils import get_tokenizer
from torchtext.vocab import build_vocab_from_iterator
from collections import Counter
from spacy.lang.en.stop_words import STOP_WORDS
import spacy


st.subheader('''
    Sentiment Analysis of twitter
''')

tokenizer = get_tokenizer('spacy', language='en_core_web_sm')


def yield_tokens(data_iter): #data_iter, e.g., train
    for _, text in data_iter: 
        yield tokenizer(text)

def load_data():
    #dataset = pytreebank.load_sst("./sentiment/")
    data = pytreebank.import_tree_corpus("./sentiment/train.txt")
    return data

def flatten(data):
       return  [(label, text) for d in data for label,text in d.to_labeled_lines()]

text_pipeline = lambda x: vocab(tokenizer(x))
nlp = spacy.load('en_core_web_sm')

def preprocessing(sentence):
    stopwords = list(STOP_WORDS)
    doc = nlp(sentence)
    cleaned_tokens = []

    for token in doc:
        if token.text not in stopwords and token.pos_ != 'PUNCT' and token.pos_ != 'SPACE' and \
                token.pos_ != 'SYM':
            cleaned_tokens.append(token.lemma_.lower().strip())

    return " ".join(cleaned_tokens)

def predict(test_str_list):
    result = list()
    for test_str in test_str_list:
        text = torch.tensor(text_pipeline(test_str)).reshape(1, -1)
        text_length = torch.tensor([text.size(1)]).to(dtype=torch.int64)
        output = model(text, text_length).squeeze(1)
        predicted = torch.max(output.data, 1)[1].detach().cpu().numpy()[0]
        result.append([test_str, predicted])
    
    result = pd.DataFrame(result,columns=['Content','Sentiment'])
    return result

def get_common_words(corpus):
    #data tokenized
    corpus_tokenized = [sent.split(" ") for sent in corpus]
    #2. numericalize (vocab)
    #2.1 get all the unique words
    #we want to flatten unit (basically merge all list)
    flat = lambda l: [item for sublist in l for item in sublist]
    vocabs = list(flat(corpus_tokenized))
    voc_size = len(vocabs)
    print('Vocab Size :',voc_size)
    word_freq = Counter(vocabs)
    common_words = word_freq.most_common(5)
    return common_words

def get_top_words(dataset):
    positive = dataset[dataset['Sentiment'].isin([3,4])] 
    negative = dataset[dataset['Sentiment'].isin([0,1])]
    print(len(positive), len(negative))
    common_words_pos = get_common_words(positive['Content'])
    common_words_neg = get_common_words(negative['Content'])
    return common_words_neg, common_words_pos

def load_model(input_dim, emb_dim, hid_dim, output_dim, num_layers, bidirectional, dropout, pad_idx,save_path= f'LSTM_TreeBank.pt'):
    model = LSTM(input_dim, emb_dim, hid_dim, output_dim, num_layers, bidirectional, dropout, pad_idx)
    model.load_state_dict(torch.load(save_path))
    return model

def count_sentiment(dataset):
    return dataset['Sentiment'].value_counts(ascending=True).to_dict()


train_data = load_data()
train_data = flatten(train_data)
vocab = build_vocab_from_iterator(yield_tokens(train_data), specials=['<unk>','<pad>','<bos>','<eos>'], special_first = True)
vocab.set_default_index(vocab["<unk>"])
pad_idx = vocab['<pad>']
input_dim  = len(vocab)
hid_dim    = 256
emb_dim    = 300         
output_dim = 5
num_layers = 2
bidirectional = True
dropout = 0.5
model = load_model(input_dim, emb_dim, hid_dim, output_dim, num_layers, bidirectional, dropout, pad_idx,save_path= f'LSTM_TreeBank.pt')





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
        data['rawContent'] = data['rawContent'].apply(preprocessing)
        result = predict(data['rawContent'])
        sentiment = count_sentiment(result)
        chart_data = pd.DataFrame.from_dict(sentiment,columns=['count'],orient='index')
        print(sentiment)
        st.bar_chart(chart_data,y='count')
        common_neg_word, common_pos_word = get_top_words(result)
        common_word = pd.DataFrame.from_dict({'positive':common_pos_word, 'negative': common_neg_word})
        st.table(common_word)
        print(common_word)
        #print(data)
        #print(output_csv)

