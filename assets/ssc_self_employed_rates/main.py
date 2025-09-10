from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAX_SSC@DF_SSC_SELF")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_ssc_self_employed_rates")
        print(f"Uploaded {data.num_rows} rows to ssc_self_employed_rates")
        
    save_state("ssc_self_employed_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
