from utils import save_state, upload_data
from datetime import datetime
from general import fetch_data

def main():
    data = fetch_data("DSD_TQ_SURVEY@DF_TRUTH_QUEST")
    
    if data.num_rows > 0:
        upload_data(data, "truth_quest_survey")
        print(f"Uploaded {data.num_rows} rows to truth_quest_survey")
        
    save_state("truth_quest_survey", {
        "last_updated": datetime.now().isoformat(),
        "row_count": data.num_rows
    })
    
    return data
