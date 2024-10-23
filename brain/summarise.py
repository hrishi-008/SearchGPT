from groq import Groq
from secrets22 import GROQ_API
import json

with open('../searchResults/scraped_data.json', 'r') as f:
    results = json.load(f)

def generate_summary(results, query, index):
    client = Groq(api_key=GROQ_API)
    completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "system",
            "content": f"""
            Your task is to accurately and concisely explain and elaborate on the content of the top search results related to the query: '{query}'. 
            You will receive input as scraped data from relevant websites. 
            Your output should be simple, clear, and easy to understand, even for someone with no prior knowledge of the topic. 
            Focus on providing the most relevant and informative explanation, avoiding any technical jargon. 
            Please exclude any promotional or irrelevant content. 
            The primary objective is to deliver high-quality, accessible information for the query: '{query}'.
            Here is the scraped data from the top website content results: {results}
            There are links in the scraped data, retain them in the output.
            If results say somehting related to denial of access, please ignore that and proceed with the next result.
            Current index: {index}
            RULE - OUTPUT SHOULD BE A MARKDOWN FORMATTED TEXT. RETAIN THE LINKS IN THE OUTPUT."""
        },
    ],
    temperature=0.6,
    max_tokens=1700,
    top_p=1,
    stream=False,
    stop=None,
    )

    return completion.choices[0].message.content

def main():
    for i in results['results']:
        title = i['title']
        link = i['link']
        text = i['text']
        # summary = generate_summary(text)
        print(f"Title: {title}\nLink: {link}\nSummary: {text}\n\n")

if __name__ == '__main__':
    main()
