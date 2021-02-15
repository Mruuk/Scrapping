import requests
from bs4 import BeautifulSoup

#configuracoes
url_base = 'https://br.indeed.com/jobs?'
results_per_page = 50

def search_keyword(keyword):
  #1. faz a busca e descobre quantas paginas de resultado
  r_indeed = requests.get(f'{url_base}q={keyword}&limit=50&start=0')
  html_indeed = r_indeed.text
  soup = BeautifulSoup(html_indeed, 'html.parser')

  #descobrimos quantas paginas analisando o codigo
  pages_links = soup.find("ul", class_="pagination-list").find_all('a')

  #lista que armazena paginas
  number_of_pages = [0, 1]
  for link in pages_links:
    n_page = link.string
    if n_page == None:
      continue
    number_of_pages.append(int(n_page))

  urls = []
  for n_page in number_of_pages[:-1]:
    url = f"{url_base}q={keyword}&limit=50&start={results_per_page * n_page}"
    urls.append(url)

  return scrapping_indeed(urls)


def scrapping_indeed(urls):
  all_jobs = []
  for url in urls:
    print('começando uma url....')
    #url + request
    r_indeed = requests.get(url)
    #salva o html no html_indeed
    html_indeed = r_indeed.text
    #faz a sopa
    soup = BeautifulSoup(html_indeed, 'html.parser')
    #criar lista de cards
    cards = soup.find_all('div', class_="result")
    for card in cards:
      company = card.find('span', class_='company')
      if company == None:
        company = 'Não encontrada'
      else:
        company = company.get_text().strip()
    
      job = {
        'title': card.find('a').get('title'),
        'company': company,
        'location': card.find('span',class_='location').string,
        'how old': card.find('span',class_='date').string,
        'link': f"https://br.indeed.com{card.find('a').get('href')}"
      }
      all_jobs.append(job)
  return all_jobs