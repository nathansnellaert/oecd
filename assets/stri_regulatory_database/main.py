from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_STRI_POLICY@DF_STRI_POLICY_MAIN")
    
    if data.num_rows > 0:
        upload_data(data, "stri_regulatory_database")
        print(f"Uploaded {data.num_rows} rows to stri_regulatory_database")
        
    save_state("stri_regulatory_database", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
