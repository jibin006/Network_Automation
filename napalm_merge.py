from napalm import get_network_driver

driver = get_network_driver("ios")

device_details = {
    "hostname" : "192.168.56.115",
    "username" : "cisco",
    "password": "cisco"
}

object = driver(**device_details)
object.open()

object.load_merge_candidate(config='interface loopback10\n ip address 192.168.100.1 255.255.255.0')

print(object.compare_config())
if len(object.compare_config()) > 0:
    choice = input("Y/N")
    if choice == "Y":
        print("commiting")
        object.commit_config()

    else:
        print("discarding")
        object.discard_config()

else:
   print("no difference")        
object.close()




