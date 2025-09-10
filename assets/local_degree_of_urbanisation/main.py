from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_LA_DEGURBA_DDOWN@DF_DEGURBA_DDOWN")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_local_degree_of_urbanisation")
        print(f"Uploaded {data.num_rows} rows to local_degree_of_urbanisation")
        
    save_state("local_degree_of_urbanisation", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
