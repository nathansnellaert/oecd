from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DF_AEI2023_DASHBOARD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_agri_environmental_dashboard_2023")
        print(f"Uploaded {data.num_rows} rows to agri_environmental_dashboard_2023")
        
    save_state("agri_environmental_dashboard_2023", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
