import streamlit as st
from langchain import LangChain
from prompttemplate import PromptTemplate

# Initialize LangChain Model
langchain_model = LangChain("gpt3")

# Initialize PromptTemplate
prompt_template = PromptTemplate()

# Define Prompts
prompt_template.add_prompt("intro", "Welcome to YourApp! How can I assist you today?")
prompt_template.add_prompt("ask_name", "What's your name?")

# Function to generate responses
def generate_response(user_input):
    response = ""
    if user_input.lower() == "hello":
        response = prompt_template.generate("intro")
    elif user_input.lower() == "name":
        response = prompt_template.generate("ask_name")
    else:
        response = langchain_model.generate(user_input)
    return response

# Main function to run the Streamlit app
def main():
    st.title("BaeFlix")
    st.write("AI: " + prompt_template.generate("intro"))
    user_input = st.text_input("You:")
    if user_input:
        response = generate_response(user_input)
        st.write("AI: " + response)

if __name__ == "__main__":
    main()
