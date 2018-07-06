import requests

TIDE_FORCAST_LOCATIONS = [
    {'name': 'Half Moon Bay, California',
     'url': 'https://www.tide-forecast.com/locations/Half-Moon-Bay-California/tides/latest'},
    {'name': 'Huntington Beach, California',
     'url': 'https://www.tide-forecast.com/locations/Huntington-Beach/tides/latest'},
    {'name': 'Providence, Rhode Island',
     'url': 'https://www.tide-forecast.com/locations/Providence-Rhode-Island/tides/latest'},
    {'name': 'Wrightsville Beach, North Carolina',
     'url': 'https://www.tide-forecast.com/locations/Wrightsville-Beach-North-Carolina/tides/latest'}]


def _get_tide_forecast_response(url):
    return requests.get(url, timeout=5)


def get_tide_forecasts_responses():
    """
    Gets html response with Requests, per each tide forecast url
    """
    return [_get_tide_forecast_response(h.get('url'))
            for h in TIDE_FORCAST_LOCATIONS]
