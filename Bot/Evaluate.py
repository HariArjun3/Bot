def evaluate(self, question):
    total_questions = len(question)
    if 'question_index' not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.answers = []
    if st.session_state.question_index < total_questions:
        for i in range(st.session_state.question_index, total_questions):
            if question[i]:
                st.write(f"Question {i + 1}/{total_questions}: {question[i]}")
                st.session_state.question_index = i
                break
        answer = st.text_area("Your Answer:", key='answer_input').strip()
        if answer:
            st.session_state.answers.append(answer)
        if st.button("Next"):
            st.session_state.question_index += 1
    else:
        st.write("You have completed all the questions!")
        st.write("Your answers:")
        for i, answer in enumerate(st.session_state.answers):
            st.write(f"Answer {i + 1}: {answer}")