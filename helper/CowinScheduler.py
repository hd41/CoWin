from .CowinRequests import *
from playsound import playsound
import config
import time


class CowinScheduler:

    @staticmethod
    def schedule():
        CowinRequests.get_states()
        state_input = '0'
        while True:
            state_input = input("Enter state: ")
            if int(state_input) > 37 or int(state_input) < 1:
                print("{} is not a valid state id. Try again ...".format(state_input))
                continue
            else:
                break

        if state_input != '0':
            CowinRequests.get_districts_by_state_id(state_input)
            districtId = input("Enter district you want to find slots in: ")
            while True:
                available_slots = CowinRequests.get_slots_by_district_id(districtId)
                if(len(available_slots) != 0):
                    playsound(config.ALARM_SOUND)
                time.sleep(config.RUN_EVERY)