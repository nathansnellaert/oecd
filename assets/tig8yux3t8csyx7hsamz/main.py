from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DF_TIG8YUX3T8CSYX7HSAMZ")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_tig8yux3t8csyx7hsamz")
        print(f"Uploaded {data.num_rows} rows to tig8yux3t8csyx7hsamz")
        
    save_state("tig8yux3t8csyx7hsamz", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
