from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_CARTEL_QDD@DF_QDD_CARTEL")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_international_cartels_database")
        print(f"Uploaded {data.num_rows} rows to international_cartels_database")
        
    save_state("international_cartels_database", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
