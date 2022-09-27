from netmiko import ConnectHandler
import getpass as gp

#For testing purposes, you may use edge2.las, 10.16.16.21

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
    
    try:
        with open('username.txt', 'r', encoding='utf-8') as f:
            username = f.readline()
            print(f'Username is {username}')

        return username
    except:
        print('Please make sure you have the "username.txt" file with your user on it :D')


def run_command(s_host, s_username, s_password, s_ip, s_fqdn):

    try:
    
        final_host = str(s_host) + '.' + s_fqdn

        neighbor_ip_address = s_ip

        net_connect = ConnectHandler(
            device_type = 'juniper_junos',
            host = final_host,
            username = s_username,
            password = s_password,
        )

        #Below are the commands we'll be running and there's also commented a quick successfull test
        #test_command = f'show bgp neighbor {neighbor_ip_address} | match "Description|Type|Local:|Local Interface"'
        #output_test = net_connect.send_command(test_command)
        #print(output_test)

        show_description_command = f'show bgp neighbor {neighbor_ip_address} | match "Description"'
        show_type_command = f'show bgp neighbor {neighbor_ip_address} | match "Type"'
        show_local_command = f'show bgp neighbor {neighbor_ip_address} | match "Local:"'
        show_local_interface_command = f'show bgp neighbor {neighbor_ip_address} | match "Local Interface"'

        output_description = net_connect.send_command(show_description_command)
        output_type = net_connect.send_command(show_type_command)
        output_local = net_connect.send_command(show_local_command)
        output_local_interface = net_connect.send_command(show_local_interface_command)

        #test_command = f'show bgp neighbor {neighbor_ip_address} | match "Description|Type|Local:|Local Interface"'

        #output_test = net_connect.send_command(test_command)

        #print(output_test)

        print('\nLets determine the peer provider, BGP state, local interface and sub-interface\n')

        print(f'\nCommand executed: {show_description_command} \nResults:\n{output_description}\n')
        print(f'\nCommand executed: {show_type_command} \nResults:\n{output_type}\n')
        print(f'\nCommand executed: {show_local_command} \nResults:\n{output_local}\n')
        print(f'\nCommand executed: {show_local_interface_command} \nResults:\n{output_local_interface}\n')

        #print(f'\nLen for local interface: {len(output_local_interface)}\n')

        local_interface = ''

        if len(output_local_interface) < 50:

            split_output_local = output_local.split()

            print(f'\nThis is the FULL split result: {split_output_local}\n')

            splitter = '+'
            local_ip = split_output_local[5].split(splitter)
            local_ip = local_ip[0]

            print(f'\nThis is just the IP we need without the +: {local_ip}\n')

            #Now that we splitted things up, let's run the commands

            show_local_interface_terse_command = f'show interface terse | match {local_ip}'
            output_local_interface_terse = net_connect.send_command(show_local_interface_terse_command)
            
            #In case the local interface is not showing, this additional command will  help.
            
            print(f'\nCommand executed: {show_local_interface_terse_command} \nResults:\n{output_local_interface_terse}\n')

            #Let's now get the local interface from the command above

            local_interface = output_local_interface_terse.split()

            local_interface = local_interface[0]

            #print(f'This is the SPLIT for local interface 0: {local_interface}')

            local_interface = local_interface.split('.')

            local_interface = local_interface[0]

            #print(f'\nThis is the local interface after: {local_interface}')

        else:

            local_interface = output_local_interface.split()

            local_interface = local_interface[2]

            #print(f'\nThis is the local interface taken from the output local interface command: {local_interface}')

            local_interface = local_interface.split('.')

            local_interface = local_interface[0]

            #print(f'\nThis is the local interface after: {local_interface}')

        #Now that we have the local interface, let's verify how long it has been down

        show_bgp_summary_command = f'show bgp summary | match {neighbor_ip_address}'
        output_bgp_summary = net_connect.send_command(show_bgp_summary_command)

        print(f'\nCommand executed: {show_bgp_summary_command} \nResults:\n{output_bgp_summary}\n')

        #Let's now verify the local interface status

        show_interfaces_description_command = f'show interfaces descriptions | match {local_interface}'
        output_interfaces_description = net_connect.send_command(show_interfaces_description_command)

        print(f'\nCommand executed: {show_interfaces_description_command} \nResults:\n{output_interfaces_description}\n')
        
        if 'up' in output_interfaces_description:
            print(f'\nInterface is down\n')

            get_cid = output_interfaces_description.split(':')
            print(f'\nThis is the GET CID output: {get_cid}')

            get_cid = get_cid[2]

            print(f'\nThis is just the CID we need: {get_cid}')

            print("""
            
For VSP Peers follow Addressing VSP Alerts -SOP 
(https://confluence.ops.expertcity.com/display/NPV/Addressing+VSP+Alerts+-SOP)

For AWS Peers follow 169.254.X.X BGP alerts (NOC)
https://confluence.ops.expertcity.com/pages/viewpage.action?pageId=198357312

There is a planned maintenance going on by the provider
    Using the CID or Peer IP
        Check Watchtower
        Check your email
Resolution: inform the Network team on-call as FYI and monitor the alert for resolution

An outage is happening on the provider side
    Open a support ticket with the respective provider of either the BGP Peering or the physical link and follow up accordingly

An unannounced internal change or decommission happen
    Using the CID, Peer IP or network device name
    Check slack
    Check Jira tickets
        Resolution: educate the person that did the change about the change management process and ask for an SDT on the alerts or them to be removed if no longer needed


This is the Contact & Escalation link: 
https://confluence.ops.expertcity.com/pages/viewpage.action?pageId=86823796

            """)

            print('\nIf needed, this is the email that could be sent to the provider\n\n')

            #Email goes here

            is_switch = False

            template = switch_template(get_cid, output_interfaces_description, is_switch)

            print(template)

        else:
            print('Interface is okay, no worries :D')


        net_connect.disconnect()
        
    except:
        net_connect.disconnect()
        print('Something went wrong! Please review your credentials and try again :D')


#This function will help us generate the email's tempalte when needed, if SWITCH security code is a must. Otherwise, it will not be added.

def switch_template(cid, interfaces_description, is_switch):

    if is_switch is True:
        
        ticket_template = f"""
            
Hello [REPLACE THIS WITH THE PROVIDER'S NAME],

Security code -- XXXX [REMEMBER TO ADD THE SECURITY CODE HERE]

We're showing that CID {cid} went down. No records of maintenance activities were found. 

Please investigate and let us know the root cause of this event. Details are below:
{interfaces_description}

Regards,

----

-- YOUR SIGNATURE GOES HERE -- 

            """
    else:
                ticket_template = f"""
            
Hello [REPLACE THIS WITH THE PROVIDER'S NAME],

We're showing that CID {cid} went down. No records of maintenance activities were found. 

Please investigate and let us know the root cause of this event. Details are below:
{interfaces_description}

Regards,

----

-- YOUR SIGNATURE GOES HERE -- 

            """
        

    return ticket_template


if __name__ == '__main__':
    main()

    print('\nProcess has been completed!')