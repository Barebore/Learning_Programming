class Track:
    def __init__(self, start_x, start_y):
        self.start_x = start_x
        self.start_y = start_y

class TrackLine:
    def __init__(self, to_x, to_y, max_speed):
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed
        