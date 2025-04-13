import torch
import gradio as gr
from transformers import pipeline


model_path = "../Models/models--sshleifer--distilbart-cnn-12-6/snapshots/a4f8f3ea906ed274767e9906dbaede7531d660ff"
text_summary = pipeline("summarization", model=model_path)

def summary(input_text):
    if not input_text.strip():
        return gr.update(value="❗ No text provided. Please enter some content to summarize."), ""
    if len(input_text.strip()) < 5:
        return gr.update(value="⚠️ Text too short to summarize. Please enter a longer input."), ""

    try:
        output = text_summary(input_text)
        return "", output[0]["summary_text"]
    except Exception as e:
        return gr.update(value=f"❌ Error during summarization: {str(e)}"), ""

custom_css = """
body {
    background-color: #1e1e1e;
}
.gradio-container {
    max-width: 1000px;
    margin: auto;
    font-family: 'Segoe UI', sans-serif;
}
.gr-button {
    background: #4a90e2;
    color: white;
    border-radius: 8px;
    font-weight: 600;
}
textarea, .gr-textbox, .gr-input, .gr-output {
    background-color: #ffffff !important;
    color: #000000 !important;
    font-size: 15px;
    padding: 12px;
    border-radius: 8px;
}
.gr-box {
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0,0,0,0.15);
    background-color: #ffffff;
}
footer { display: none !important; }
"""

with gr.Blocks(css=custom_css) as demo:
    gr.Markdown("""
    <div style="text-align: center; margin-bottom: 10px;">
        <h1 style="font-size: 32px; font-weight: bold;">📚 Academic Text Summarizer</h1>
        <p style="font-size: 16px; color: #ccc;">
            A lightweight summarization app built by <strong style="color:white;">Abhijeet Solanki</strong>, AI & NLP
        </p>
    </div>
    """)

    with gr.Row(equal_height=True):
        with gr.Column(scale=1):
            input_text = gr.Textbox(
                label="Input Text",
                lines=15,
                placeholder="Paste your article, research abstract, or paragraph here..."
            )
        with gr.Column(scale=1):
            output_text = gr.Textbox(
                label="Generated Summary",
                lines=15,
                placeholder="Your summary will appear here..."
            )

    with gr.Row():
        summarize_btn = gr.Button("✨ Generate Summary")
        clear_btn = gr.Button("🧹 Clear")

    summarize_btn.click(fn=summary, inputs=input_text, outputs=[input_text, output_text])
    clear_btn.click(fn=lambda: ("", ""), inputs=None, outputs=[input_text, output_text])

demo.launch()

