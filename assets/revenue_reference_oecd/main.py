from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REF_OECD@DF_REFSERIES_OECD")
    
    if data.num_rows > 0:
        upload_data(data, "revenue_reference_oecd")
        print(f"Uploaded {data.num_rows} rows to revenue_reference_oecd")
        
    save_state("revenue_reference_oecd", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
