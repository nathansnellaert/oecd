from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SHA@DF_SHA_FS")
    
    if data.num_rows > 0:
        upload_data(data, "healthcare_financing_scheme_revenues")
        print(f"Uploaded {data.num_rows} rows to healthcare_financing_scheme_revenues")
        
    save_state("healthcare_financing_scheme_revenues", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
