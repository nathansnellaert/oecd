from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10@DF_TABLE14_EXP")
    
    if data.num_rows > 0:
        upload_data(data, "sector_expenditure_detailed")
        print(f"Uploaded {data.num_rows} rows to sector_expenditure_detailed")
        
    save_state("sector_expenditure_detailed", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
