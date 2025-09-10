from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_WILD_LIFE@DF_WILD_LIFE")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_threatened_species")
        print(f"Uploaded {data.num_rows} rows to threatened_species")
        
    save_state("threatened_species", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
