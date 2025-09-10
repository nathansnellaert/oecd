from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX@DF_TAB20")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_afdd_external_financial_inflows")
        print(f"Uploaded {data.num_rows} rows to afdd_external_financial_inflows")
        
    save_state("afdd_external_financial_inflows", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
