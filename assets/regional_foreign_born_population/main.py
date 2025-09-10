from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_MIGRANT@DF_MIGR_STOCK")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_regional_foreign_born_population")
        print(f"Uploaded {data.num_rows} rows to regional_foreign_born_population")
        
    save_state("regional_foreign_born_population", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
