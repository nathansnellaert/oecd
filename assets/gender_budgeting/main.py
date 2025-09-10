from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_GOV_GENBUD@DF_GOV_GENBUD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_gender_budgeting")
        print(f"Uploaded {data.num_rows} rows to gender_budgeting")
        
    save_state("gender_budgeting", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
