from flask import Flask, render_template, request
import random
from googlesearch import search
import webbrowser


app = Flask(__name__, template_folder='template')
app.static_folder = 'static'

def get_google_search_results(query):
    search_results = list(search(query, num=5, stop=5, pause=2))
    return search_results

def get_chatbot_response(user_text):
    # Check if the user's input is a Google search request
    if user_text.lower().startswith("google "):
        query = user_text[7:]  # Extract the query after "google "
        results = get_google_search_results(query)
        if results:
            return f"Here are some search results:\n{'\n'.join(results)}"
        else:
            return "No results found."
    else:
        # Add your existing chatbot logic here
        return "Your chatbot response goes here."

@app.route("/")
def home():
    return render_template("index.html")

def open_browser():
    webbrowser.open_new('http://127.0.0.1:5000/')

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    response = get_chatbot_response(user_text)
    return response

if __name__ == "__main__":
    open_browser()
    app.run()
