from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EARNINGS@PAY_INCIDENCE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_low_high_pay_incidence")
        print(f"Uploaded {data.num_rows} rows to low_high_pay_incidence")
        
    save_state("low_high_pay_incidence", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
