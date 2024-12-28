
import requests
from flask import Flask, request, jsonify, render_template
import os
from langchain import PromptTemplate, LLMChain
from langchain_community.llms import CTransformers
from fredapi import Fred

app = Flask(__name__, template_folder='template')
news_api_key = os.environ.get('news_api_key')
fred_api_key = os.environ.get('fred_api_key')

local_llm = "neural-chat-7b-v3-1.Q4_K_M.gguf"

config = {
    'max_new_tokens': 1024,
    'repetition_penalty': 1.1,
    'temperature': 0.1,
    'top_k': 50,
    'top_p': 0.9,
    'stream': True,
    'threads': int(os.cpu_count() / 2)
}

llm = CTransformers(
    model=local_llm,
    model_type="mistral",
    lib="avx2",  # for CPU use
    **config
)

print("LLM Initialized...")

prompt_template = """Use the following pieces of information to answer the user's question.
If you don't know the answer, just say that you don't know, don't try to make up an answer.

Context: {context}
Question: {question}

Only return the helpful answer below and nothing else.
Helpful answer:
"""

prompt = PromptTemplate(template=prompt_template, input_variables=['context', 'question'])


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/get_response', methods=['POST'])
def get_response():
    query = request.form.get('query')
    category = request.form.get('category')
    print("Category: ",category)

    context = ""
    source=" "
    answer=" "

    if category == 'stock':
        response = call_yahoo_finance_api(query)

    elif category == 'finance':
        print("Finance API being called")
        response= call_news_api(query)
        print("Response Generated:", answer)
        context = response.get('articles', [])
        print("Context:", context)
        source = "News Api"
        print("Source:",source)
        print("Finance API call complete")

    elif category == 'economic':
        response = call_fred_api(query)
        print("Response Generated:", answer)
        context = response.get('articles', [])
        print("Context:", context)
        source = "Fred Api"
        print("Source:", source)
        print("Fred Api call ended")
    else:
        response = {
            "answer": "Sorry, I can't help with that! We assure you to improve ourselves. Till then, ask something else."}



    response_data = {
        "answer": response,
        "source": source,
        "context": context,
    }
    return jsonify(response_data)


def call_yahoo_finance_api(query):
    # Implement this function
    pass


def call_news_api(query):
    url = 'https://newsapi.org/v2/everything?'
    parameters = {
        'q': query,  # query phrase
        'pageSize': 20,
        'langauge':'en',# maximum is 100
        'apiKey': news_api_key  # using the API key from environment variable
    }
    response = requests.get(url, params=parameters)

    if response.status_code == 200:
        data = response.json()  # Parse the JSON response
        return data  # Return the data as JSON
    else:
        return {"error": "Failed to fetch news articles."}


def call_fred_api(query):
    print("Fred Api called")
    fred = Fred(api_key=fred_api_key)
    try:
        # Assuming the query is a valid FRED series code, like 'SP500'
        data = fred.get_series(query)

        # If the data is retrieved successfully
        if data is not None:
            # Returning the latest available data (last date and value)
            latest_value = data.iloc[-1]  # Get the most recent value
            latest_date = data.index[-1]
            print(latest_value)
            print(latest_date)# Get the date corresponding to that value
            return {
                "date": latest_date.strftime('%Y-%m-%d'),
                "value": latest_value
            }
        else:
            return {"error": "No data found for the provided series code."}

    except Exception as e:
        return {"error": f"An error occurred: {str(e)}"}


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
