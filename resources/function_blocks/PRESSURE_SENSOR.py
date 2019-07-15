

class PRESSURE_SENSOR:

    def __init__(self):
        self.pressure = 0

    def schedule(self, event_name, event_value):
        if event_name == 'INIT':
            return [event_value, None, None, self.pressure, False]

        elif event_name == 'READ':
            # self.pressure += 1
            return [None, event_value, None, self.pressure, False]

        elif event_name == 'CALIBRATE':
            return [None, None, event_value, self.pressure, False]
