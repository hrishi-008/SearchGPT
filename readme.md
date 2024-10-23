# **SummarAI (earlier SearchGPT)**

A tool for summarizing search results and website content using FAISS, LLMs, and the Retrieval-Augmented Generation (RAG) technique.

## **Overview**

Search GPT is a Streamlit-based application that automates the process of scraping Google search results, extracting content from websites, storing and retrieving information using FAISS (Facebook AI Similarity Search), and summarizing the content using a language model. This tool leverages the Retrieval-Augmented Generation (RAG) technique to provide concise and easy-to-understand summaries of web content based on user queries. While the github version uses FAISS, the dockerised veriosn uses ANNOY (Approximate Nearest Neighbors Oh Yeah) for retrieval, everythig else remains same. This is done to improve the speed of making the vector DB, althuogh at the cost of the quality of retrieved documents.

## **Demo**

[Search GPT Demo](https://github.com/user-attachments/assets/141db33d-22c0-41a7-a546-fe8fe01f717b)

## **Features**

- **Google Search Scraping**: Automatically scrapes Google search results for a given query.
- **Website Content Extraction**: Scrapes and extracts relevant content from the search result links.
- **FAISS Database Integration**: Stores and retrieves scraped data efficiently using FAISS.
- **Content Summarization with RAG**: Uses the RAG technique to generate summaries by combining retrieved content with a language model, ensuring accurate and context-aware summaries.
- **Streamlit Interface**: Provides a simple web interface for users to input queries and receive summarized results.

## **Dockerization**

The Search GPT application has been Dockerized for easier deployment and management. You can now run the entire application within a Docker container without manually installing dependencies or setting up the environment.

### **Docker Image**

The official Docker image is available on Docker Hub:

**Docker Hub Link**: [hrishi700/search_gpt](https://hub.docker.com/repository/docker/hrishi700/search_gpt/general)

### **Pulling the Image**

To pull the image from Docker Hub, use the following command:

```bash
docker pull hrishi700/search_gpt:v2
```

### **Running the Container**

You can run the application using Docker with the following command:

```bash
docker run -p 8000:8000 hrishi700/search_gpt:v2
```

This will expose the app on port 8000. You can access the Streamlit interface by navigating to:

```
http://localhost:8000
```

## **Setup and Installation**

### **Prerequisites**

If you prefer running the app without Docker, you will need:

- Python 3.11 or higher
- Required Python packages (can be installed via `requirements.txt`)

### **Installation Steps (Non-Docker)**

1. Clone the Repository:

```bash
git clone https://github.com/hrishi-008/SearchGPT.git
cd SearchGPT
```

2. Install Dependencies:

```bash
pip install -r requirements.txt
```

3. Add your GROQ API:

- Add your GROQ-API in the `brain/secrets22.py`
- PS: Name this file anything but `secrets.py`!!

4. Run the Application:

```bash
streamlit run brain/full_pipe.py
```

## **Usage**

1. **Enter Query**: Input your search query in the text box provided in the Streamlit interface.
2. **Search and Summarize**: Click on the "Search and Summarize" button to initiate the process.
3. The application will scrape Google search results, extract content from relevant websites, summarize the information using the RAG technique, and display it on the screen.
4. **View and Save Summaries**: The summarized content is displayed on the interface. The summary is also saved in `searchResults/summary.md` for later reference.

## **Project Structure**

- `full_pipe.py`: The main script that runs the Streamlit application.
- `google_search_results.py`: Module for scraping Google search results and saving them in `gsearch_results.json`.
- `scrape_websites.py`: Module for scraping content from the websites listed in `gsearch_results.json`, saving the content in `scraped_data.json`.
- `faiss_db.py`: Module for interacting with the FAISS database, storing, and retrieving the scraped data.
- `summarise.py`: Module for generating summaries of the website content using the RAG technique based on the user query.
- `searchResults/`: Directory where the summarized content is saved as `summary.md`, and other json files.

## **Future Scope**

- Improving retrieval process in terms of speed and quality.
- Hosting it on cloud service for accessibility and testing.
- Implementing a feature to provide summaries for the top 3 websites by passing individual content through a retriever.
- Improving UI.

## **Contact**

For any questions or suggestions, please contact:

- [LinkedIn](https://www.linkedin.com/in/hrishk)
