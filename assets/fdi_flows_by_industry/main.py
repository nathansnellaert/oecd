from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FDI@DF_FDI_FLOW_IND")
    
    if data.num_rows > 0:
        upload_data(data, "fdi_flows_by_industry")
        print(f"Uploaded {data.num_rows} rows to fdi_flows_by_industry")
        
    save_state("fdi_flows_by_industry", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
