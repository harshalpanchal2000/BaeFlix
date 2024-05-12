import streamlit as st
from langchain import LangChain
from prompttemplate import PromptTemplate
import json

# Initialize LangChain Model
langchain_model = LangChain("gpt3")

# Initialize PromptTemplate
prompt_template = PromptTemplate()

# Define Prompts
prompt_template.add_prompt("intro", "Welcome to BaeFlix! How can I assist you today?")
prompt_template.add_prompt("ask_name", "What's your name?")

# Load conversation history from a JSON file
@st.cache
def load_conversation_history():
    try:
        with open("conversation_history.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save conversation history to a JSON file
def save_conversation_history(conversation_history):
    with open("conversation_history.json", "w") as file:
        json.dump(conversation_history, file)

# Function to generate responses
def generate_response(user_input, conversation_history):
    response = ""
    if user_input.lower() == "hello":
        response = prompt_template.generate("intro")
    elif user_input.lower() == "name":
        response = prompt_template.generate("ask_name")
    else:
        response = langchain_model.generate(user_input)
    
    # Add user input and AI response to conversation history
    conversation_history.append({"user_input": user_input, "ai_response": response})
    save_conversation_history(conversation_history)
    
    return response

# Main function to run the Streamlit app
def main():
    st.title("BaeFlix - Your AI Girlfriend")
    
    # Load conversation history
    conversation_history = load_conversation_history()
    
    # Display conversation history
    st.header("Conversation History")
    for interaction in conversation_history:
        st.write(f"User: {interaction['user_input']}")
        st.write(f"AI: {interaction['ai_response']}")
    
    st.header("Chat with Your AI Girlfriend")
    st.write("AI: " + prompt_template.generate("intro"))
    
    user_input = st.text_input("You:")
    if user_input:
        response = generate_response(user_input, conversation_history)
        st.write("AI: " + response)

if __name__ == "__main__":
    main()
