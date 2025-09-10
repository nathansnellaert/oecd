from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_ILR@DF_QDD_ILR")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_interest_limitation_rules")
        print(f"Uploaded {data.num_rows} rows to interest_limitation_rules")
        
    save_state("interest_limitation_rules", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
