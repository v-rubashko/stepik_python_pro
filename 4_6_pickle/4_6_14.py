import pickle


def filter_dump(filename, objects, typename):
    data = [item for item in objects if type(item) == typename]
    with open(filename, "wb") as file:
        pickle.dump(data, file)

