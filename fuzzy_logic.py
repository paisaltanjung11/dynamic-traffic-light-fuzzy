import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Variabel Fuzzy
num_people = ctrl.Antecedent(np.arange(0, 101, 1), 'num_people') 
time_of_day = ctrl.Antecedent(np.arange(0, 24, 1), 'time_of_day')
duration = ctrl.Consequent(np.arange(5, 91, 1), 'duration')

# Fungsi Keanggotaan Fuzzy
num_people['few'] = fuzz.trimf(num_people.universe, [0, 0, 20])
num_people['medium'] = fuzz.trimf(num_people.universe, [15, 40, 70])
num_people['many'] = fuzz.trimf(num_people.universe, [50, 100, 100])

time_of_day['morning'] = fuzz.trimf(time_of_day.universe, [0, 6, 12]) # start(from 0 -> naik hingga puncak), puncak(=1), setelah waktu 12, mulai turun lg ke 0, after jam 12 siang bkn kategori morning
time_of_day['afternoon'] = fuzz.trimf(time_of_day.universe, [10, 14, 18])
time_of_day['evening'] = fuzz.trimf(time_of_day.universe, [16, 20, 24])

duration['short'] = fuzz.trimf(duration.universe, [5, 10, 20])
duration['medium'] = fuzz.trimf(duration.universe, [15, 30, 50])
duration['long'] = fuzz.trimf(duration.universe, [40, 70, 90])

rules = [
    ctrl.Rule(num_people['few'] & time_of_day['morning'], duration['short']),
    ctrl.Rule(num_people['few'] & time_of_day['afternoon'], duration['short']),
    ctrl.Rule(num_people['few'] & time_of_day['evening'], duration['medium']),

    ctrl.Rule(num_people['medium'] & time_of_day['morning'], duration['medium']),
    ctrl.Rule(num_people['medium'] & time_of_day['afternoon'], duration['medium']),
    ctrl.Rule(num_people['medium'] & time_of_day['evening'], duration['long']),

    ctrl.Rule(num_people['many'] & time_of_day['morning'], duration['medium']),
    ctrl.Rule(num_people['many'] & time_of_day['afternoon'], duration['long']),
    ctrl.Rule(num_people['many'] & time_of_day['evening'], duration['long']),
]

# Fuzzy Sistem
traffic_light_ctrl = ctrl.ControlSystem(rules)
traffic_light = ctrl.ControlSystemSimulation(traffic_light_ctrl)

def calculate_duration(num_people_input, time_of_day_input):
    traffic_light.input['num_people'] = num_people_input
    traffic_light.input['time_of_day'] = time_of_day_input

    traffic_light.compute()
    return traffic_light.output['duration']


