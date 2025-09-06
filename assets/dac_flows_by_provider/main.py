from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DAC1@DF_DAC1")
    
    if data.num_rows > 0:
        upload_data(data, "dac_flows_by_provider")
        print(f"Uploaded {data.num_rows} rows to dac_flows_by_provider")
        
    save_state("dac_flows_by_provider", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
