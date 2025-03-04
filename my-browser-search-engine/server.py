from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Allows frontend requests

app = Flask(__name__, static_folder='static')
CORS(app)  # Enable CORS

# ✅ Predefined search data
search_data = [
    {"title": "Example Domain", "url": "https://example.com", "description": "This is an example website."},
    {"title": "Python Official", "url": "https://www.python.org", "description": "Python is a programming language."},
    {"title": "Flask Framework", "url": "https://flask.palletsprojects.com", "description": "Flask is a web framework for Python."},
    {"title": "Valentine's Day Surprise", "url": "https://bhanu14ma2007.github.io/very/", "description": "A Valentine's Day special website."},
    {"title": "Amazon", "url": "https://www.amazon.com/", "description": "Amazon is a shopping website with a variety of products."}, 
    {"title": "Apple", "url": "https://www.apple.com", "description": "Official site for Apple products such as iPhones, MacBooks, iPads, and software services."}
]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("q", "").strip().lower()
    if not query:
        return jsonify([])  # Return empty response if query is empty

    # 🔍 Search in predefined dataset
    results = [item for item in search_data if query in item["title"].lower() or query in item["description"].lower()]
    
    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # ✅ Removed debug=True for production
