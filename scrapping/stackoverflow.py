import requests
from bs4 import BeautifulSoup

#settings
url_base = 'https://stackoverflow.com/jobs?'
results_per_page = 50

def search_so(keyword):
  #url + request
  r_so = requests.get(f'{url_base}q={keyword}')
  html_so = r_so.text
  #make a soup
  soup = BeautifulSoup(html_so, 'html.parser')
  #pega todos links do menu de navegacao
  pages_links = soup.find("div", class_="s-pagination").find_all('a')
  last_pages = int(pages_links[-2].find('span').string)
  all_pages = range(1, last_pages)
  #pega os links e cria as urls
  urls = []
  for n_page in all_pages:
    if n_page == 1:
      url = f'{url_base}q={keyword}'
    else:
      url = f'{url_base}q={keyword}&pg={n_page}'
    urls.append(url)
  #envia as urls para scrapping
  return scrapping_so(urls)

def scrapping_so(urls):
  all_jobs = []
  #Para cada url recebida faça:
  for url in urls:
    print("começando uma url Stack Overflow....")
    #url + request
    r_so = requests.get(url)
    #salva o html no html_indeed
    html_so = r_so.text
    #faz a sopa
    soup = BeautifulSoup(html_so, 'html.parser')
    #filtrar os card. criar lista de cards
    cards = soup.find_all('div', class_="-job")
    for card in cards:  
      #Monta o job
      job = {
        'title': card.find('a', class_='s-link').get('title'),
        'company': card.find('h3', class_='fc-black-700').find_all('span')[0].string,
        'location': card.find('h3', class_='fc-black-700').find_all('span')[1].string,
        'how_old': card.find('ul', class_='mt4').find('li').string,
        'link': f"https://stackoverflow.com/{card.find('a', class_='s-link').get('href')}"
      }
      #adiciona o job em all_jobs
      all_jobs.append(job)
  #retorna all_jobs
  return all_jobs
