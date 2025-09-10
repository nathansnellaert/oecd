from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REF_GLOBAL@DF_REFSERIES_GLOBAL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_revenue_reference_global")
        print(f"Uploaded {data.num_rows} rows to revenue_reference_global")
        
    save_state("revenue_reference_global", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
