from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TAXBEN_NCC@DF_NCC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_net_childcare_costs")
        print(f"Uploaded {data.num_rows} rows to net_childcare_costs")
        
    save_state("net_childcare_costs", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
