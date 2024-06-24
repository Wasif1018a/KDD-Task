#!/usr/bin/env python
# coding: utf-8

# # 1. Data Exploration and Preparation:

# In[1]:


import pandas as pd
from datasets import load_dataset

dataset = load_dataset('scientific_papers', 'pubmed', trust_remote_code=True)
dataset


# In[2]:


sample = dataset['train'][0]
print(sample)


# In[3]:


df = pd.DataFrame(dataset['train'])

# Checking for missing values
print(df.isnull().sum())

# Inspecting data types
print(df.dtypes)


# In[4]:


import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

def clean_text(text):
    # Removing special characters
    text = re.sub(r'\W', ' ', text)

    # Removing single characters
    text = re.sub(r'\s+[a-zA-Z]\s+', ' ', text)

    # Removing multiple spaces
    text = re.sub(r'\s+', ' ', text, flags=re.I)

    # Converting to lowercase
    text = text.lower()

    return text

df['article'] = df['article'].apply(clean_text)
df['abstract'] = df['abstract'].apply(clean_text)


# In[5]:


from nltk.tokenize import word_tokenize
nltk.download('punkt')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Tokenizing the text
    tokens = word_tokenize(text)

    # Removing stop words
    tokens = [word for word in tokens if word not in stop_words]

    return ' '.join(tokens)

df['article'] = df['article'].apply(preprocess_text)
df['abstract'] = df['abstract'].apply(preprocess_text)


# In[13]:


df['article'][0]


# In[ ]:


from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import pandas as pd

model_name = 't5-small'
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def summarize_dataframe(df):
    summaries = []
    for article in df.iloc[:, 0]:
        summary = summarize(article)
        summaries.append(summary)
    df['summary'] = summaries
    return df

def summarize(text):
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=512, truncation=True)
    summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary


# In[ ]:


df['summary']

