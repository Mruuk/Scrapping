import requests
from bs4 import BeautifulSoup

#settings
url_base = 'https://br.indeed.com/empregos?'
results_per_page = 50

def search_ideed(keyword):
  #url + request
  r_indeed = requests.get(f'{url_base}q={keyword}&limit=50&start=0')
  html_indeed = r_indeed.text
  #make a soup
  soup = BeautifulSoup(html_indeed, 'html.parser')
  #pega todos links do menu de navegacao
  pages_links = soup.find("ul", class_="pagination-list").find_all('a')
  #cria lista com numeros do menu (paginas)
  number_of_pages = [0, 1]
  for link in pages_links:
    n_page = link.string
    if n_page == None:
      continue
    number_of_pages.append(int(n_page))
  #com a lista de numero de paginas cria as url em lista
  urls = []
  for n_page in number_of_pages:
    url = f"{url_base}q={keyword}&limit=50&start={results_per_page * n_page}"
    urls.append(url)
  #envia as urls para scrapping
  return scrapping_indeed(urls)


def scrapping_indeed(urls):
  all_jobs = []
  #para cada url recebina faça:
  for url in urls:
    print("começando uma url Indeed....")
    #url + request
    r_indeed = requests.get(url)
    #salva o html no html_indeed
    html_indeed = r_indeed.text
    #faz a sopa
    soup = BeautifulSoup(html_indeed, 'html.parser')
    #filtrar os card. criar lista de cards
    cards = soup.find_all('div', class_="result")
    for card in cards:  
      company = card.find('span', class_='company')
      if company == None:
        company = 'Não encontrada.'
      else:
        company = company.get_text().strip()
      #monta o job
      job = {
        'title': card.find('a').get('title'),
        'company': company,
        'location': card.find('span', class_='location').string,
        'how_old': card.find('span', class_='date').string,
        'link': f"https://br.indeed.com{card.find('a').get('href')}"
      }
      #add o job na lista all_jobs
      all_jobs.append(job)
  #retorna a lista com todos os jobs
  return all_jobs
