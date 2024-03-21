def temp(outside):
    if outside > 60:
        print('it is warm outside')
    elif outside > 80:
        print('it is hot outside.')
    elif outside < 50:
        print('it is cold outside.')
    elif outside > 50:
        print('its not warm but its also not too cold.')

temp(80)