import gspread


def sheet_google():
  gc = gspread.service_account(filename='credentials.json')
  sh_id = 'your id'

  
  csv = open('jobs.csv','r').read().encode('utf8')
  gc.import_csv(sh_id, csv)


  
