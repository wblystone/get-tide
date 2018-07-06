from bs4 import BeautifulSoup

BS_HTML_PARSER = 'html.parser'

TAG_TABLE = 'table'
CLASS_TABLE = 'tide-table'

TAG_TABLE_HEADER = 'th'
TAG_TABLE_DATACELL = 'td'
TAG_TABLE_ROW = 'tr'

CLASS_TIME = 'time'
CLASS_DATE = 'date'
CLASS_HORIZON = 'horizon'

# following normalized out
CLASS_TIMETIDE = 'timetide'
# signifies end of table on latest page view
CLASS_DATELAST = 'datelast'


def _get_tide_table(tide_forecast_response):
    tide_forecast_content = BeautifulSoup(tide_forecast_response.content, BS_HTML_PARSER)

    return tide_forecast_content.find(TAG_TABLE, {'class': CLASS_TABLE})


def _process_data_cell(data_cell):
    _class = data_cell.get('class')
    if _class is None:
        _class = [CLASS_HORIZON]
    _class = ''.join(_class)

    # normalizes some extra class names
    if _class == CLASS_TIMETIDE:
        _class = CLASS_TIME
    elif _class == CLASS_DATELAST:
        _class = CLASS_DATE

    key = _class
    value = data_cell.string

    return key, value


def get_data_rows(tide_forecast_response):
    """
    Parses out html response with BeautifulSoup into list of hashes,
        key values pairs per column type and cell value
    """

    tide_table = _get_tide_table(tide_forecast_response)

    data_rows = \
        [time_row.find_all([TAG_TABLE_HEADER, TAG_TABLE_DATACELL])
         for time_row in tide_table.find_all(TAG_TABLE_ROW)]

    processed_data_rows = []
    for data_row in data_rows:
        data_row_h = {}
        for data_cell in data_row:
            key, value = _process_data_cell(data_cell)
            data_row_h[key] = value

        processed_data_rows.append(data_row_h)

    return processed_data_rows
