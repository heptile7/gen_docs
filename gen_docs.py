import openai
import os
api_key = os.getenv('OPENAI_API_KEY')
client = openai.OpenAI(api_key=api_key)

def generate_code_documentation(code):
    # Specify the prompt with the code for documentation generation
    prompt = f"Generate documentation for the following code:\n\n{code}"
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
            "role": "system",
            "content": "Provide functional documentation for python code."
            },
            {
            "role": "user",
            "content": code
            }
        ],
        # temperature=0.7,
        # max_tokens=64,
        # top_p=1
        )

    # Extract and print the generated documentation
    generated_documentation = response.choices[0].message
    return generated_documentation.content

def combine_txt_files(directory_path, output_file_path):
    with open(output_file_path, 'w') as output_file:
        for filename in os.listdir(directory_path):
            if filename.endswith(".txt") and not os.path.join(directory_path, filename) == output_file_path:
                file_path = os.path.join(directory_path, filename)
                with open(file_path, 'r') as input_file:
                    output_file.write(file_path)
                    output_file.write(input_file.read() + '\n')

def all_codes():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py') and not root.startswith('.\\venv') and not file.startswith('gen_docs.py'):
                print(os.path.join(root, file))
                code = open(os.path.join(root, file)).read()
                code_doc = generate_code_documentation(str(code))
                with open(f"docs\\{file.rstrip('.py')}_documentation.txt","w") as doc:
                    doc.write(code_doc)
    
    # Combine all code documents
    combine_txt_files('.\docs', r'.\docs\full_docs.txt')



if __name__ == "__main__":
    all_codes()

