from .level import Level

class Aqi:
    """ Encapsulates info about the Air Quality Index system """

    GOOD_DESCRIPTION      = """ Air quality is considered satisfactory,
                                and air pollution poses little or no risk. """
    MODERATE_DESCRIPTION  = """ Air quality is acceptable; however, for some pollutants
                                there may be a moderate health concern for a very small number
                                of people who are unusually sensitive to air pollution. """
    USG_DESCRIPTION       = """ Although general public is not likely to be affected at this AQI
                                range, people with lung disease, older adults and children are at
                                a greater risk from exposure to ozone, whereas persons with heart
                                and lung disease, older adults and children are at greater risk
                                from the presence of particles in the air. """
    UNHEALTHY_DESCRIPTION = """ Everyone may begin to experience health effects; members
                                of sensitive groups may experience more serious health
                                effects. """
    VERY_UNHEALTHY_DESCRIPTION = """ Health alert: everyone may experience more serious
                                     health effects. """
    HAZARDOUS_DESCRIPTION = """ Health warnings of emergency conditions. The entire population
                                is more likely to be affected. """

    def __init__(self):
        self._levels = [
            Level(1, 'Good', self.GOOD_DESCRIPTION, 0x00CC00, 0, 50),
            Level(2, 'Moderate', self.MODERATE_DESCRIPTION, 0xFFFF00, 51, 100),
            Level(3, 'USG', self.USG_DESCRIPTION, 0xFF6699, 101, 150),
            Level(4, 'Unhealthy', self.UNHEALTHY_DESCRIPTION, 0xFF0000, 151, 200),
            Level(5, 'Very Unhealthy', self.VERY_UNHEALTHY_DESCRIPTION, 0x99004C, 201, 300),
            Level(6, 'Hazardous', self.HAZARDOUS_DESCRIPTION, 0x7E0023, 301, 500)
        ]

    def level_at(self, index):
        return self._levels[index-1]

    def level_for_value(self, value):
        for level in self._levels:
            if level.min_aqi <= value and level.max_aqi >= value:
                return level
        raise ValueError('Unknown AQI: {0}'.format(value))

    @property
    def levels(self):
        return self._levels
