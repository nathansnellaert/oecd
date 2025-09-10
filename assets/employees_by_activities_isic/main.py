from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ALFS@DF_ALFS_EMP_EES")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_employees_by_activities_isic")
        print(f"Uploaded {data.num_rows} rows to employees_by_activities_isic")
        
    save_state("employees_by_activities_isic", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
