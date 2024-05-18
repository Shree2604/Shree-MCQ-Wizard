import streamlit as st
import os
import re
import random
from dotenv import load_dotenv
from text import select_text_from_pdf
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_mcq_questions_and_answers_from_pdf(pdf_file_path, difficulty, num_questions):
    # Extract text from PDF
    try:
        pdf_text = select_text_from_pdf(pdf_file_path)
    except Exception as e:
        st.error(f"Error reading PDF file: {e}")
        return

    # Format for MCQ questions
    Ans_format = """Please generate Answer Key in the following Format:
    ## Answer Key:
    **Q{question_number}. {correct_option} , Q{question_number}. {correct_option} ,**"""

    q_format = """Please generate multiple choice questions in the following format:

     **Question No. {question_number}:** {question}

   a. {option_a}
   b. {option_b}
   c. {option_c}
   d. {option_d}

  Based on the given text only: {text}"""

    # Define the prompt based on the difficulty level
    difficulty_prompt = {
        "Easy": f"Please generate {num_questions} very easy MCQ questions. These questions should be straightforward and have an answer key based solely on the given text. {q_format}{Ans_format}{pdf_text}",
        "Medium": f"Please generate {num_questions} moderate level MCQ questions. These questions should be of moderate difficulty and have an answer key based solely on the given text. {q_format}{Ans_format}{pdf_text}",
        "Hard": f"Please generate {num_questions} hard MCQ questions. These questions should be challenging, with relatively more complex compared to easy and moderate. Answers should have a key based solely on the given text. {q_format}{Ans_format}{pdf_text}"
    }

    prompt = difficulty_prompt.get(difficulty, "Invalid difficulty level. Please choose from 'easy', 'medium', or 'hard'.")

    # Configure GenerativeAI
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

    # Initialize GenerativeModel
    model = genai.GenerativeModel('gemini-pro')

    # Generate content (MCQ questions)
    response = model.generate_content(prompt)
    model_response = response.text
    cleaned_text = re.sub(r'[*#]', '', model_response)
    start_index = cleaned_text.find("Answer Key")
    answer_key = cleaned_text[start_index:]
    generated_que = cleaned_text[:start_index]

    questions = generated_que.split("Question No. ")[1:]  # Split into individual questions
    key_answers = answer_key.split(", ")  # Split answer key

    return questions, key_answers



