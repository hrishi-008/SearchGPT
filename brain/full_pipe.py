'''
TODO
1. selelnium link scraper - google_search_results.py --> gsearch_results.json
2. join above with website scraper - scrape_websites.py --> scraped_data.json
3. pass scraped_data.json to faiss db. Use faiss_db.py
4. take query pass to faiss db and the llm --> summarise.py
5. Display summarised content along with the links
6. FUTURE SCOPE - Give summary for top 3 websites 
    * This can be done by giving individual content of the website through a retriever.
'''
import streamlit as st
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
        return self.results

def main():
    st.title("Search GPT")
    st.write("A tool for summarizing search results and website content using FAISS and LLMs.")

    query = st.text_input("Enter your search query:", value="Best holiday destinations in India, Diwali")
    
    if st.button("Search and Summarize"):
        search = SearchGpt(query)
        results = search.get_results()
        if results:
            st.write("### Summary of Search Results:")
            for i, result in enumerate(results, 1):
                with st.expander(f"# Result {i}"):
                    st.write(result)

            # Save the summaries to a markdown file
            with open('searchResults/summary.md', 'w') as f:
                for result in results:
                    f.write(result + "\n")
            st.success("Summary saved to searchResults/summary.md")

if __name__ == '__main__':
    main()
