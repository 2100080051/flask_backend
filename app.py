from flask import Flask, request, jsonify
from flask_cors import CORS
from utils import search_articles, concatenate_content, generate_answer

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "✅ Flask backend is running!"

@app.route('/ask', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        query = data.get("query", "")

        if not query:
            return jsonify({"error": "No query provided"}), 400

        # Step 1: Search articles
        articles = search_articles(query)

        # Step 2: Combine content
        context = concatenate_content(articles)

        # Step 3: Generate answer
        answer = generate_answer(context, query)

        return jsonify({"answer": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
