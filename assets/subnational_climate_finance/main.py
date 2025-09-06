from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SNGF_CSF@DF_SGCF")
    
    if data.num_rows > 0:
        upload_data(data, "subnational_climate_finance")
        print(f"Uploaded {data.num_rows} rows to subnational_climate_finance")
        
    save_state("subnational_climate_finance", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
