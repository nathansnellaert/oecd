from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIE@DF_TIE_POL")
    
    if data.num_rows > 0:
        upload_data(data, "entrepreneurship_poland")
        print(f"Uploaded {data.num_rows} rows to entrepreneurship_poland")
        
    save_state("entrepreneurship_poland", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
