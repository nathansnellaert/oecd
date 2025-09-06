from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAX_PIT@DF_PIT_SUB_PROG")
    
    if data.num_rows > 0:
        upload_data(data, "pit_subcentral_progressive_rates")
        print(f"Uploaded {data.num_rows} rows to pit_subcentral_progressive_rates")
        
    save_state("pit_subcentral_progressive_rates", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
