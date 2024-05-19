user_query = st.text_input("Ask about local businesses")
if st.button("Send Query"):
  if user_query:
    response = query_ollama3(user_query)  # Call the function with user input
    st.write("Response:", response)
