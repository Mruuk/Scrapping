import csv


def save_to_csv(jobs):
  file = open('jobs.csv', 'w')
  writer = csv.writer(file)
  writer.writerow(['title','company', 'location', 'how old', 'link'])
  #writer.writerow(list(jobs.keys()))

  for job in jobs:
    writer.writerow(list(job.values()))
