import openai
import os
from openai import OpenAI

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

def generate_project_docs():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py') and not root.startswith('.\\venv') and not file.startswith('gen_docs.py'):
                print(os.path.join(root, file))
                code = open(os.path.join(root, file)).read()
                code_doc = generate_code_documentation(str(code))
                with open(f"docs\\{file.rstrip('.py')}_documentation.txt","w") as doc:
                    doc.write(code_doc)

def generate_business_use_case():
    combine_txt_files('.\docs', r'.\docs\full_docs.txt')
    with open(r".\docs\full_docs.txt","r") as full_doc:
        full_docs = full_doc.read()
    prompt = f"The :\n\n{full_docs}"

    client = OpenAI()

    with open(".\README.md","r") as readme:
        readme_content = readme.read()

    prompt = f"The Readme file for the project is:\n{readme_content}.\n The code documentation for the project is:\n{full_docs}"
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
            "role": "system",
            "content": "Your task is to understand the code documentation and pitch to a business client two use-cases in detail where it can be used"
            },
            {
            "role": "user",
            "content": prompt
            }
        ],
        temperature=0.5,
        # max_tokens=10000,
        )

    # Extract and print the generated documentation
    generated_documentation = response.choices[0].message

    with open('prompt_.txt','w') as genai:
        genai.write(str(generated_documentation.content))
    return generated_documentation.content

def all_codes():
    # generate_project_docs()

    use_case = generate_business_use_case()
    print(use_case)




if __name__ == "__main__":
    all_codes()

