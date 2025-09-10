from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ALFS@DF_ALFS_EMP_ISIC")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_employment_by_activities_isic_rev4")
        print(f"Uploaded {data.num_rows} rows to employment_by_activities_isic_rev4")
        
    save_state("employment_by_activities_isic_rev4", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
