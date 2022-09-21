from netmiko import ConnectHandler
import getpass as gp

#For testing purposes you may use vpnrt2.grr, 169.254.16.29 (this is for AWS)

def main():

    get_host_name = input('Host name? (Do NOT add expertcity.com! Example: asr1k.las)\n')
    get_username = read_username()
    get_fqdn = input(str('Input you fully-qualified domain name: (If using expertcity.com, you may leave this blank, simply press ENTER)\n'))

    if get_fqdn == '':
        get_fqdn = 'expertcity.com'
    
    get_password = gp.getpass()
    get_neighbor_ip_address = input(str('Please enter the neighbors IP address:\n'))
    run_command(get_host_name, get_username, get_password, get_neighbor_ip_address, get_fqdn)


def read_username():

    with open('username.txt', 'r', encoding='utf-8') as f:
        username = f.readline()
        print(f'Username is {username}')

    return username


def run_command(s_host, s_username, s_password, s_ip, s_fqdn):

    try:

        final_host = str(s_host) + '.' + s_fqdn

        #final_host = str(s_host) + '.expertcity.com'
        neighbor_ip_address = s_ip

        net_connect = ConnectHandler(
            device_type = 'cisco_ios',
            host = final_host,
            username = s_username,
            password = s_password,
        )

        show_description_command = f'show ip bgp all neighbors {neighbor_ip_address} | include Description'
        show_bgp_state_command = f'show ip bgp all neighbors {neighbor_ip_address} | include BGP state'
        show_interface_associated_state_command = f'show ip bgp all neighbors {neighbor_ip_address} | include Interface associated'
        show_last_reset = f'show ip bgp all neighbors {neighbor_ip_address} | include Last reset'

        # Testing command with all info
        # exec_command = 'show ip bgp all neighbors 10.16.10.52 | include Description|BGP state|Interface associated|Last reset'
        
        output_description = net_connect.send_command(show_description_command)
        output_bgp_state = net_connect.send_command(show_bgp_state_command)
        output_show_interface_associated_state = net_connect.send_command(show_interface_associated_state_command)
        output_last_reset = net_connect.send_command(show_last_reset)

        print('\n--- Lets determine the peer provider, BGP state, local interface and sub-interface ---\n\n--- Commands full info ---\n')

        print(f'\nCommand executed: {show_description_command} \nResults:\n{output_description}\n')

        aws_word = 'AWS'

        print(f'\n\nCommand executed: {show_bgp_state_command} \nResults:\n{output_bgp_state}\n')

        bgp_down = 'down'

        if bgp_down in output_bgp_state:
            print('\nBe aware:\n---> BGP is DOWN! <---\n')
            if aws_word in output_description:
                print('This is AWS, please consider waiting up to 5hrs before taking any actions.\nPlease follow https://confluence.ops.expertcity.com/pages/viewpage.action?pageId=198357312 if needed.')

        else:
            print('\n---> BPG is UP <---.\n')

        print(f'\nCommand executed: {show_interface_associated_state_command} \nResults:\n{output_show_interface_associated_state}\n')
        print(f'\nCommand executed: {show_last_reset} \nResults:\n{output_last_reset}\n')
        
        print('\n--- Local Interface Status ---\n')
        
        split_interface_associated = output_show_interface_associated_state.split()

        #print(split_interface_associated)

        #Example command: show interface TenGigabitEthernet0/1/0.300 | include line protocol|Description

        show_local_interface_status_command = f'show interface {split_interface_associated[2]} | include line protocol|Description'

        output_local_interface_status_command = net_connect.send_command(show_local_interface_status_command)

        print(f'\nCommand executed: {show_local_interface_status_command} \nResults:\n{output_local_interface_status_command}\n')

        is_down = 'down'

        if is_down in output_local_interface_status_command:
            print('Interface is down! :(\n\nPlease check: https://confluence.ops.expertcity.com/pages/viewpage.action?pageId=266269157\n')
            
        else:
            print('Interface is up!')
        
    except:
        print('Something went wrong! Please review your credentials and try again :D')

if __name__ == '__main__':
    main()

    print('\nProcess has been completed!')