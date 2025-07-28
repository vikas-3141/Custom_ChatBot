# 🤖 Darshan UMS Chatbot

A smart, lightweight chatbot built with Streamlit, Scikit-learn, and NLTK to help students and faculty quickly get answers about the **Darshan University Management System (UMS)**.

---

## 📌 Features

- 🎓 Answers FAQs related to Darshan UMS (e.g., attendance, timetable, exam, fees)
- 🔍 Natural language understanding using ML (Logistic Regression)
- 🧠 Customizable intent file (`learnings.json`)
- 🖥️ Web-based interface via Streamlit
- 🔐 Local execution – no data leaves your machine

---

## 🛠️ Tech Stack

| Component         | Description                  |
|------------------|------------------------------|
| **Python**       | Core language                |
| **Streamlit**    | Web UI framework             |
| **Scikit-learn** | Model training & prediction  |
| **NLTK**         | Tokenization & text processing |
| **JSON**         | Custom chatbot intents       |

---

## 🗂️ Project Structure

📁 Darshan-UMS-Chatbot/

├── chatbot/ # Virtual environment (ignored in Git)

├── app.py # Main Streamlit app

├── learnings.json # Chatbot intents and responses

├── requirements.txt # Python dependencies

├── .gitignore # Ignore unnecessary files/folders

└── README.md # You're here!


---

## ⚙️ Installation

```bash
# 1. Clone the repo
git clone https://github.com/your-username/Custom_Chatbot.git
cd Darshan-UMS-Chatbot

# 2. (Optional) Create a virtual environment
python -m venv chatbot
source chatbot/bin/activate    # For Linux/macOS
chatbot\Scripts\activate       # For Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4.Install The ollma and Type This Command
ollama pull llama3  

# 5. Run the Streamlit app
streamlit run app.py
💬 Example Questions to Ask

✅ What you can ask:

"Hi"
"Show my timetable"
"How to pay fees?"
"Any job openings?"
"Where is LMS?"
❌ What you can’t ask (yet):

"What is my CGPA?"
"Email my attendance"
"Can I reschedule my exam?"
"Reset my UMS password"
"Update my profile photo"
📦 Dependencies

Python 3.8+
Streamlit
Scikit-learn
NLTK
Install all via:

pip install -r requirements.txt
📍 Future Improvements

Add authentication using UMS credentials
Connect directly to live UMS APIs (if available)
Voice-based interaction
Mobile responsiveness
🧑‍💻 Developed By

Vikas Sanchaniya & Bhavya Masharu
Email: sanchaniyavikas.com
GitHub: vikas-3141

🏫 About

This chatbot is built specifically for students of Darshan University, to simplify interaction with the UMS portal and reduce repetitive tasks.
