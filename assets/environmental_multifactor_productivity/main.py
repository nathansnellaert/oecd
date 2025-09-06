from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAMFP@DF_EAMFP")
    
    if data.num_rows > 0:
        upload_data(data, "environmental_multifactor_productivity")
        print(f"Uploaded {data.num_rows} rows to environmental_multifactor_productivity")
        
    save_state("environmental_multifactor_productivity", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
