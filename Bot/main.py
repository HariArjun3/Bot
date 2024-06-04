from Bot import ResumeBot
from Clean_Resume import clean_resume
from Question_Generation import question_generation
from Evaluate import evaluate
from Question_generator import question_generator
import Percentage as ms
import Config_file as cf
import streamlit as st


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
                que = question_generator(matched_skills)
                flag = False
                if not flag:
                    evaluate(question=que)
                    flag = True

                # st.write('Completed Thanks')


if __name__ == "__main__":
    main()
