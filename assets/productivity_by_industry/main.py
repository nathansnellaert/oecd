from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PDB@DF_PDB_ISIC4_I4")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_productivity_by_industry")
        print(f"Uploaded {data.num_rows} rows to productivity_by_industry")
        
    save_state("productivity_by_industry", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
