from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HW@DF_AVG_ANN_HRS_WKD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_annual_hours_worked")
        print(f"Uploaded {data.num_rows} rows to annual_hours_worked")
        
    save_state("annual_hours_worked", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
