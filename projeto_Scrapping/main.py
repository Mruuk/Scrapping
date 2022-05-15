from indeed import search_ideed
from stackoverflow import search_so
from save import save_to_csv
from googlesheet import sheet_google

#busca
search = 'python'

#salva resultado do indeed
result_indeed = search_ideed(search)
#salva resultado do indeed
result_so = search_so(search)

#junta os resultados em all_results
all_results = result_indeed + result_so

#envia para salvar no csv
save_to_csv(all_results)

#salvar o csv no googlesheet
sheet_google()