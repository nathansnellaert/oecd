from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10_IDC@DF_TABLE10_IDC")
    
    if data.num_rows > 0:
        upload_data(data, "annual_tax_social_contributions")
        print(f"Uploaded {data.num_rows} rows to annual_tax_social_contributions")
        
    save_state("annual_tax_social_contributions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
