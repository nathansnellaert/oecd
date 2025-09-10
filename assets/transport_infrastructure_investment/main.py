from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_INFRINV@DF_INFRINV")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_transport_infrastructure_investment")
        print(f"Uploaded {data.num_rows} rows to transport_infrastructure_investment")
        
    save_state("transport_infrastructure_investment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
