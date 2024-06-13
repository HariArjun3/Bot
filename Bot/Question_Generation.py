import os
from openai import OpenAI
import re


def question_generation(questions,experience):
    client = OpenAI(
        api_key='sk-proj-WiYKJkjVE8Fw8cA0eybWT3BlbkFJTX5vHTDGzn5569zERZCl',
    )
    t = (f'{questions}interview Questions for each programming languages with {experience} level  and dont mention the language name in the '
         f'question')

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": t,
            }
        ],
        model="gpt-3.5-turbo",
    )
    question_answer = chat_completion.choices[0].message.content.splitlines()
    total = []
    for i in range(len(question_answer)):
        if question_answer[i].strip() == '':
            continue
        else:
            total.append(question_answer[i])
    question_answer = total
    question = []
    for i in range(len(question_answer)):
        question.append(question_answer[i])

    return question


# def answer_generation(questions):
#     client = OpenAI(
#         api_key='sk-proj-q90Vk8IpUcY9bn66odEtT3BlbkFJ4VYEjBHbxCDuy5oYuaGU',
#     )
#     t = f'{questions} give me answer for this question based on the language seperately in single line and give me title as language and  answer in next line'
#
#     chat_completion = client.chat.completions.create(
#         messages=[
#             {
#                 "role": "user",
#                 "content": t,
#             }
#         ],
#         model="gpt-3.5-turbo",
#     )
#
#     question_answer = chat_completion.choices[0].message.content.splitlines()
#     total = []
#     for i in range(len(question_answer)):
#         if question_answer[i].strip() == '':
#             continue
#         else:
#             total.append(question_answer[i])
#     return total


if __name__ == "__main__":
    question = question_generation(['C++','Python'])
    print(question)
    # answer = answer_generation(question)
    # print(answer)
