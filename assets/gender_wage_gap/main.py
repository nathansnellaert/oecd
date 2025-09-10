from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EARNINGS@GENDER_WAGE_GAP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_gender_wage_gap")
        print(f"Uploaded {data.num_rows} rows to gender_wage_gap")
        
    save_state("gender_wage_gap", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
