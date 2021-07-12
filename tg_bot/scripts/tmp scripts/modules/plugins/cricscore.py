import requests
import time

get_all_matches = "https://cricapi.com/api/matches/"
get_score = "https://cricapi.com/api/cricketScore/"

api_key = "MNifkE3V6RMNbrX9NElliyx3bSV2"
unique_id = list()

match = None


def get_init(func="ipl_match_update"):
    global get_all_matches
    global get_score
    global api_key
    global unique_id
    global match

    text = res_dict = None

    uri_params_1 = {"apikey": api_key}
    resp = requests.get(get_all_matches, params=uri_params_1)
    res_dict = resp.json()
    match = res_dict['matches']

    if func == "ipl_tday_update":
        text = ipl_tday_update()
    elif func == "ipl_match_update":
        text = ipl_match_update()

    return text

    """
        print("ID :",i['unique_id'])
        print("DATE :",i['date'])
        print("TEAMS :",i['team-1'],"vs",i['team-2'])
        print("TYPE :", i['type'])
        print("STARTED :",i['matchStarted'])
        print()

        #matchStarted
        #Twenty20
        #2020-10-22T00:00:00.000Z
    """


def ipl_tday_update():
    global match
    global unique_id

    tday = (time.strftime("%Y-%m-%d", time.gmtime()))
    nti = (time.strftime("%H:%M:%S", time.gmtime()))
    text = ""

    for i in match:

        if i['type'] == 'Twenty20' and i['date'][:10] == tday:
            unique_id.append(i['unique_id'])

            ti = i['dateTimeGMT']
            ti = ti[ti.find("T")+len("T"):ti.rfind("Z")][:8]

            cmin = nti[3:]
            cmin = cmin[:2]
            chrs = nti[:2]
            ctime = int(chrs)*60 + int(cmin)

            gmin = ti[3:]
            gmin = gmin[:2]
            ghrs = ti[:2]
            gtime = int(ghrs)*60 + int(gmin)

            countd = "(Match Started)"
            winnert = toss = ""

            if ctime >= gtime:
                remtimehrs = 0
                remtimemin = 0
                try:
                    toss = "Toss : " + "<b>" + i['toss_winner_team'] + "</b>\n"
                except:
                    pass
                try:
                    winnert = "Winner : " + "<b>" + i['winner_team'] + "</b>\n"
                except:
                    pass
            else:

                remtimemin = (gtime - ctime) % 60
                remtimehrs = (int(ghrs) - int(chrs))-1

                if remtimehrs <= 0:
                    remtimehrs = 0

                remtimehrs = remtimehrs
                countd = "(" + str(remtimehrs) + "hr " + \
                    str(remtimemin) + "min remaining)"

            #mlef = int() - int()

            text = (text +
                    "Match : " + "<a href='https://www.google.com/search?q=ipl&oq=ipl&aqs=chrome.0.69i59l3j69i57j69i65j69i60l2j69i61.465j0j4&sourceid=chrome&ie=UTF-8'>" + i['team-1'] + " vs " + i['team-2'] + "</a>\n" +
                    "Type  : " + i['type'] + "\n" +
                    "Date  : " + "<b>" + i['date'][:10] + "</b>\n" +
                    "Time : " + "<b>" + ti + " GMT " + countd + "</b>\n" +
                    toss +
                    winnert + "\n")

            return text


def ipl_match_update():
    global match
    global unique_id
    global api_key
    global get_all_matches

    tday = (time.strftime("%Y-%m-%d (%H:%M:%S GMT)", time.gmtime()))
    text = ""
    for i in match:
        if i['type'] == 'Twenty20' and i['date'][:10] == tday[:10]:
            unique_id.append(i['unique_id'])

    for i in unique_id:
        uri_params = {'apikey': api_key, 'unique_id': i}
        resp = requests.get(get_score, params=uri_params)
        update = resp.json()

        stat = update['stat']
        try:
            score = update['score']
        except:
            pass
        try:
            desc = update['description']
        except:
            pass

        if desc == score:
            desc = ""
        else:
            desc = "Description : " + desc + "\n"

        date = tday

        text = (text +
                "Match : " + "<a href='https://www.google.com/search?q=ipl&oq=ipl&aqs=chrome.0.69i59l3j69i57j69i65j69i60l2j69i61.465j0j4&sourceid=chrome&ie=UTF-8'>" + update['team-1'] + " vs " + update['team-2'] + "</a>\n\n" +
                "Status : " + "<b>" + stat + "</b>\n\n" +
                "Score  : " + "<b>" + score + "</b>\n" +
                desc + "\n" +
                "Type   : " + "Twenty20" + "\n"
                "Refreshed   : " + "<i>" + date + "</i>\n" +
                "\n<i>> /iplupdate</i>")

        return text


if __name__ == '__main__':
    get_init()
