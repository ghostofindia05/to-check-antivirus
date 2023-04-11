import wmi

# Create a WMI object

wmi_obj = wmi.WMI()

# Query for the Windows Defender antivirus

antivirus = wmi_obj.Win32_Product(Name="Windows Defender Antivirus")

if len(antivirus) > 0:

    print("Windows Defender is installed.")

else:

    print("Windows Defender is not installed.")
