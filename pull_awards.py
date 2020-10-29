from pymongo import mongo_client
from requests import get as get_req
from pymongo import MongoClient

with open("key.txt", "r") as file:
    headers_dict = {"X-TBA-Auth-Key": file.read()}

db = MongoClient().analyze_awards

team_list = [118, 125, 148, 254, 503, 694, 701, 846, 900, 971, 1114, 1323, 1481, 1678, 1868, 1902, 1967, 2056, 2073, 2135, 2265, 2412, 3132, 3250, 3476, 4575, 5458, 7667]


for team_num in team_list:
    award_list = get_req(f"https://www.thebluealliance.com/api/v3/team/frc{team_num}/awards", headers=headers_dict)
    if isinstance(award_list.json(), list):
        db.team_awards.update_one({"team_num": team_num}, {"$set": {"awards": award_list.json()}}, upsert=True)