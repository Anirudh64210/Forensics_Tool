import subprocess
import json

def get_antivirus_detections():
    command = 'Get-MpThreatDetection'
    powershell_process = subprocess.Popen(['powershell', '-Command', command], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = powershell_process.communicate()
    
    if powershell_process.returncode == 0:
        detections = json.loads(stdout.decode('utf-8'))
        return detections
    else:
        print("Error:", stderr.decode('utf-8'))
        return []

antivirus_detections = get_antivirus_detections()

for detection in antivirus_detections:
    print("Threat Name:", detection['ThreatName'])
    print("Severity:", detection['Severity'])
    print("Status:", detection['Status'])
    print("==================================")
