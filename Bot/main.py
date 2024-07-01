from Bot import ResumeBot
from Clean_Resume import clean_resume
from Question_Generation import question_generation
from Question_generator import question_generator
import Percentage as ms
import Config_file as cf
import streamlit as st
from pymongo import MongoClient
import hashlib


def Experience():
    st.write("Experience Checker")
    note = st.selectbox("Select your Year of experience",
                        ["Fresher(0-2Y)", "Intermediate(2-4Y)", "Experienced(Above 4Y)",
                         "Expert(Above 10Y)"], key="experience_selectbox")
    if st.button('Submit', key="experience_submit_button"):
        return note
    else:
        return None


def generate_mongo_id_like(string):
    hash_object = hashlib.sha256(string.encode())
    return hash_object.hexdigest()


def PrintQuestion(_id):
    client = MongoClient('localhost', 27017)
    db = client['Practice']
    collection = db['Bot']
    answer = {}
    questions = collection.find_one({'_id': _id})['question']
    for i, question in enumerate(questions):
        st.write(f"Question: {question}")
        answer[question] = st.text_input("Your Answer: ", key=f"{question}_{i}")
    submit_button = st.button("Submit Answers", key="submit_answers_button")
    if submit_button:
        for key, value in answer.items():
            collection.update_one({'_id': _id}, {'$set': {f'answers.{key}': value}})
        st.success("Answers submitted successfully!")


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

                if 'experience' not in st.session_state:
                    exp = Experience()
                    if exp:
                        st.session_state.experience = exp
                else:
                    exp = st.session_state.experience

                if exp:
                    client = MongoClient('localhost', 27017)
                    db = client['Practice']
                    collection = db['Bot']

                    user_data = clean_resume(resume_text)
                    name = user_data['name']
                    number = user_data['number']
                    email = user_data['email']

                    _id = generate_mongo_id_like(name)
                    existing_entry = collection.find_one({'_id': _id})

                    if existing_entry:
                        collection.update_one({'_id': _id}, {'$inc': {'attended_count': 1}})
                    else:
                        collection.insert_one(
                            {'_id': _id, 'name': name, 'number': number, 'email': email,
                             'skills': matched_skills, 'percentage': percentage,
                             'experience': exp, 'question': question_generator(matched_skills, exp),
                             'attended_count': 1})

                    if 'answers' not in st.session_state:
                        st.session_state.answers = {}

                    PrintQuestion(_id)


if __name__ == '__main__':
    main()
