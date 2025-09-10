from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC20@DF_T625R_A")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_financial_flows_counterpart_annual")
        print(f"Uploaded {data.num_rows} rows to financial_flows_counterpart_annual")
        
    save_state("financial_flows_counterpart_annual", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
