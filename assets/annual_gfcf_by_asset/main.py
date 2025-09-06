from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NAMAIN10@DF_TABLE1_EXPENDITURE_GFCF_ASSET")
    
    if data.num_rows > 0:
        upload_data(data, "annual_gfcf_by_asset")
        print(f"Uploaded {data.num_rows} rows to annual_gfcf_by_asset")
        
    save_state("annual_gfcf_by_asset", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
