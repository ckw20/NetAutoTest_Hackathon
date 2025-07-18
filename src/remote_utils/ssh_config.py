import sys 
import paramiko

from .ssh_config_template import *

private_key = paramiko.RSAKey.from_private_key_file("/root/.ssh/id_rsa")
ssh_config_A100_2 = ssh_config_template("starpub.star", 10017, "root", private_key)
ssh_config_dell_2 = ssh_config_template("dell-2.star", 8997, "vagrant", private_key)
ssh_config_wyz = ssh_config_template("183.173.13.208", 22, "wyz", private_key)
ssh_config_xet = ssh_config_template("10.0.9.37", 22, "root", private_key)
ssh_config_xrt = ssh_config_template("166.111.239.76", 2223, "xrt", private_key)


# ssh_config_dc4new = ssh_config_template("192.168.51.139", 22, "ckw20", private_key)
# ssh_config_dc6 = ssh_config_template("192.168.253.144", 22, "dc6", private_key)
# ssh_config_p4 = ssh_config_template("192.168.212.139", 22, "root", private_key)

# shell_config_dc4new = shell_config_template(ssh_config_dc4new, "/home/ckw20/capture_pcap/", "ckw20@ckw20")
# shell_config_dc6 = shell_config_template(ssh_config_dc6, "/home/dc6/pcaps/", "dc6@dc6-System-Product-Name")
# shell_config_p4_netbeacon = shell_config_template(ssh_config_p4, "/root/temp/netbeacon/", "root@localhost")