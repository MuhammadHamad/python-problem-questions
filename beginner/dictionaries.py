
# !Input :-
''' myinfo = {
            "server1" : {
                    "IBM": {
                        "datacenter":"Bangalore",
                        "env": {
                                "PR": "192.168.1.1",
                                "DR": "192.168.1.2"
                                }
                            }
                    }
            } '''

# !Output :-
# Bangalore datacenter PR address is : 192.168.1.1
# Bangalore datacenter DR address is : 192.168.1.2

myinfo = {
    "server1": {
        "IBM": {
            "datacenter": "Bangalore",
            "env": {
                "PR": "192.168.1.1",
                "DR": "192.168.1.2"
            }
        }
    }
}

bangalore_PR = myinfo["server1"]["IBM"]["env"]['PR']
bangalore_DR = myinfo["server1"]["IBM"]["env"]['DR']

print(f"Bangalore datacenter PR address is : {bangalore_PR}")
print(f"Bangalore datacenter DR address is : {bangalore_DR}")