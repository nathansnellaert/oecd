from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX@DF_TAB18")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_afdd_export_diversification")
        print(f"Uploaded {data.num_rows} rows to afdd_export_diversification")
        
    save_state("afdd_export_diversification", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
