import re
from pymongo import MongoClient
team_list = [118, 125, 148, 254, 503, 694, 701, 846, 900, 971, 1114, 1323, 1481, 1678, 1868, 1902, 1967, 2056, 2073, 2135, 2265, 2412, 3132, 3250, 3476, 4575, 5458, 7667]
db = MongoClient().analyze_awards
# how many regional chairmans winners
regional_award_winners = 0
hall_of_fame = 0
champs = 0
total_awards = 0
dubs = 0
for team in team_list:
    total_awards += len(db.team_awards.find_one({'team_num': team})['awards'])
    for award in db.team_awards.find_one({'team_num': team})['awards']:
        if award["name"] == "Regional Chairman's Award":
            regional_award_winners += 1
            break
    for award in db.team_awards.find_one({'team_num': team})['awards']:
        if award["name"] == "Chairman's Award Winner":
            hall_of_fame += 1
            break
    for award in db.team_awards.find_one({'team_num': team})['awards']:
        if award["name"] == "Championship Winner":
            champs += 1
            break
    for award in db.team_awards.find_one({'team_num': team})['awards']:
        if award["award_type"] == 0:
            dubs += 1
print(regional_award_winners)
print(hall_of_fame)
print(champs)
print(total_awards)
print(dubs)
