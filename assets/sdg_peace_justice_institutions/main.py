from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_SDG@DF_SDG_G_16")
    
    if data.num_rows > 0:
        upload_data(data, "sdg_peace_justice_institutions")
        print(f"Uploaded {data.num_rows} rows to sdg_peace_justice_institutions")
        
    save_state("sdg_peace_justice_institutions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
