from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIVA_EXGRVA@DF_EXGRVA")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_tiva_value_added_exports")
        print(f"Uploaded {data.num_rows} rows to tiva_value_added_exports")
        
    save_state("tiva_value_added_exports", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
