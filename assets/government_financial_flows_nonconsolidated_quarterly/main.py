from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASEC20@DF_T620GOV_Q")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_government_financial_flows_nonconsolidated_quarterly")
        print(f"Uploaded {data.num_rows} rows to government_financial_flows_nonconsolidated_quarterly")
        
    save_state("government_financial_flows_nonconsolidated_quarterly", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
