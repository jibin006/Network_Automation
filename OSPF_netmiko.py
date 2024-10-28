from netmiko import ConnectHandler

# List of routers
Router_List = ['192.168.56.115', '192.168.56.116', "192.168.56.117 "]

# User credentials
username = input('Please Enter Your Username: ')
password = input('Please Enter Your Password: ')

# Function to configure the interface
def interface_config(ssh):
    int_name = input('Enter Interface Name: ')
    ip_address = input('Enter IP Address: ')
    subnet_mask = input('Enter Subnet Mask: ')
    
    commands = [f'interface {int_name}', f'ip address {ip_address} {subnet_mask}']
    result = ssh.send_config_set(commands)
    print(result)
    
    # Show interface status after configuration
    int_brief = ssh.send_command('show ip interface brief')
    print(int_brief)

# Function to configure OSPF
def ospf_config(ssh):
    ospf_proc_id = input('Enter OSPF Process ID: ')
    ospf_router_id = input('Enter Router ID: ')
    network_count = int(input('How Many Networks to Advertise: '))

    commands = [f'router ospf {ospf_proc_id}', f'router-id {ospf_router_id}']
    
    for _ in range(network_count):
        network_id = input('Enter Network ID: ')
        wildcard_mask = input('Enter Wildcard Mask: ')  
        area_id = input('Enter Area ID: ')
        commands.append(f'network {network_id} {wildcard_mask} area {area_id}')
    
    result = ssh.send_config_set(commands)
    print(result)

# Main logic for user choice
def main():
    user_choice = input('1. Interface Config\n2. OSPF Config\nPlease Make a Choice (1/2): ')
    
    if user_choice not in ['1', '2']: 
        print('Invalid choice. Please try again.')  
        return

    for router in Router_List:
        device = {
            'device_type': 'cisco_ios',
            'host': router,
            'username': username,
            'password': password,
            
        }

        print(f'Connecting to Router {router}...')
        ssh = ConnectHandler(**device)
        ssh.enable()
        
        if user_choice == '1':
            interface_config(ssh)
        elif user_choice == '2':
            ospf_config(ssh)

        ssh.disconnect()

if __name__ == '__main__':
    main() 
