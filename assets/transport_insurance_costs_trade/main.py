from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ITIC@DF_ITIC")
    
    if data.num_rows > 0:
        upload_data(data, "transport_insurance_costs_trade")
        print(f"Uploaded {data.num_rows} rows to transport_insurance_costs_trade")
        
    save_state("transport_insurance_costs_trade", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
