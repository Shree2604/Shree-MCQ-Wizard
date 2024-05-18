import streamlit as st
import os
from dotenv import load_dotenv
from MCQ import generate_mcq_questions_and_answers_from_pdf

load_dotenv()

def main():
    # Set the app title
    st.set_page_config(page_title="MCQ Generator", page_icon="📝", layout="wide")

    # File uploader page
    if "questions" not in st.session_state:
        st.title("🔖 Shree MCQ Generator: Transforming PDFs into Interactive Quizzes")

        pdf_file = st.file_uploader("Upload a PDF file", type=["pdf"])

        num_questions = st.number_input("Enter the number of questions", min_value=1)

        difficulty_level = st.selectbox("Select difficulty level", ["Easy", "Medium", "Hard"])

        if st.button("Start Quiz 🚀"):
            if pdf_file and num_questions and difficulty_level:
                pdf_file_path = pdf_file.name
                with open(pdf_file_path, "wb") as f:
                    f.write(pdf_file.getbuffer())

                # Generate MCQ questions and answer key
                questions, key_answers = generate_mcq_questions_and_answers_from_pdf(pdf_file_path, difficulty_level, num_questions)

                # Store questions and answers in session state
                st.session_state["questions"] = questions
                st.session_state["key_answers"] = key_answers
               
                # Store user's attempted questions
                st.session_state["attempted_questions"] = [False] * len(questions)
                st.session_state["user_answers"] = [None] * len(questions)  # Added to store user's answers

                # Redirect to the MCQ page after loading questions
                st.rerun()

    # MCQ page
    else:
        st.title("📝 MCQ Questions")

        # Get user's attempted questions
        attempted_questions = st.session_state["attempted_questions"]

        # Display questions
        for i, (question, attempted) in enumerate(zip(st.session_state["questions"], attempted_questions), start=1):
            if not attempted:
                st.markdown(f'<div style="color: red;"><b>Question No. {i}:</b> (Not Attempted)</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div style="color: white;"><b>Question No. {i}:</b></div>', unsafe_allow_html=True)
            st.write(question)
            user_answer = st.text_input("Your Answer:", key=f"question_{i}")
            st.session_state["user_answers"][i-1] = user_answer  # Store user's answer
            if user_answer.strip() != "":
                attempted_questions[i-1] = True

        # Display the count of attempted questions
        attempted_count = sum(attempted_questions)
        st.write(f"Attempted {attempted_count}/{len(attempted_questions)} questions.")

        # Submit button
        if st.button("Submit"):
            st.session_state["submitted"] = True

        # Display results when submit button is clicked
        if st.session_state.get("submitted", False):
            # Get user answers
            user_answers = st.session_state["user_answers"]

            # Calculate score and display results
            score = 0
            st.write("**Results:**")
            for i, (user_ans, key_ans, attempted) in enumerate(zip(user_answers, st.session_state["key_answers"], attempted_questions), start=1):
                if not attempted:
                    st.write(f"Question {i}: Not Attempted 🚫")
                else:
                    key_ans_parts = key_ans.split(". ")
                    if len(key_ans_parts) > 1:
                        correct_ans = key_ans_parts[1].strip()
                        if user_ans == correct_ans:
                            score += 1
                            st.write(f"Question {i}: Correct ✅")
                        else:
                            st.write(f"Question {i}: Incorrect ❌")
                    else:
                        st.write(f"Question {i}: Answer not found")

            st.write(f"Total Score: {score}/{len(attempted_questions)} 🎉")

            # Display answer key
            st.subheader("Answer Key:")
            for i, key_ans in enumerate(st.session_state["key_answers"], start=1):
                key_ans_parts = key_ans.split(". ")
                if len(key_ans_parts) > 1:
                    correct_ans = key_ans_parts[1].strip()
                    st.write(f"Q{i}. {correct_ans}")
                else:
                    st.write(f"Q{i}. Answer not found")

            # Clear session state
            del st.session_state["questions"]
            del st.session_state["key_answers"]
            del st.session_state["attempted_questions"]
            del st.session_state["submitted"]
            del st.session_state["user_answers"]

            # Add button to return to the home page
            if st.button("Back to Home"):
                st.session_state.clear()  # Clear session state
                st.experimental_rerun()  # Restart the app

if __name__ == "__main__":
    main()
