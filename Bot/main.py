from Bot import ResumeBot
from Clean_Resume import clean_resume
from Question_Generation import question_generation
from Question_generator import question_generator
import Percentage as ms
import Config_file as cf
import streamlit as st
import Experience_checker as ec
import Clean_Resume as cr
from pymongo import MongoClient
import hashlib


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

                client = MongoClient('localhost', 27017)
                db = client['Practice']
                collection = db['Bot']

                user_data = cr.clean_resume(resume_text)
                name = user_data['name']
                number = user_data['number']
                email = user_data['email']

                def generate_mongo_id_like(string):
                    hash_object = hashlib.sha256(string.encode())
                    return hash_object.hexdigest()

                _id = generate_mongo_id_like(name)
                if not collection.find_one({'_id': _id}):
                    collection.insert_one(
                        {'_id': _id, 'name': name, 'number': number, 'email': email,
                         'skills': matched_skills, 'percentage': percentage,
                         'experience': exp, 'question': question_generator(matched_skills, exp)})

                def PrintQuestion(_id):
                    client = MongoClient('localhost', 27017)
                    db = client['Practice']
                    collection = db['Bot']
                    answer = {}
                    for question in collection.find({'_id': _id}):
                        for i in question['question']:
                            st.write(f"Question: {i}")
                            answer[i] = st.text_input("Your Answer: ", key=f"{i}")
                    submit_button = st.button("Submit Answers")
                    if submit_button:
                        print(answer)
                        for key, value in answer.items():
                            collection.update_one({'_id': _id}, {'$set': {f'question.{key}': value}})

                PrintQuestion(_id)


if __name__ == "__main__":
    main()
