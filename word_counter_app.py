import streamlit as st

def word_count(text):
    # Split the input text into words and return the count
    words = text.split()
    return len(words)

# Streamlit app
st.title("Word Counter App")

# User input for sentence or paragraph
user_input = st.text_area("Enter a sentence or paragraph:")

# Button to trigger word count
count_button = st.button("Count Words")

# Check if the button is clicked and user input is not empty
if count_button and user_input:
    # Count words using the word_count function
    count = word_count(user_input)

    # Display word count
    st.subheader("Result:")
    st.write(f"Word Count: {count}")
elif count_button:
    # Display error message for empty input when the button is clicked
    st.subheader("Result:")
    st.write("Please enter a sentence or paragraph.")
