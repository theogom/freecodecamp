DAYS = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']


def add_time(start: str, duration: str, day: str = None) -> str:
    """
    Add a duration to a 12-hour clock format time
    """
    start_splitted = start.replace(' ', ':').split(':')
    hours, minutes = map(int, start_splitted[:2])
    period = start_splitted[2]

    duration_splitted = duration.split(':')

    # Add times
    new_hours = hours + int(duration_splitted[0])
    new_minutes = minutes + int(duration_splitted[1])

    # Minutes overflow
    if new_minutes // 60 > 0:
        new_minutes -= 60
        new_hours += 1

    # Hours overflow
    midday = 0
    while new_hours // 12 > 0:
        new_hours -= 12
        midday += 1

    new_hours = 12 if new_hours == 0 else new_hours

    if midday % 2 == 1:
        new_period = 'AM' if period == 'PM' else 'PM'
    else:
        new_period = period

    new_time = f'{new_hours}:{new_minutes:0>2} {new_period}'

    day_passed = (midday + (1 if period == 'PM' else 0)) // 2

    if day is not None:
        day = day.capitalize()
        day = DAYS[(DAYS.index(day) + day_passed) % 7]
        new_time = ', '.join((new_time, day))

    if day_passed > 0:
        info = '(next day)' if day_passed == 1 else f'({day_passed} days later)'
        new_time = ' '.join((new_time, info))

    return new_time
