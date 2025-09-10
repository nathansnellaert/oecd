from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TOURISM_ENT_EMP@DF_ENT_EMP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_tourism_enterprises_employment")
        print(f"Uploaded {data.num_rows} rows to tourism_enterprises_employment")
        
    save_state("tourism_enterprises_employment", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
