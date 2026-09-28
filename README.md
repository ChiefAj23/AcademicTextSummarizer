# 📚 Academic Text Summarizer
A lightweight, AI-powered web application that generates concise and coherent summaries of academic texts, research papers, articles, and technical documentation. Built using Hugging Face Transformers and Gradio, this tool is designed to assist graduate students, researchers, and knowledge workers by simplifying the summarization process.


![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Transformers](https://img.shields.io/badge/🤗-Transformers-orange)
![Gradio](https://img.shields.io/badge/Gradio-UI-lightgrey?logo=gradio)

---

## Problem Statement
As a graduate researcher, I must regularly read and summarize voluminous research papers and academic journals. This is a time-consuming and mentally exhausting process. This routine process acts as a hurdle to productivity and slows down the rate of literature review and synthesis of knowledge. To address this issue, I designed an AI-powered summarization tool that employs the latest natural language processing techniques to produce concise summaries from lengthy academic documents. This tool will be helpful for students, scholars, and professionals by automatically summarizing, saving time, and enhancing comprehension.

---

## 🚀 Features

- 🧑‍🧬 **Abstractive Summarization** using `distilbart-cnn-12-6` (Hugging Face)
- ⚙️ Built with **Gradio** for an interactive, browser-based UI
- 💾 Supports **local inference** for offline use
- 💬 Simple and intuitive user experience
- 👨‍🎓 Designed specifically for students, researchers, and educators

---

## 🧠 Model Information

This app uses the `sshleifer/distilbart-cnn-12-6` model from Hugging Face, which is a distilled version of Facebook's BART model fine-tuned on the CNN/DailyMail dataset for summarization tasks.

### 📥 Downloading the Model Manually (Optional)
If you prefer not to download the model at runtime, you can manually download it and use it locally.

#### Step 1: Download the model
```bash
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "sshleifer/distilbart-cnn-12-6"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./models/distilbart-cnn-12-6")
tokenizer.save_pretrained("./models/distilbart-cnn-12-6")
```

#### Step 2: Update app code to use local path
```python
model_path = "./models/distilbart-cnn-12-6"
text_summary = pipeline("summarization", model=model_path, tokenizer=model_path)
```

This enables **offline inference** and faster loading time for repeated use.

---

## 💠 Tech Stack

| Component     | Description                                       |
|---------------|---------------------------------------------------|
| `Python`      | Programming language                              |
| `Hugging Face Transformers` | NLP model loading and inference     |
| `Gradio`      | Web UI for model interaction                      |
| `PyTorch`     | Deep learning backend for transformer inference   |

---

## 📂 File Structure

```
📁 AcademicTextSummarizer/
│
├── App/
│   └── TextSummary.py     # Gradio app interface
├── requirements.txt       # Python dependencies
├── LICENSE
└── README.md              # Project documentation
```

---


## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/ChiefAj23/AcademicTextSummarizer.git
cd AcademicTextSummarizer
```

### 2. Set up the virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python App/TextSummary.py
```

---

## 📸 UI Preview

<img width="979" alt="Screenshot 2025-04-14 at 11 18 53 AM" src="https://github.com/user-attachments/assets/ac21fbe7-56d6-4c92-9a5d-1c8e9d3a4eec" />

---

## ✍️ Author

**Abhijeet Solanki**
If you enjoyed this or have suggestions, feel free to reach out!

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

