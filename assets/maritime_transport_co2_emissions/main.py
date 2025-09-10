from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_MARITIME_TRANSPORT@DF_MARITIME_TRANSPORT")
    
    if data.num_rows > 0:
        upload_data(data, "oecd_maritime_transport_co2_emissions")
        print(f"Uploaded {data.num_rows} rows to maritime_transport_co2_emissions")
        
    save_state("maritime_transport_co2_emissions", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
