# 📰 Article-Summarizer

This project encompasses two distinct approaches to summarization: one based on **TextBlob** and **newspaper** for extractive summarization, and another using **T5** from the Hugging Face Transformers library for abstractive summarization.

## ✨ Features

1. **News Summarizer:**
   - Extracts titles, authors, publication dates, and key points from any news article.
   - Analyzes the sentiment of the article's content.
   - Simple and user-friendly GUI built with **Tkinter**.

2. **Abstractive Summarizer with T5:**
   - Generates human-like summaries using the **T5 Transformer model**.
   - Handles long texts with efficient tokenization and inference using PyTorch.
   - Interactive GUI with scrollable text input and output fields.

## 🚀 How It Works

### News Summarizer
- **Input:** Paste the URL of a news article.
- **Output:** The tool extracts and displays the title, author(s), publication date, summary, and sentiment of the article.
- **Usage:** Perfect for quickly understanding the gist of a news article without reading the entire content.

### Abstractive Summarizer
- **Input:** Paste or type any lengthy article or text.
- **Output:** The tool generates an abstract summary, capturing the essence of the text.
- **Usage:** Ideal for summarizing research papers, essays, or any long-form content into a few key sentences.

## 🛠️ Installation

To get started with **Article-Summarizer**, follow these steps:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/Article-Summarizer.git
   cd Article-Summarizer
