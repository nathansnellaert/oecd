from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DAC2@DF_DAC4")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_dac4_private_investment")
        print(f"Uploaded {data.num_rows} rows to dac4_private_investment")
        
    save_state("dac4_private_investment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
