

# **AI Text Summarizer**  

## **Overview**  
The **AI Text Summarizer** is a web-based tool that generates a **concise summary** of input text in three bullet points using an **LLM model (DeepSeek AI)**. The application is built with **Gradio** for the front-end UI and uses **FastAPI** to interact with the LLM.  

This project enables users to quickly extract key points from large pieces of text, making it useful for students, professionals, and researchers.  

## **Tech Stack**  

| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language for the project. |
| **Gradio** | Provides a simple and interactive web-based UI for the summarization tool. |
| **FastAPI** | A modern, high-performance web framework used to create the API. |
| **Postman** | Used to test API requests and responses efficiently. |
| **Git & GitHub** | Version control and repository management. |
| **DeepSeek AI Model (via API)** | The core LLM used for text summarization. |
| **Virtual Environment (`venv`)** | Ensures dependency management and project isolation. |

---

## **Why These Technologies?**  

### **1. Gradio**  
- Provides a quick and easy way to create web-based applications without complex frontend development.  
- Allows users to input text and get results interactively.  

### **2. FastAPI**  
- Handles API requests efficiently.  
- Supports asynchronous processing for better performance.  
- Generates automatic API documentation (Swagger UI).  

### **3. Postman**  
- Helps in testing API endpoints without writing additional scripts.  
- Useful for debugging and monitoring API responses.  

### **4. DeepSeek AI (LLM Model)**  
- Generates high-quality text summaries using advanced deep-learning techniques.  
- Processes text through API requests for fast and scalable summarization.  

### **5. Git & GitHub**  
- Enables version control and collaboration.  
- The project is hosted on GitHub for easy access and updates.  

### **6. Virtual Environment (`venv`)**  
- Prevents conflicts with system-wide Python packages.  
- Keeps dependencies consistent across different machines.  

---

## **Installation & Setup**  

Follow these steps to set up and run the project on your local machine.  

### **Step 1: Clone the Repository**  
```bash
git clone https://github.com/Nsk364/AI-Text-Summarizer-Agent.git
cd AI-Text-Summarizer-Agent
```

### **Step 2: Create and Activate Virtual Environment**  
#### **Windows**  
```bash
python -m venv dsvenv
dsvenv\Scripts\activate
```
#### **Mac/Linux**  
```bash
python3 -m venv dsvenv
source dsvenv/bin/activate
```

### **Step 3: Install Dependencies**  
```bash
pip install -r requirements.txt
```

### **Step 4: Start the API Server (FastAPI)**  
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```
- The API will be available at: `http://127.0.0.1:8000`  
- Open `http://127.0.0.1:8000/docs` to view the Swagger UI for API testing.  

### **Step 5: Launch the Gradio UI**  
```bash
python app.py
```
- The web interface will open automatically in your browser.  
- You can input text and get a summarized output in **three bullet points**.  

---

## **How the API Works**  

- The FastAPI server listens for incoming requests.  
- When a user submits text via the Gradio UI, the backend makes a request to the **DeepSeek AI API**.  
- The response from the model is formatted and displayed in the UI.  

---

## **Testing the API with Postman**  

1. Open **Postman** and create a **new request**.  
2. Set the method to `POST` and enter:  
   ```
   http://127.0.0.1:8000/summarize
   ```
3. In the **Body** tab, select **raw** and choose `JSON`.  
4. Enter the request payload:  
   ```json
   {
       "text": "Your input text here..."
   }
   ```
5. Click **Send**, and you should receive a JSON response with the summarized text.  

---

## **Future Enhancements**  

- **Allow users to select summary length** (short, medium, long).  
- **Add multilingual support** for summarization.  
- **Improve UI** by adding more customization options.  
- **Implement caching** to speed up processing for repeated texts.  

---

## **Contributing**  

1. Fork the repository.  
2. Create a new branch:  
   ```bash
   git checkout -b feature-branch-name
   ```
3. Make changes and commit:  
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your branch and create a **Pull Request**.  

---

## **Contact & Support**  
For any queries or suggestions, reach out to:  
📧 Email: nipunsai_kokonda@srmap.edu.in  
📂 GitHub: [Nsk364](https://github.com/Nsk364)  

---
