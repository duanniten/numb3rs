from numb3rs import validate

def test_check_valid_ip():
    list_ips = [
        '192.168.1.1',
        '1.1.1.1',
        '255.255.255.255',
        '0.0.0.0',
        '99.255.0.3',
    ]
    for ip in list_ips:
        assert validate(ip) == True

def test_check_invalid_ip():
    list_ips = [
        '256.168.1.1',
        '1.256.1.1',
        '255.255.257.255',
        '0.0.0.998',
        '99.255.0',
        '1111.0.0.0'
    ]
    for ip in list_ips:
        assert validate(ip) == False
