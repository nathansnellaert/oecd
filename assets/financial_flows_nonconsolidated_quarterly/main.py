from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC20@DF_T620R_Q")
    
    if data.num_rows > 0:
        upload_data(data, "financial_flows_nonconsolidated_quarterly")
        print(f"Uploaded {data.num_rows} rows to financial_flows_nonconsolidated_quarterly")
        
    save_state("financial_flows_nonconsolidated_quarterly", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
