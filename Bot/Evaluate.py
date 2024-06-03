import streamlit as st



def evaluate(question):
    print('question', question)
    answers = {}
    questions = question
    # Get the first question
    # question = get_question()

    # Ask the user the current question and get the answer
    answer = st.text_input(question)

    # Store the current question and answer in the dictionary
    answers[question] = answer

    # Display a submit button
    if st.button("Submit"):
        # Print the dictionary of questions and answers
        st.write("Answers:", answers)

        # Reset the answers dictionary for the next questionnaire
        answers.clear()

        # Check if there are more questions
        if questions:
            # Get the next question
            question = questions.pop(0)


# st.write("User answers:", user_answers)
