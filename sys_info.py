import subprocess

h_w_components={
        "CPU":"lscpu", 
        "MEMORY":"dmidecode -t memory", 
        "HARDISK":"smartctl -a /dev/sda", 
        "PCI DEVICES":"lspci", 
        "USB DEVICES": "lsusb", 
        "ETHERNET MAC": "['ip addr show', 'nmcli', 'ifconfig', 'cat /sys/class/net/enp0s3/address']", 
        "MB":"dmidecode -t system",
        "BIOS":"dmidecode -t bios" 
}
def get_sys_info(i):
    result= subprocess.run(i, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        return result.stdout
    else:
        return f"Error: {result.stderr}"
    

for component in h_w_components:
    print(get_sys_info(component))
