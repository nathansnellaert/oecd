from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_AFDD_STAT_ANNEX@DF_TAB30")
    
    if data.num_rows > 0:
        upload_data(data, "africa_environmental_premature_deaths")
        print(f"Uploaded {data.num_rows} rows to africa_environmental_premature_deaths")
        
    save_state("africa_environmental_premature_deaths", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
