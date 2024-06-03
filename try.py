import streamlit as st


def Evaluate(self, get_coding_questions):
    questions = get_coding_questions()
    total_questions = len(questions)

    # Initialize session state variables
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0

    if 'answers' not in st.session_state:
        st.session_state.answers = []

    # Function to handle the submission of an answer
    def handle_submission():
        answer = st.session_state.answer_input.strip()
        if answer:
            st.session_state.answers.append(answer)
            st.session_state.answer_input = ""  # Clear the input box
            if st.session_state.question_index < total_questions - 1:
                st.session_state.question_index += 1
            else:
                st.session_state.question_index += 1  # Move past the last question to show completion message

    # Display the current question or completion message
    if st.session_state.question_index < total_questions:
        current_question = questions[st.session_state.question_index]
        st.write(f"Question {st.session_state.question_index + 1}/{total_questions}: {current_question}")

        # Text area for the user's answer
        st.text_area("Your Answer:", key='answer_input', on_change=handle_submission)
    else:
        st.write("You have completed all the questions!")
        st.write("Your answers:")
        for i, answer in enumerate(st.session_state.answers):
            st.write(f"Answer {i + 1}: {answer}")

    # Button to go to the next question
    if st.session_state.question_index < total_questions and st.button("Next"):
        handle_submission()
        st.experimental_rerun()


if __name__ == "__main__":
    Evaluate()