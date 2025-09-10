from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX@DF_TAB03")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_africa_population_growth_rate")
        print(f"Uploaded {data.num_rows} rows to africa_population_growth_rate")
        
    save_state("africa_population_growth_rate", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
