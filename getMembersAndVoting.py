import requests
import json
import csv
import pandas

headers = {
    'X-API-Key': 'REPLACE_WITH_YOUR_KEY',
}

accessing = (115, 'senate') # replace left argument with number, right with 'senate' or 'house'

#optionally loop for more senates
member_url = "https://api.propublica.org/congress/v1/%d/%s/members.json" % accessing
member_ids = requests.get(member_url, headers=headers).json()


#populate idlist with all ids for this session of congress
idlist = []
names = []
for i in range(int(member_ids['results'][0]['num_results'])):
    currMember = member_ids['results'][0]['members'][i]

    idlist.append(currMember['id'])
    if currMember['middle_name'] is None:
        names.append(currMember['first_name'] + ' ' + currMember['last_name'])
    else:
        names.append(currMember['first_name'] + ' ' + currMember['middle_name'] + ' ' + currMember['last_name'])

# get bill names, done only once
bills = ['Congressmen']
billsjson = requests.get("https://api.propublica.org/congress/v1/members/%s/votes.json" % idlist[0], headers=headers).json()

for i in range(int(billsjson['results'][0]['num_results'])):
    bills.append(billsjson['results'][0]['votes'][i]['description'])


# get all voting data for each member in idlist
# rows = congressmen
# cols = votes
num_bills = requests.get("https://api.propublica.org/congress/v1/members/%s/votes.json" % idlist[0], headers=headers).json()['results'][0]['num_results']
num_bills = int(num_bills) + 1 # needs to be 1 bigger to fit the senator id

votes = [[0] * num_bills for i in range(len(idlist) + 1)]
index = 1
for i in idlist:
    url = "https://api.propublica.org/congress/v1/members/%s/votes.json" % (i)
    member_votes = requests.get(url, headers=headers).json()

    votes[index][0] = i

    for j in range(int(member_votes['results'][0]['num_results'])):
        votes[index][j + 1] = member_votes['results'][0]['votes'][j]['position']
    index += 1



# replace ids with names
for i in range(len(names)):
    votes[i+1][0] = names[i]
for i in range(len(bills)):
    votes[0][i] = bills[i]

data = pandas.DataFrame(votes)
data.to_csv('%d_%s.csv' % accessing, index=False)
