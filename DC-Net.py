
def main():
    a_secret_key, a_broadcast_data = alice('8AD5', '7639')
    b_secret_key, b_broadcast_data = bob('C08E', 'D2BA')
    message = 'A779'
    message = convert_to_binary(message)
    status = 0
    print(dc_net(a_secret_key, a_broadcast_data, b_secret_key, b_broadcast_data, message, status))


def convert_to_binary(string_input):
    string_input = int(string_input, 16)
    return bin(string_input)[2:].zfill(16)


def alice(secret_key, broadcast_data):
    return convert_to_binary(secret_key), convert_to_binary(broadcast_data)


def bob(secret_key, broadcast_data):
    return convert_to_binary(secret_key), convert_to_binary(broadcast_data)


def dc_net(alice_secret, alice_broadcast, bob_secret, bob_broadcast, secret_message, status_bit):
    out_put = []
    out_put_secret= []
    if status_bit == 0:
        for bit in range(0, 16):
            out_put.append(int(alice_secret[bit]) ^ int(bob_secret[bit]))
            out_put_secret.append(int(alice_broadcast[bit]) ^ int(bob_broadcast[bit]) ^ int(out_put[bit]))
        out_put = ''.join(str(x) for x in out_put)
        out_put_secret = ''.join(str(x) for x in out_put_secret)
        return hex(int(out_put,2)), hex(int(out_put_secret,2))
    else:
        for bit in range(0, 16):
            out_put.append(int(alice_secret[bit]) ^ int(bob_secret[bit]) ^ int(secret_message[bit]))
    out_put = ''.join(str(x) for x in out_put)
    return hex(int(out_put,2))


if __name__ == "__main__":
    main()
