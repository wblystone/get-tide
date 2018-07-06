from lib import tide_forecast_client
from lib import tide_parser
from lib import tide_data_analyzer


def main():
    """
    GET-TIDE

    Wrapper main, invokes:
        1) tide_forecast_client: get all html responses per urls
        2) tide_parser: extract out tag data as needed,
            rotate into a list of dictionaries
        3) tide_data_analyzer: query against retrieved and parsed data
            as per challange specification
    """

    for tide_forecast_response in tide_forecast_client.get_tide_forecasts_responses():
        data_rows = tide_parser.get_data_rows(tide_forecast_response)
        tide_data_analyzer.get_tide_time_and_height_per_day(data_rows)
        print()


if __name__ == '__main__':
    main()
