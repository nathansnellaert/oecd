from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_DAC2@DF_ODF")
    
    if data.num_rows > 0:
        upload_data(data, "official_development_financing")
        print(f"Uploaded {data.num_rows} rows to official_development_financing")
        
    save_state("official_development_financing", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
