import requests
import gradio as gr

OLLAMA_URL = "http://localhost:11434/api/generate"
stop_processing = False  # Flag to control processing

def summarize_text(text):
    global stop_processing
    stop_processing = False  # Reset flag when function starts

    payload = {
        "model": "deepseek-r1:7b",
        "prompt": f"Summarize the following text in **3 bullet points**:\n\n{text}",
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        
        if stop_processing:  # If stop button was pressed
            return "❌ Processing stopped by user."

        return response.json().get("response", "⚠️ No summary generated.")
    
    except requests.exceptions.RequestException as e:
        return f"⚠️ Error: {str(e)}"

def stop():
    global stop_processing
    stop_processing = True
    return "❌ Processing stopped."

def clear_text():
    return ""  # Returns an empty string to clear the text input

# Modern Glassmorphic CSS
custom_css = """
body {
    font-family: 'Poppins', sans-serif;
    color: white;
    background: linear-gradient(to right, #141e30, #243b55);
}
.gradio-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.gr-block {
    width: 60%;
    background: rgba(255, 255, 255, 0.1);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
    text-align: center;
}
textarea, input {
    background: rgba(255, 255, 255, 0.2);
    border: none;
    color: white;
    padding: 10px;
    border-radius: 8px;
}
textarea::placeholder {
    color: rgba(255, 255, 255, 0.6);
}
button {
    width: 150px;
    padding: 10px;
    font-size: 16px;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
    transition: 0.3s;
}
button:first-of-type {
    background: linear-gradient(135deg, #ff416c, #ff4b2b);
    color: white;
    border: none;
}
button:first-of-type:hover {
    transform: scale(1.05);
    box-shadow: 0px 4px 8px rgba(255, 75, 43, 0.4);
}
button:nth-of-type(2) {
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    color: white;
    border: none;
}
button:nth-of-type(2):hover {
    transform: scale(1.05);
    box-shadow: 0px 4px 8px rgba(37, 117, 252, 0.4);
}
button:last-of-type {
    background: linear-gradient(135deg, #ffcc00, #ff9900);
    color: white;
    border: none;
}
button:last-of-type:hover {
    transform: scale(1.05);
    box-shadow: 0px 4px 8px rgba(255, 153, 0, 0.4);
}
"""

with gr.Blocks(css=custom_css) as interface:
    gr.Markdown("# AI-Powered Text Summarizer by NSK ")
    gr.Markdown("🔍 Enter text, and DeepSeek AI will generate a **concise summary** in **3 bullet points**.")

    with gr.Row():
        text_input = gr.Textbox(lines=8, placeholder="Type or paste your text here...")
    
    output_text = gr.Textbox(label="📄 Summarized Text", interactive=False)
    
    with gr.Row():
        summarize_button = gr.Button("Summarize")
        stop_button = gr.Button("Stop Processing")
        clear_button = gr.Button("Clear")

    summarize_button.click(summarize_text, inputs=text_input, outputs=output_text)
    stop_button.click(stop, outputs=output_text)
    clear_button.click(clear_text, outputs=text_input)

if __name__ == "__main__":
    interface.launch(share=True)

# cd C:\Codes\DeepSeekProjects\TextSummarizer
