from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from pprint import pprint
from langchain_community.document_loaders import JSONLoader
from langchain_community.vectorstores import FAISS
import summarise as summ

def search_with_faiss(query):
    embeddings = HuggingFaceEmbeddings()
    # try:
    #     faiss_index = FAISS.load_local(
    # "faiss_index", embeddings, allow_dangerous_deserialization=True
    # )

    # except:
    file_path='searchResults/scraped_data.json'
    loader = JSONLoader(
    file_path=file_path,
    jq_schema='.results[]',
    text_content=False)

    pages = loader.load_and_split()

    faiss_index = FAISS.from_documents(pages, embeddings)
    faiss_index.save_local("faiss_index")

    retriever = faiss_index.as_retriever(k=2)
    docs = retriever.invoke(query, k=2)
    return docs

if __name__ == '__main__':
    query = "how to make a website"
    docs = search_with_faiss(query)
    # print((docs[0].page_content))
    for doc in docs:
        title = doc.page_content
        print(type(title))