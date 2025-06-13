"""Utility to generate sermon csv by ingesting raw text data from sermon browser
wordpress database
"""

from csv import QUOTE_MINIMAL, writer
import re
from phpserialize import loads


def gen_html_audio_element_str(data_item):
    result = ""
    org_str = data_item["audio"]
    if org_str and org_str != "NULL":
        result = (
            "<audio controls>"
            f'<source src="https://pccoakland.org/oif/wp-content/uploads/sermons/{org_str}" '
            'type="audio/mpeg">Your browser does not support the audio element.'
            "</audio>"
        )
    print(result)
    return result


def format_scripture_data(data_item):
    result = []
    start_data = loads(
        bytes(data_item["start"], encoding="utf-8"),
        decode_strings=True,
        array_hook=dict,
    )
    end_data = loads(
        bytes(data_item["end"], encoding="utf-8"), decode_strings=True, array_hook=dict
    )

    if start_data and end_data:
        start_data_items = start_data.items()
        end_data_items = end_data.items()
        if len(start_data_items) != len(end_data_items):
            raise ValueError("Mismatch between number of start and end items")
        for idx, scripture_data in start_data_items:
            result.append(
                f"{scripture_data['book']} {scripture_data['chapter']}:{scripture_data['verse']}-{end_data[idx]['verse']}"
            )

    if result:
        return ",".join(result)


def normalize(val):
    """Remove backslashes from strings"""
    result = re.sub(r"\\", "", str(val))
    return result if result else val


def read_raw_sermon_data(file):
    result = []
    with open(file, mode="r", errors="ignore") as f:
        lines = f.read().splitlines()
        data = [line.split("\t") for line in lines]
        header = data[0]
        rows = data[1:]
        for row in rows:
            result_item = {}
            for idx, header_item in enumerate(header):
                result_item[header_item] = normalize(row[idx])
            result.append(result_item)
    return result


def generate_csv(out_csv, data):
    with open(out_csv, mode="w", encoding="utf8") as csv_file:
        csv_writer = writer(csv_file, quoting=QUOTE_MINIMAL, escapechar="\\")
        # Write header
        csv_writer.writerow(
            ["Date", "Speaker", "Title", "Scripture", "Series", "Audio"]
        )
        for data_item in data:
            scripture_data = format_scripture_data(data_item)
            audio_html_element = gen_html_audio_element_str(data_item)
            csv_writer.writerow(
                [
                    data_item["datetime"],
                    data_item["preacher"],
                    data_item["title"],
                    scripture_data,
                    data_item["series"],
                    audio_html_element,
                ]
            )
            print(audio_html_element)
        # Write data loop
        # csv_writer.writerow(['2025-04-20', 'Pastor Jesse McLaughlin', 'Worship the Risen Jesus', 'Matthew 28:1–15', '<audio controls><source src=\"https://pccoakland.org/oif/wp-content/uploads/sermons/2025-04-20 - OIF Sermon - Jesse McLaughlin.mp3\" type=\"audio/mpeg\">Your browser does not support the audio element.</audio>' ])


def main():
    data = read_raw_sermon_data("./sermon-data.txt")
    generate_csv("output.csv", data)


if __name__ == "__main__":
    main()
    # print(loads(data=b'a:1:{i:0;a:3:{s:4:"book";s:7:"1 Peter";s:7:"chapter";i:4;s:5:"verse";i:1;}}', decode_strings=True))
