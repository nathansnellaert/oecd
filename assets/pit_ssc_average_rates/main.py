from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAX_PIT@DF_PIT_AV")
    
    if data.num_rows > 0:
        upload_data(data, "pit_ssc_average_rates")
        print(f"Uploaded {data.num_rows} rows to pit_ssc_average_rates")
        
    save_state("pit_ssc_average_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
