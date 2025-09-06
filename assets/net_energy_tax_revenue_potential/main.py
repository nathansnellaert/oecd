from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_NEER@DF_REVPOT")
    
    if data.num_rows > 0:
        upload_data(data, "net_energy_tax_revenue_potential")
        print(f"Uploaded {data.num_rows} rows to net_energy_tax_revenue_potential")
        
    save_state("net_energy_tax_revenue_potential", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
