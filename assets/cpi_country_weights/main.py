from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_CPI_COU_WEIGHTS@DF_CPI_CTRY_WEIGHTS")
    
    if data.num_rows > 0:
        upload_data(data, "cpi_country_weights")
        print(f"Uploaded {data.num_rows} rows to cpi_country_weights")
        
    save_state("cpi_country_weights", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
