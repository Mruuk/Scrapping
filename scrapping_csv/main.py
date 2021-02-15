from indeed import scrapping_indeed, search_keyword
from save import save_to_csv


result = search_keyword('python')
save_to_csv(result)