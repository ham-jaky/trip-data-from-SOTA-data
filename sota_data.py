import maidenhead
import datetime
from io import StringIO
import csv

# maidenhead.to_maiden(lat, lon)

test_summit_single = {
	"ref":"DM/HE-001",
	"name": "Wasserkuppe",
	"locator": "JO40xl",
	"altm": 950,
	"activations": 233,
	"points": 10
}

def load_csv(csv_file = "data/summitslist.csv"):
    format = "SOTA Summits List (Date=%d/%m/%Y)"
    with open(csv_file, encoding="utf-8") as f:
        note, table_content = f.read().split("\n", maxsplit=1)
    reader = csv.DictReader(StringIO(table_content))
    note_date = datetime.datetime.strptime(note, format)
    return list(reader), note_date


def csv_dict_to_sorted_dict(summit: dict):
    locator = maidenhead.to_maiden(float(summit["GridRef2"]), float(summit["GridRef1"]))
    return {
        "ref": summit["SummitCode"],
        "name": summit["SummitName"],
        "locator": locator,
        "altm": summit["AltM"],
        "activations": summit["ActivationCount"],
        "points": summit["Points"]
    }


def ref_starts_with(summits: list, x: str):
    x = x.lower()
    selected_summits = []
    for summit in summits:
        if summit["SummitCode"].lower().startswith(x):
            selected_summits.append(csv_dict_to_sorted_dict(summit=summit))
    return selected_summits
