import requests
import datetime

COWIN_URL: str = 'https://cdn-api.co-vin.in/api'

headers = {
    "accept": "application/json",
    "Accept-Language": "hi_IN",
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/39.0.2171.95 Safari/537.36 "
}


def print_bold(string):
    print(datetime.datetime.now().strftime("%c") + " : \033[1m" + string + "\033[0m")


class CowinRequests:

    @staticmethod
    def get_states():
        endpoint = '/v2/admin/location/states'
        r = requests.get(url=COWIN_URL + endpoint, headers=headers)
        states_json = r.json()['states']
        for idx in range(0, len(states_json), 2):
            state1 = states_json[idx]
            state2 = states_json[idx + 1] if idx + 1 < len(states_json) else ""
            print('{:<35}{:<40}'.format(str(state1["state_id"])
                                        + ' : ' + state1["state_name"], (str(state2["state_id"])
                                                                         + ' : ' + state2[
                                                                             "state_name"]) if idx + 1 < len(
                states_json) else ""))

    @staticmethod
    def get_districts_by_state_id(state_id):
        endpoint = '/v2/admin/location/districts/' + state_id
        r = requests.get(url=COWIN_URL + endpoint, headers=headers)
        districts_json = r.json()['districts']
        for idx in range(0, len(districts_json), 2):
            state1 = districts_json[idx]
            state2 = districts_json[idx + 1] if idx + 1 < len(districts_json) else ""
            print('{:<35}{:<40}'.format(str(state1["district_id"])
                                        + ' : ' + state1["district_name"], (str(state2["district_id"])
                                                                            + ' : ' + state2[
                                                                                "district_name"]) if idx + 1 < len(
                districts_json) else ""))

    @staticmethod
    def get_slots_by_district_id(district_id):
        try:
            endpoint = '/v2/appointment/sessions/public/findByDistrict'
            nextDate = datetime.datetime.today() + datetime.timedelta(days=1)
            params = {
                'date': nextDate.strftime('%d-%m-%Y'),
                'district_id': district_id
            }
            r = requests.get(url=COWIN_URL + endpoint, headers=headers, params=params)
            availableSessions = r.json()['sessions']

            if len(availableSessions) == 0:
                print_bold("No slots available.")
            else:
                print("Available centers: {}".format(len(availableSessions)))
                for idx in range(len(availableSessions)):
                    sessionObj = availableSessions[idx]
                    print('{:<20}{:<20}{:<40}{:<40}'.format(sessionObj["center_id"],
                                                            sessionObj["pincode"],
                                                      sessionObj["name"],
                                                      sessionObj["address"]))
                    print('==> {:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format(sessionObj["from"],
                                                                             sessionObj["to"],
                                                                             str(sessionObj["min_age_limit"]),
                                                                             str(sessionObj["available_capacity"]),
                                                                             sessionObj["vaccine"],
                                                                             sessionObj["fee_type"]))
            return availableSessions
        except Exception as ex:
            print("{} is not a valid district id.".format(district_id))

    @staticmethod
    def get_slots_by_pincode(pincode):
        try:
            nextDate = datetime.datetime.today() + datetime.timedelta(days=1)
            formattedDate = nextDate.strftime('%d-%m-%Y')
            getSlotsByPincodeEndpoint = COWIN_URL + '/v2/appointment/sessions/public/findByPin?pincode={}&date={}'.format(
                pincode, formattedDate)
            r = requests.get(url=getSlotsByPincodeEndpoint, headers=headers)
            availableSessions = r.json()['sessions']

            if len(availableSessions) == 0:
                print_bold('No slots available')
            else:
                for idx in range(len(availableSessions)):
                    sessionObj = availableSessions[idx]
                    print('{:<20}{:<40}{:<40}'.format(sessionObj["center_id"],
                                                      sessionObj["name"],
                                                      sessionObj["address"]))
                    print('===> {:<20}{:<20}{:<20}{:<20}{:<20}{:<20}'.format(sessionObj["from"],
                                                                             sessionObj["to"],
                                                                             str(sessionObj["min_age_limit"]),
                                                                             str(sessionObj["available_capacity"]),
                                                                             sessionObj["vaccine"],
                                                                             sessionObj["fee_type"]))
            return availableSessions
        except Exception as ex:
            print_bold("{} is not a valid pincode".format(pincode))