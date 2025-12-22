def create_prompt():
    topic = input("Enter the topic: ")
    tone = input("Enter the tone(e.g. serious, humorous):")
    
    prompt = f"Write a {tone} story about {topic}."
    return prompt

user_prompt = create_prompt()
print("Generated Prompt: ", user_prompt)    
