from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EARNINGS@AV_AN_WAGE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_average_annual_wages")
        print(f"Uploaded {data.num_rows} rows to average_annual_wages")
        
    save_state("average_annual_wages", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
