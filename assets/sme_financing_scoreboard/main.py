from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SMEE_FINANCING@DF_SMEE_SCOREBOARD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_sme_financing_scoreboard")
        print(f"Uploaded {data.num_rows} rows to sme_financing_scoreboard")
        
    save_state("sme_financing_scoreboard", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
