from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIE@DF_TIE_USA")
    
    if data.num_rows > 0:
        upload_data(data, "entrepreneurship_usa")
        print(f"Uploaded {data.num_rows} rows to entrepreneurship_usa")
        
    save_state("entrepreneurship_usa", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
