''' This is my first do-it-all-over project. ''' 

import math
import statistics

company_name: str = "Messiah school."
count_active_students: int = 200
has_international_presence: bool = True
average_client_satisfaction: float = 4.9
services_offered: list = ["Day care", "ECDC", "Elementary"]
satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]


active_projects_string: str = f"Active Projects: {count_active_students}"
international_presence_string: str = f"International Presence: {has_international_presence}"
client_satisfaction_string: str = f"Average Client Satisfaction: {average_client_satisfaction}"

import statistics

smallest= min(satisfaction_scores)
largest= max(satisfaction_scores)
total= sum(satisfaction_scores)
count= len(satisfaction_scores)
mean= statistics.mean(satisfaction_scores)
mode= statistics.mode(satisfaction_scores)
median= statistics.median(satisfaction_scores)
standard_deviation=statistics.stdev(satisfaction_scores)

stats_string: str = f"""
Descriptive Statistics for Our Satisfaction Scores:
  Smallest: {smallest}
  Largest: {largest}
  Total: {total}
  Count: {count}
  Mean: {mean}
  Mode: {mode}
  Median: {median}
  Standard Deviation: {standard_deviation}
"""

byline: str = f"""
Name: {company_name}
Active students:{count_active_students}
International presence: {international_presence_string}
Client satisfaction: {client_satisfaction_string}
Services offered: {services_offered}
{stats_string}
"""

def main():
  ''' Display all output'''
  print(company_name)
  print(count_active_students)
  print(international_presence_string)
  print(client_satisfaction_string)
  print(services_offered)
  print(stats_string)

  # If all of the above works, then the byline should work too:
  print(byline)

if __name__ == '__main__':
  main()