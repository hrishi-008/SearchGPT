from flask import Flask, request, jsonify
from flask_cors import CORS
import google_search_results as gsr
import scrape_websites as scraper
import summarise as summ
import faiss_db as db

class SearchGpt:
    def __init__(self, query):
        self.query = query
        self.googler = gsr
        self.scraper = scraper
        self.summariser = summ
        self.db = db
        self.results = []
        self.index = 1

    def get_results(self, index=1):
        self.index = index
        self.googler.google_search(self.query)
        self.scraper.parse_search_results()
        docs = self.db.search_with_faiss(self.query)
        for doc in docs:
            summary = self.summariser.generate_summary(doc.page_content, self.query, self.index)
            self.results.append(summary)
            self.index += 1
        with open('searchResults/summary.md', 'w') as f:
                    for result in self.results:
                        f.write(result + "\n")
        return self.results
    

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search():
    query = request.json.get('query')
    search = SearchGpt(query)
    results = search.get_results()
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
