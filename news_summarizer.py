import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def summarize():
    url_text = url.get('1.0', "end").strip()

    article = Article(url_text)

    article.download()
    article.parse()

    article.nlp()

    title.config(state='normal')
    authors.config(state='normal')
    p_date.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    authors.delete('1.0', 'end')
    authors.insert('1.0', article.authors)

    p_date.delete('1.0', 'end')
    p_date.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis = TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0', f'Polarity: {analysis.polarity}, Sentiment: {"positive" if analysis.polarity > 0  else "negative" if analysis.polarity < 0 else "neutral"}')

    title.config(state='disabled')
    authors.config(state='disabled')
    p_date.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')

root = tk.Tk()
root.title("News Summarizer")
root.geometry('1200x600')

#Title
tlabel = tk.Label(root, text='Title')
tlabel.pack()

title = tk.Text(root, height=1, width=140)
title.config(state='disabled', bg='#dddddd')
title.pack()

#Author
alabel = tk.Label(root, text='Author')
alabel.pack()

authors = tk.Text(root, height=1, width=140)
authors.config(state='disabled', bg='#dddddd')
authors.pack()

#Publication Date
plabel = tk.Label(root, text='Publication Date')
plabel.pack()

p_date = tk.Text(root, height=1, width=140)
p_date.config(state='disabled', bg='#dddddd')
p_date.pack()

#Summary
slabel = tk.Label(root, text="Summary")
slabel.pack()

summary = tk.Text(root, height=20, width=140)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

#Sentiment Analysis
selabel = tk.Label(root, text="Sentiment Analysis")
selabel.pack()

sentiment = tk.Text(root, height=1, width=140)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

#URL
ulabel = tk.Label(root, text='Add URL')
ulabel.pack()

url = tk.Text(root, height=1, width=140)
url.config(state='normal', bg='#ffffff')
url.pack()

#Button
btn = tk.Button(root, text="Summarize", command=summarize)
btn.pack(pady=5)

root.mainloop()
