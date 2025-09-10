from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DAC2@DF_DAC2A")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_oda_disbursements_by_country")
        print(f"Uploaded {data.num_rows} rows to oda_disbursements_by_country")
        
    save_state("oda_disbursements_by_country", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
