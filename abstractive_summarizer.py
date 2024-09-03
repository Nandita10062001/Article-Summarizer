import tkinter as tk
from tkinter import scrolledtext
from datasets import load_dataset
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

dataset = load_dataset("cnn_dailymail", "3.0.0")

tokenizer = T5Tokenizer.from_pretrained("t5-small")  # Using t5-small for faster performance
model = T5ForConditionalGeneration.from_pretrained("t5-small")

def summarize_article(article_text):
    input_text = "summarize: " + article_text
    input_ids = tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True)
    
    with torch.no_grad():  # Disable gradient calculation for faster inference
        summary_ids = model.generate(input_ids, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Define the GUI
class SummarizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Abstractive Summarization with T5")
        
        self.label = tk.Label(root, text="Enter Article:")
        self.label.pack(pady=10)

        self.article_input = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
        self.article_input.pack(pady=10)

        self.summarize_button = tk.Button(root, text="Summarize", command=self.summarize)
        self.summarize_button.pack(pady=10)

        self.summary_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=10)
        self.summary_output.pack(pady=10)

    def summarize(self):
        article_text = self.article_input.get("1.0", tk.END)
        summary = summarize_article(article_text)
        self.summary_output.delete("1.0", tk.END)
        self.summary_output.insert(tk.END, summary)


def main():
    root = tk.Tk()
    app = SummarizerApp(root)
    
    sample_article = dataset["validation"][10]["article"]
    app.article_input.insert(tk.END, sample_article)
    
    root.mainloop()

if __name__ == "__main__":
    main()
