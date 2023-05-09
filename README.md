# to-check-antivirus
This is python code to check antivirus is installed or not
this is only used for windows defender. 
if you want to it for another antivirus software we need to change the query accordingly
for example:-to find mecafe installed or not.


antivirus = wmi_obj.Win32_Product(Name="McAfee Endpoint Security")

```console.
import wmi

# Create a WMI object

wmi_obj = wmi.WMI()

# Query for the Windows Defender antivirus

antivirus = wmi_obj.Win32_Product(Name="Windows Defender Antivirus")

if len(antivirus) > 0:

    print("Windows Defender is installed.")

else:

    print("Windows Defender is not installed.")
```
