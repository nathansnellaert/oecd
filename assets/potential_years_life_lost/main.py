from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_HEALTH_STAT@DF_PYLL")
    
    if data.num_rows > 0:
        upload_data(data, "potential_years_life_lost")
        print(f"Uploaded {data.num_rows} rows to potential_years_life_lost")
        
    save_state("potential_years_life_lost", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
