
def int_to_bytes32(value: int) -> bytes:
    assert(isinstance(value, int))
    return value.to_bytes(32, byteorder='big')


def bytes_to_int(value) -> int:
    if isinstance(value, bytes) or isinstance(value, bytearray):
        return int.from_bytes(value, byteorder='big')
    elif isinstance(value, str):
        b = bytearray()
        b.extend(map(ord, value))
        return int.from_bytes(b, byteorder='big')
    else:
        raise AssertionError


def bytes_to_hexstring(value) -> str:
    assert(isinstance(value, bytes) or isinstance(value, bytearray))
    return "0x" + "".join(map(lambda b: format(b, "02x"), value))


def bytes_to_address(value) -> str:
    return bytes_to_hexstring(value).replace("000000000000000000000000", "")


def hexstring_to_bytes(value: str) -> bytes:
    assert(isinstance(value, str))
    assert(value.startswith("0x"))
    return bytes.fromhex(value.replace("0x", ""))
