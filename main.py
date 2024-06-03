import io
import re
from pdfminer3.converter import TextConverter
from pdfminer3.layout import LAParams
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfpage import PDFPage
from pymongo import MongoClient
from Bot.Question_Generation import question_generation

client = MongoClient('localhost', 27017)
db = client['Chatbot']
collection = db['Bot']


def skill_config(file):
    li = []
    with open(file, 'r') as file:
        for skill in file:
            li.append(skill.strip())
        return li


def pdf_reader(file):
    resource_manager = PDFResourceManager()
    fake_file_handle = io.StringIO()
    converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
    page_interpreter = PDFPageInterpreter(resource_manager, converter)

    try:
        with open(file, 'rb') as fh:
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                page_interpreter.process_page(page)

        text = fake_file_handle.getvalue()
        converter.close()
        fake_file_handle.close()
        return text
    except FileNotFoundError:
        print("Error: Resume file not found.")
        return None


def clean_resume(resume_text):
    name = re.findall(r'\b([A-Z][a-z]+(?: [A-Z]\.)? [A-Z][a-z]+)\b', resume_text)
    number = re.findall(r'(?:\+?\d{1,2} \()?[-.\s]?\d{3}[-\.\s]?\d{3,10}', resume_text)
    email_pattern = re.findall(r'\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b', resume_text)

    if not any([name, number, email_pattern]):
        print("Warning: No name, number, or email found in resume.")

    return {'name': name[0] if name else None, 'number': number[0] if number else None,
            'email': email_pattern[0] if email_pattern else None}


def search_and_calculate_percentage(text, skills_list):
    found = False
    total_skills = 0
    matched_skills = []

    for skill in skills_list:
        if skill.lower().strip() in text.lower().strip():
            found = True
            total_skills += 1
            matched_skills.append(skill)

    percentage = (total_skills / len(skills_list)) * 100
    return f"Skills found: {percentage:.2f}%"


def store_in_mongo(data):
    try:
        collection.insert_one(data)
        print("Data saved to MongoDB successfully.")
    except Exception as e:
        print(f"Error saving data to MongoDB: {e}")


def get_data():
    all_doc = collection.find()
    for doc in all_doc:
        print(doc['name'], "\n",
              doc['number'], "\n",
              doc['email'], "\n",
              doc['skills'], "\n",
              doc['percentage'])


def generate_question(skill):
    get_input = question_generation(skill)
    return get_input


if __name__ == '__main__':
    skills = skill_config('skills.txt')
    resume_text = pdf_reader("Hari's_Resume.pdf")
    print(resume_text)
    cleaned_data = clean_resume(resume_text)
    percentage = search_and_calculate_percentage(resume_text, skills)
    que = generate_question(skills)
    data = {'name': cleaned_data['name'], 'number': cleaned_data['number'], 'email': cleaned_data['email'],
            'skills': skills, 'percentage': percentage, }
    store_in_mongo(data)
    # get_data()
    print(cleaned_data)
    print(que)
