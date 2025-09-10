from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REF_ASAP@DF_REFSERIES_ASAP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_revenue_reference_asia_pacific")
        print(f"Uploaded {data.num_rows} rows to revenue_reference_asia_pacific")
        
    save_state("revenue_reference_asia_pacific", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
