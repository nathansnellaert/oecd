from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EXP_MORSC@DF_EXP_MORSC")
    
    if data.num_rows > 0:
        upload_data(data, "environmental_health_costs")
        print(f"Uploaded {data.num_rows} rows to environmental_health_costs")
        
    save_state("environmental_health_costs", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
