from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

def generate_description_openai(product_name, keywords, tone="neutral"):
    # Clean up the keywords list (remove extra whitespace)
    keywords_list = [kw.strip() for kw in keywords]
    
    # Construct the prompt using the product name, keywords, and tone.
    prompt = (
        f"Write a compelling product description for '{product_name}', "
        f"incorporating these keywords: {', '.join(keywords_list)}. "
        f"Use a {tone} tone.\n\nProduct Description:"
    )
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=150,
            n=1,
            temperature=0.7,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/', methods=['GET', 'POST'])
def index():
    description = None
    if request.method == 'POST':
        product_name = request.form.get('product_name', '')
        keywords = request.form.get('keywords', '').split(',')
        tone = request.form.get('tone', 'neutral')
        
        if product_name and keywords:
            description = generate_description_openai(product_name, keywords, tone)
    return render_template('index.html', description=description)

if __name__ == '__main__':
    app.run(debug=True)
