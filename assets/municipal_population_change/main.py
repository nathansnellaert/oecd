from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DASHBOARD@MUNI_CHANGE")
    
    if data.num_rows > 0:
        upload_data(data, "municipal_population_change")
        print(f"Uploaded {data.num_rows} rows to municipal_population_change")
        
    save_state("municipal_population_change", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
