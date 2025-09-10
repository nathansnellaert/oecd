from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PDB@DF_PDB_LV")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_productivity_levels")
        print(f"Uploaded {data.num_rows} rows to productivity_levels")
        
    save_state("productivity_levels", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
