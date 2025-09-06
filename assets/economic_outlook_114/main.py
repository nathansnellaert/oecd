from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_EO_114@DF_EO_114")
    
    if data.num_rows > 0:
        upload_data(data, "economic_outlook_114")
        print(f"Uploaded {data.num_rows} rows to economic_outlook_114")
        
    save_state("economic_outlook_114", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
