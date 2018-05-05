cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps():
    """return a comma separated string of jeep models (original order)"""
    jeeps = ""
    for i in cars["Jeep"]:
        jeeps = jeeps + i + ", "
    return jeeps.rstrip(", ")


def get_first_model_each_manufacturer():
    """return a list of matching models (original ordering)"""
    first_model = [cars[i][0] for i in cars]
    return first_model


def get_all_matching_models(grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    trail_list = []
    for i in cars:
        for j in cars[i]:
            if grep.lower() in j.lower():
                trail_list.append(j)
    return sorted(trail_list)


def sort_car_models():
    """sort the car models (values) and return the resulting cars dict"""
    for i in cars:
        cars[i] = sorted(cars[i])
    return cars
