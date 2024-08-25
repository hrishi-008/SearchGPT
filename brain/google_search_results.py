from selenium import webdriver
from selenium.webdriver.common.by import By
import time, json
from selenium.webdriver.chrome.options import Options

def google_search(query):
    """
    Perform a Google search and save the top 5 results to a JSON file.
    Args:
        query (str): The search query to be used.
    Returns:
        None
    Raises:
        None
    Example Usage:
        google_search("GitHub Copilot")
    """
    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(f'https://www.google.com/search?q={query}')
    driver.implicitly_wait(5)

    button = driver.find_element(By.CLASS_NAME, 'Lu57id')
    button.click()
    time.sleep(1)

    button2 = driver.find_element(By.LINK_TEXT, 'Web')
    button2.click()

    driver.implicitly_wait(5)

    # Get the top 5 results
    results = driver.find_elements(By.CSS_SELECTOR, 'div.g')

    variable = {
        'query': query,
        'results': []
    }

    for i, result in enumerate(results):
        title = result.find_element(By.CSS_SELECTOR, 'h3').text
        link = result.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
        #  save the results to a json variable
        variable['results'].append({'title': title, 'link': link})
        if i == 11:
            break

    # Save the results to a json file
    with open('searchResults/gsearch_results.json', 'w') as f:
        json.dump(variable, f)

    # Close the browser
    driver.quit()

def main():
    google_search('how to cook pizza at home')

if __name__ == '__main__':
    main()