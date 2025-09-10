from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TIE@DF_TIE_ESP")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_entrepreneurship_spain")
        print(f"Uploaded {data.num_rows} rows to entrepreneurship_spain")
        
    save_state("entrepreneurship_spain", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
