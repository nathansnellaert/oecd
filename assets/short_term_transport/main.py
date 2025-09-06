from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_ST@DF_STINDICATORS")
    
    if data.num_rows > 0:
        upload_data(data, "short_term_transport")
        print(f"Uploaded {data.num_rows} rows to short_term_transport")
        
    save_state("short_term_transport", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
