import subprocess
import os
 
subprocess.run(["python", "./install_resouces.py"])

if os.path.exists('merge_race_result.csv') and os.path.exists('best_team_pit_stop.csv') and os.path.exists('df_constructor_standings.csv') and os.path.exists('df_driver_standings.csv'):
    print('file already exist')
else:
    print("lancement du processuce du nettoyage de données")
    subprocess.run(["python", "./F1_dataviz_last.py"]) 
    
subprocess.run(["python", "./first_dash_test.py"])