from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NASU@DF_INDICATOR_D21X31_P3S14")
    
    if data.num_rows > 0:
        upload_data(data, "sut_taxes_subsidies_household_consumption")
        print(f"Uploaded {data.num_rows} rows to sut_taxes_subsidies_household_consumption")
        
    save_state("sut_taxes_subsidies_household_consumption", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
