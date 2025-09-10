from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_DEMO_POP_AGE_DDOWN@DF_POP_AGE_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_local_population_age_sex")
        print(f"Uploaded {data.num_rows} rows to local_population_age_sex")
        
    save_state("local_population_age_sex", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
