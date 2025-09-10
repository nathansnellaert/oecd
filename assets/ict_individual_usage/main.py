from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ICT_HH_IND@DF_IND")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_ict_individual_usage")
        print(f"Uploaded {data.num_rows} rows to ict_individual_usage")
        
    save_state("ict_individual_usage", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
