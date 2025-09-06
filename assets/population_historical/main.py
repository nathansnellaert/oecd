from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_POPULATION@DF_POP_HIST")
    
    if data.num_rows > 0:
        upload_data(data, "population_historical")
        print(f"Uploaded {data.num_rows} rows to population_historical")
        
    save_state("population_historical", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
