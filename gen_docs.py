import openai
import os
api_key = os.getenv('OPENAI_API_KEY')
api_key = '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'
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

def all_codes():
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.py') and not root.startswith('.\\venv') and not file.startswith('gen_docs.py'):
                print(os.path.join(root, file))
                code = open(os.path.join(root, file)).read()
                code_doc = generate_code_documentation(str(code))
                with open(f"docs\\{file.rstrip('.py')}_documentation.txt","w") as doc:
                    doc.write(code_doc)


if __name__ == "__main__":
    # Replace this with the actual code you want to document
    sample_code = """def add_numbers(a, b):\n\treturn a + b\n\nresult = add_numbers(3, 4)\nprint(result)"""
    # file = "reports/report_generator.py"
    # code = open(file).read()
    all_codes()

    # Generate code documentation
    # code_doc = generate_code_documentation(str(code))
    # with open(f"{file}_documentation.txt","w") as doc:
        # doc.write(code_doc)