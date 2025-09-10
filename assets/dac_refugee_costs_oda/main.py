from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_QDD_DCD_IDRC@DF_QDD_DCD_IDRC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_dac_refugee_costs_oda")
        print(f"Uploaded {data.num_rows} rows to dac_refugee_costs_oda")
        
    save_state("dac_refugee_costs_oda", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
