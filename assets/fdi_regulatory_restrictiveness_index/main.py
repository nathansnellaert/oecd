from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_FDIRRI_SCORES@DF_FDIRRI_SCORES")
    
    if data.num_rows > 0:
        upload_data(data, "fdi_regulatory_restrictiveness_index")
        print(f"Uploaded {data.num_rows} rows to fdi_regulatory_restrictiveness_index")
        
    save_state("fdi_regulatory_restrictiveness_index", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
