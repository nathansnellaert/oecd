from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC10_IDC@DF_TABLE12_IDC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_annual_government_fiscal_aggregates")
        print(f"Uploaded {data.num_rows} rows to annual_government_fiscal_aggregates")
        
    save_state("annual_government_fiscal_aggregates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
