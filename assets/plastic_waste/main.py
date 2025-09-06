from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PW@DF_PW")
    
    if data.num_rows > 0:
        upload_data(data, "plastic_waste")
        print(f"Uploaded {data.num_rows} rows to plastic_waste")
        
    save_state("plastic_waste", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
