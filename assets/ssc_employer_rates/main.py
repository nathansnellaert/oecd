from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAX_SSC@DF_SSC_EMPLOYER")
    
    if data.num_rows > 0:
        upload_data(data, "ssc_employer_rates")
        print(f"Uploaded {data.num_rows} rows to ssc_employer_rates")
        
    save_state("ssc_employer_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
