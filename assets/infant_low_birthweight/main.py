from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_STAT@DF_IH_LB")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_infant_low_birthweight")
        print(f"Uploaded {data.num_rows} rows to infant_low_birthweight")
        
    save_state("infant_low_birthweight", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
