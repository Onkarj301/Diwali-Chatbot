import streamlit as st
import nltk  
from sklearn.feature_extraction.text import TfidfVectorizer  
from sklearn.svm import SVC  
import numpy as np
from PIL import Image

# Load the NLTK data
nltk.download('punkt')

# Displaying the Happy Diwali greeting
st.title("Happy Diwali!")
st.write("Wishing you and your loved ones a joyful and prosperous Diwali! 🪔✨")

# Load and display the Diwali image
images = ["diwali.jpg"]  # Update the path to your Diwali image
st.image(images, caption='Happy Diwali!', width=700)


# Training data: simple Diwali-related FAQs and responses
train_data = {
    "What is Diwali?": "Diwali is a Hindu festival of lights, celebrating the victory of light over darkness and good over evil.",
    "Why is Diwali celebrated?": "Diwali commemorates Lord Rama's return to Ayodhya after 14 years of exile and celebrates the triumph of light over darkness.",
    "What are common Diwali traditions?": "Diwali traditions include lighting diyas, decorating homes, exchanging gifts, and enjoying sweets.",
    "What are some Diwali gift ideas?": "Popular Diwali gift ideas include sweets, diyas, candles, home decor, and personalized items like photo frames.",
    "What are Diwali decorations?": "Diwali decorations often feature diyas, rangoli, fairy lights, and flower garlands to create a festive atmosphere.",
    "greeting": "Happy Diwali! May this festival of lights bring joy and prosperity to you and your loved ones!",
    "recipes": "Popular Diwali recipes include Gulab Jamun, Ladoo, Jalebi, and Samosa. Let me know if you need more info!"
}

# Preprocess training data
questions = list(train_data.keys())
answers = list(train_data.values())

# TF-IDF vectorization
vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(questions)

# Train the classifier (SVM)
model = SVC(kernel='linear')
model.fit(X_train, range(len(questions)))

# Function to predict the answer
def get_response(user_input):
    user_input_vect = vectorizer.transform([user_input])
    prediction = model.predict(user_input_vect)
    return answers[prediction[0]]

# Streamlit UI for the chatbot
st.title("Diwali Chatbot 🧨🎊🎉")
st.write("Ask me anything about Diwali!")

# User input
user_input = st.text_input("You:")

if user_input:
    if "sweets" in user_input.lower():
        images=["kajukatli.jpg","sankarpalya.jpg","ladu.jpg"]
        captions = ["Kajukatli", "Sankarpalya", "Ladu"]
        st.image(images,captions,width=200)  
    elif "decoration" in user_input.lower():
        images=["lighting.jpg","diya.jpg","flowers.jpg"]
        captions = ["lighting", "Diya", "flowers"]
        st.image(images, captions,width=200)  # Ensure the path is correct
    elif "gift" in user_input.lower():
        images=["chocolate.webp","dry.webp","Hamper.webp"]
        captions = ["Chocolate", "Dryfruits","Hamper"]
        st.image(images, captions,width=200) 

# Display chatbot response
if user_input:
    response = get_response(user_input)
    st.write(f"Chatbot: {response}")
