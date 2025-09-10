from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_NEAC_EMP_FIELD")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_tertiary_employment_by_field")
        print(f"Uploaded {data.num_rows} rows to tertiary_employment_by_field")
        
    save_state("tertiary_employment_by_field", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
