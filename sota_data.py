import maidenhead
import pandas as pd
from io import StringIO

# maidenhead.to_maiden(lat, lon)

test_summit_single = {
	"ref":"DM/HE-001",
	"name": "Wasserkuppe",
	"locator": "JO40xl",
	"altm": 950,
	"activations": 233,
	"points": 10
}

def load_csv():
    with open("data/summitslist.csv", encoding="utf-8") as f:
        note, table_content = f.read().split("\n", maxsplit=1)
    df = pd.read_csv(StringIO(table_content))
    print(df)
