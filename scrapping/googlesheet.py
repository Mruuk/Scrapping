import gspread


def sheet_google():
  gc = gspread.service_account(filename='credentials.json')
  sh_id = '10RVlErMrLTMHkQiglSXu6o9fEaU1OYm2SWXwC7KycfU'

  
  csv = open('jobs.csv','r').read().encode('utf8')
  gc.import_csv(sh_id, csv)


  