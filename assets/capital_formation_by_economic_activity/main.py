from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE8")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_capital_formation_by_economic_activity")
        print(f"Uploaded {data.num_rows} rows to capital_formation_by_economic_activity")
        
    save_state("capital_formation_by_economic_activity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
