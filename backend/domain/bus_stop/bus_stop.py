class BusStop:

    stop_id = ''
    stop_name = ''
    stop_lat = 0.0
    stop_lon = 0.0

    def __init__(self, stop_id, stop_name, stop_lat, stop_lon):
        self.stop_id = stop_id
        self.stop_name = stop_name
        self.stop_lat = stop_lat
        self.stop_lon = stop_lon