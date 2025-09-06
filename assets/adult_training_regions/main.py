from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_REG_EDU@DF_TRAINING")
    
    if data.num_rows > 0:
        upload_data(data, "adult_training_regions")
        print(f"Uploaded {data.num_rows} rows to adult_training_regions")
        
    save_state("adult_training_regions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
