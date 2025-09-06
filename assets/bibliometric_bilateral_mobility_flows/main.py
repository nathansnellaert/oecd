from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_BIBLIO_F@DF_BIBLIO_F")
    
    if data.num_rows > 0:
        upload_data(data, "bibliometric_bilateral_mobility_flows")
        print(f"Uploaded {data.num_rows} rows to bibliometric_bilateral_mobility_flows")
        
    save_state("bibliometric_bilateral_mobility_flows", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
