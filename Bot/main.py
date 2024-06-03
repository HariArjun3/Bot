from Bor import ResumeBot
from Clean_Resume import clean_resume
from Question_Generation import question_generation
from Evaluate import evaluate
from Question_generator import question_generator
import streamlit as st


def main():
    bot = ResumeBot()
    bot.greet()
    bot.resume()


if __name__ == "__main__":
    main()