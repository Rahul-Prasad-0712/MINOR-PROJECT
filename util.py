import json
import pickle
import numpy as np

__state = ["year", "type", "gender", "age_group", "choose a state", "a & n islands", "andhra pradesh",
           "arunachal pradesh", "assam", "bihar", "chandigarh", "chhattisgarh", "d & n haveli", "daman & diu",
           "delhi (ut)", "goa", "gujarat", "haryana", "himachal pradesh", "jammu & kashmir", "jharkhand", "karnataka",
           "kerala", "lakshadweep", "madhya pradesh", "maharashtra", "manipur", "meghalaya", "mizoram", "nagaland",
           "odisha", "puducherry", "punjab", "rajasthan", "sikkim", "tamil nadu", "total (all india)", "total (states)",
           "total (uts)", "tripura", "uttar pradesh", "uttarakhand", "west bengal"][4:]
__data_columns = None
__model = None


def get_estimated_suicide(State, Year, Type, Gender, Age_group):
    try:
        state_index = __data_columns.index(State.lower())
    except:
        state_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = Year
    x[1] = Type
    x[2] = Gender
    x[3] = Age_group
    if state_index >= 0:
        x[state_index] = 1
    return round(__model.predict([x])[0], 2)


def get_state_names():
    return __state


def load_saved_artifacts():
    print('loading saved artifacts... start')
    global __data_columns
    global __state

    with open("./Artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __state = __data_columns[4:]
    global __model
    with open('./Artifacts/Suicide_model.pickle', 'rb') as f:
        __model = pickle.load(f)

    print('loading saved artifacts ... done')


if __name__ == '__main__':
    load_saved_artifacts()
    print(get_state_names())
    print(get_estimated_suicide('chhattisgarh', 2016, 5, 0, 2))
    print(get_estimated_suicide('andhra Pradesh', 2019, 37, 1, 2))
    print(get_estimated_suicide('maharashtra', 2017, 10, 0, 3))
    print(get_estimated_suicide('kerala', 2023, 40, 1, 4))
