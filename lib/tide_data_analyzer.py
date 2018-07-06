# columns
COLUMN_TIME = 'time'
COLUMN_TIMEZONE = 'time-zone'
COLUMN_TIDE = 'tide'
COLUMN_LEVELMETRIC = 'levelmetric'
COLUMN_HORIZON = 'horizon'

# matching vars
HORIZON_SUNRISE = 'Sunrise'
HORIZON_SUNSET = 'Sunset'
TIDETYPE_LOWTIDE = 'Low Tide'


def get_tide_time_and_height_per_day(data_rows):
    """
    Get all row for:
        1) lowtide
        2) during daylight (after sunrise, before sunset)
    """

    daylight_flag = False

    for data_row in data_rows:
        time = data_row.get(COLUMN_TIME)
        timezone = data_row.get(COLUMN_TIMEZONE)
        tidetype = data_row.get(COLUMN_TIDE)
        height = data_row.get(COLUMN_LEVELMETRIC)
        horizon = data_row.get(COLUMN_HORIZON)

        if horizon == HORIZON_SUNRISE:
            daylight_flag = True
        elif horizon == HORIZON_SUNSET:
            daylight_flag = False

        if tidetype == TIDETYPE_LOWTIDE and daylight_flag:
            print(time, timezone, height)
