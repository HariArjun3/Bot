from Bot import ResumeBot
from Clean_Resume import clean_resume
from Question_Generation import question_generation
# from Evaluate import evaluate
from Question_generator import question_generator
import Percentage as ms
import Config_file as cf
import streamlit as st
import Experience_checker as ec


def main():
    bot = ResumeBot()
    bot.greet()
    if bot.name:
        resume_text = bot.resume()
        if resume_text:
            file = cf.config_file()
            if file:
                skills = ms.skill_config(file)
                matched_skills = ms.matched_skills(resume_text, skills)
                percentage = ms.matching_skills(resume_text, skills)
                st.write(percentage)
                st.write(matched_skills)
                exp = ec.Experience()

                if 'question' not in st.session_state:
                    st.session_state['question'] = question_generator(matched_skills, exp)
                print('question', st.session_state['question'])
                st.write("All Questions:")

                if 'answers' not in st.session_state:
                    st.session_state['answers'] = {}  # Initialize an empty dictionary to store answers

                all_user_answers = {}  # Dictionary to store answers for all questions

                for idx, i in enumerate(st.session_state['question'], start=1):
                    st.write(f"Question {idx}: {i}")

                    text_area_key = f"text_area_{i}"
                    answer_text_area = st.text_area("Your Answers (Separate with commas):", key=text_area_key)

                # Single submit button at the end
                submit_button = st.button("Submit All Answers", key="submit_all")

                if submit_button:
                    try:
                        for idx, i in enumerate(st.session_state['question'], start=1):
                            user_answers = st.session_state[text_area_key].strip().split(',')
                            all_user_answers[i] = [answer.strip() for answer in user_answers]
                        # Update st.session_state['answers'] with all answers at once
                        st.session_state['answers'] = all_user_answers
                    except ValueError:
                        st.error("Please enter answers separated by commas for all questions.")

                st.write(f"Collected answers: {st.session_state['answers']}")
                if st.button("End Session"):
                    st.session_state.clear()


if __name__ == "__main__":
    main()
