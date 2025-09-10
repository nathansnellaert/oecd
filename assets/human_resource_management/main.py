from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_GOV@DF_GOV_HRM_2025")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_human_resource_management")
        print(f"Uploaded {data.num_rows} rows to human_resource_management")
        
    save_state("human_resource_management", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
