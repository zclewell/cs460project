import json
from geolite2 import geolite2
import collections
import csv

def extractIp(filename):
    countryDict = {}
    reader = geolite2.reader()
    csvF = open('loc.csv', mode='w')
    writer = csv.writer(csvF)
    writer.writerow(['country', 'lat','long'])
    with open(filename) as f:
        line = f.readline()
        while line:
            try:
                obj = json.loads(line)
                ip = obj['src_ip']
                match = reader.get(ip)
                if match is not None:
                    # print(match)
                    name = match['country']['names']['en']
                    if name in countryDict:
                        countryDict[name] += 1
                    else: 
                        countryDict[name] = 1
                    
                    lat = match['location']['latitude']
                    long = match['location']['longitude']
                    writer.writerow([name, lat, long])
            except:
                pass
            finally:
                line = f.readline()
    countryDict = sorter(countryDict)

    with open('country.csv', mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(['country', 'count'])
        for k, v in countryDict:
            writer.writerow([k, v])

def sorter(dict):
    return collections.OrderedDict(sorted(dict.items(), key=lambda t: t[1], reverse=True)).items()

if __name__ == "__main__":
    extractIp('./json/meta.login.json')
