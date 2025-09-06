from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DF_AEI2024_DASHBOARD")
    
    if data.num_rows > 0:
        upload_data(data, "agri_environmental_2024_dashboard")
        print(f"Uploaded {data.num_rows} rows to agri_environmental_2024_dashboard")
        
    save_state("agri_environmental_2024_dashboard", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
