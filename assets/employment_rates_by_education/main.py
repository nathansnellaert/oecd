from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EAG_LSO_EA@DF_LSO_NEAC_EMP")
    
    if data.num_rows > 0:
        upload_data(data, "employment_rates_by_education")
        print(f"Uploaded {data.num_rows} rows to employment_rates_by_education")
        
    save_state("employment_rates_by_education", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
