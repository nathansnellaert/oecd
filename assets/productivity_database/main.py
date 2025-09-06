from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_PDB@DF_PDB")
    
    if data.num_rows > 0:
        upload_data(data, "productivity_database")
        print(f"Uploaded {data.num_rows} rows to productivity_database")
        
    save_state("productivity_database", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
