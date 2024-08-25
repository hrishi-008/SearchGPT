import json
import requests
from bs4 import BeautifulSoup as bs

def parse_search_results():
    """
    Parses the search results from a JSON file and scrapes the content of each link.
    Returns:
        None
    Raises:
        FileNotFoundError: If the JSON file containing the search results is not found.
    """
    # read results.json
    with open('searchResults/gsearch_results.json', 'r') as f:
        results = json.load(f)

    query = results['query']

    variable = {
        'query': query,
        'results': []
    }


    for i in results['results']:
        title = i['title']
        link = i['link']
        content = requests.get(link).text
        soup = bs(content, 'html.parser')
        body = soup.find('body')
        # print(body)
        try:
            text = body.get_text().strip()
            # remove unnecessary characters from the text including newlines and extra spaces
            text = ' '.join(text.split())

        except:
            text = 'Access Denied'
        #  save the results to a json variable
        variable['results'].append({'title': title, 'link': link, 'text': text})
    # Save the results to a json file
    with open('searchResults/scraped_data.json', 'w') as f:
        json.dump(variable, f)

def main():
    parse_search_results()

if __name__ == '__main__':
    main()
