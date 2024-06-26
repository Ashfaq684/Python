from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
website = f'{root}/movies_letter-A'
result = requests.get(website)
content = result.text
soup = BeautifulSoup(content, 'lxml')

# Pagination
pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
last_page = pages[-2].text

links = []

for page in range(1, int(last_page) + 1)[:2]:
    page_url = f'{website}?page={page}'
    result = requests.get(page_url)
    content = result.text
    soup = BeautifulSoup(content, 'lxml')
    
    box = soup.find('article', class_='main-article')
    
    for link in box.find_all('a', href=True):
        links.append(link['href'])

    for link in links:
        try:
            print(link)
            result = requests.get(f'{root}/{link}')
            content = result.text
            soup = BeautifulSoup(content, 'lxml')
            
            box = soup.find('article', class_='main-article')
            title = box.find('h1').get_text()
            transcript = box.find('div', class_='full-script').get_text(strip=True, separator='\n')
            
            filename = f"{title}.txt".replace('/', '_').replace(':', '').replace('?', '')
            
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(transcript)
        except requests.RequestException as e:
            print(f"Error scraping {link}: {e}")
        except AttributeError:
            print(f"Transcript not found for {link}")
