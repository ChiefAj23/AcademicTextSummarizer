# 📚 Academic Text Summarizer
A lightweight, AI-powered web application that generates concise and coherent summaries of academic texts, research papers, articles, and technical documentation. Built using Hugging Face Transformers and Gradio, this tool is designed to assist graduate students, researchers, and knowledge workers by simplifying the summarization process.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Transformers](https://img.shields.io/badge/🤗-Transformers-orange)
![Gradio](https://img.shields.io/badge/Gradio-UI-lightgrey?logo=gradio)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

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

## 💠 Tech Stack

| Component     | Description                                       |
|---------------|---------------------------------------------------|
| `Python`      | Programming language                              |
| `Hugging Face Transformers` | NLP model loading and inference     |
| `Gradio`      | Web UI for model interaction                      |
| `PyTorch`     | Deep learning backend for transformer inference   |

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/text-summarizer-app.git
cd text-summarizer-app
```

### 2. Set up virtual environment (recommended)

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
python app.py
```

---

## 📸 UI Preview

> Coming soon...

---

## 📂 File Structure

```
📁 text-summarizer-app/
│
├— app.py                 # Gradio app interface
├— requirements.txt       # Python dependencies
├— README.md              # Project documentation
└— models/                # Local model snapshots (optional)
```

---

## ✍️ Author

**Abhijeet Solanki**
If you enjoyed this or have suggestions, feel free to reach out!
Abhijeet Solanki

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


