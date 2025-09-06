from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIE@DF_TIE_FRA")
    
    if data.num_rows > 0:
        upload_data(data, "entrepreneurship_france")
        print(f"Uploaded {data.num_rows} rows to entrepreneurship_france")
        
    save_state("entrepreneurship_france", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
