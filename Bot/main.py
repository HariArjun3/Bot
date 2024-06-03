from Bor import ResumeBot
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
            # cleaned_resume = clean_resume(resume_text)
            # skills = bot.skill_config('skills.txt')
            # matched_skills = bot.matched_skills(resume_text, skills)
            # st.write(bot.matching_skills(resume_text, skills))
            # que = bot.question_generator(matched_skills)
            # bot.evaluate(question=que)
            file = cf.config_file()
            if file:
                skills = ms.skill_config(file)
                # skills = ms.skill_config("C:/Users/Lenovo/PycharmProjects/Bot/skills.txt")
                matched_skills = ms.matched_skills(resume_text, skills)
                st.write(matched_skills)
                que = question_generator(matched_skills)
                e = evaluate(question=que)
                st.write('Completed Thanks')


if __name__ == "__main__":
    main()
