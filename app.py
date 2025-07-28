import streamlit as st
import random
import json
import numpy as np
import string
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

# Load intents from your JSON file
with open('learnings.json', 'r') as f:
    data = json.load(f)

patterns = []
tags = []
responses = {}

def preprocess(text):
    # Lowercase, remove punctuation
    text = text.lower()
    return ''.join(ch for ch in text if ch not in string.punctuation)

# Prepare training data
for intent in data['intents']:
    for pattern in intent['patterns']:
        patterns.append(preprocess(pattern))
        tags.append(intent['tag'])
    responses[intent['tag']] = intent['responses']

# Vectorizer without stop words (to keep short words like 'hi', 'hello')
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(patterns)
y = np.array(tags)

# Train classifier
model = LogisticRegression(max_iter=300)
model.fit(X, y)

# Important: Define keywords for critical intents to guarantee accurate detection
KEYWORD_INTENTS = {
    "greeting": ['hi', 'hello', 'hey', 'good morning', 'good evening'],
    "goodbye": ['bye', 'goodbye', 'thanks', 'see you'],
    "profile_info": ['profile', 'who am i', 'my details', 'student details', 'my information'],
    "fee_payment": ['fee', 'pay fees', 'tuition', 'payment'],
    "exam_info": ['exam', 'hall ticket', 'exam form', 'exam date', 'apply for exam'],
    "job_portal": ['job', 'placement', 'career', 'job openings'],
    # Add more keyword lists here for other intents as needed
}

def check_keywords(user_text):
    user_text = user_text.lower()
    for intent, keywords in KEYWORD_INTENTS.items():
        if any(keyword in user_text for keyword in keywords):
            return intent
    return None

# Streamlit app UI
st.set_page_config(page_title="Darshan UMS Chatbot", page_icon="🤖")
st.title("🤖 Darshan UMS Chatbot")
st.markdown("Ask me anything about your Darshan UMS portal!")

user_input = st.text_input("You:", "")

if user_input and user_input.strip():
    user_processed = preprocess(user_input)

    # First check keywords for guaranteed detection
    keyword_intent = check_keywords(user_input)
    if keyword_intent:
        response = random.choice(responses.get(keyword_intent, ["Sorry, I couldn't find an answer."]))
        st.success(f"Bot: {response}")

    else:
        # ML based prediction fallback
        user_vec = vectorizer.transform([user_processed])
        predicted_tag = model.predict(user_vec)[0]
        confidence = np.max(model.predict_proba(user_vec))

        # DEBUG: comment this out in production
        st.write(f"**DEBUG:** Predicted Tag = {predicted_tag}, Confidence = {confidence:.2f}")

        if confidence > 0.3 and predicted_tag in responses:
            response = random.choice(responses[predicted_tag])
            st.success(f"Bot: {response}")
        else:
            # Fallback response from JSON or generic message
            fallback_response = random.choice(responses.get("fallback", ["Sorry, I didn't understand that. Please try rephrasing."]))
            st.warning(f"Bot: {fallback_response}")

st.markdown("---")
st.caption("🔧 Developed by Vikas Sanchaniya using Streamlit | Darshan UMS Bot")
