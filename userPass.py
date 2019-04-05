import json
import collections
import csv

def extractUserPass(filename):
    userPassDict = {}
    userDict = {}
    passDict = {}
    with open(filename) as f:
        line = f.readline()
        while line:
            try:
                obj = json.loads(line)
                if 'username' in obj.keys():
                    user = obj['username']
                    password = obj['password']
                    pair  = (user, password)
                    pair_key = json.dumps(pair)
                    # print(pair_key, pair)
                    if user in userDict:
                        userDict[user] += 1
                    else:
                        userDict[user] = 1
                    if password in passDict:
                        passDict[password] += 1
                    else:
                        passDict[password] = 1
                    if pair_key in userPassDict:
                        userPassDict[pair_key] += 1
                    else:
                        userPassDict[pair_key] = 1
            except KeyError:
                continue
            line = f.readline()
    userPassDict = sorter(userPassDict)
    userDict = sorter(userDict)
    passDict = sorter(passDict)

    with open('userPass.csv', mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(['username', 'password', 'count'])
        for k, v in userPassDict:
            pair = json.loads(k)
            writer.writerow([pair[0], pair[1], v])

    with open('pass.csv', mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(['password', 'count'])
        for k, v in passDict:
            writer.writerow([k, v])

    with open('user.csv', mode='w') as f:
        writer = csv.writer(f)
        writer.writerow(['username', 'count'])
        for k, v in passDict:
            writer.writerow([k, v])





def sorter(dict):
    return collections.OrderedDict(sorted(dict.items(), key= lambda t: t[1], reverse=True)).items()

    # print(sorted_dict)

# def output_helper(dict, )


if __name__ == "__main__":
    extractUserPass('cowrie.json')
