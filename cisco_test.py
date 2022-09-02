from netmiko import ConnectHandler

def main():

    get_host_name = input('Host name? (Do NOT add expertcity.com! Example: asr1k.las)\n')
    get_username = 'ddiaz'
    get_password = input('Please input your password.\n')
    run_command(get_host_name, get_username, get_password)

def run_command(s_host, s_username, s_password):

    final_host = str(s_host) + '.expertcity.com'

    net_connect = ConnectHandler(
        device_type = 'cisco_ios',
        host = final_host,
        username = s_username,
        password = s_password,
    )

    output = net_connect.send_command(
        "show ip bgp all neighbors 10.16.10.52 | include Description|BGP state|Interface associated|Last reset"
    )
    print(output)


if __name__ == '__main__':
    main()