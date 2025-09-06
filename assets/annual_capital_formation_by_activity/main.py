from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10_IDC@DF_TABLE8A_IDC")
    
    if data.num_rows > 0:
        upload_data(data, "annual_capital_formation_by_activity")
        print(f"Uploaded {data.num_rows} rows to annual_capital_formation_by_activity")
        
    save_state("annual_capital_formation_by_activity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
