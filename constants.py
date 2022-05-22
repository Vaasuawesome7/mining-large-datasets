SUPPORT_THRESHOLD = 3

HASH_TABLE_SIZE_PCY = 512
HASH_TABLE_SIZE_MS1 = 512
HASH_TABLE_SIZE_MS2 = 512
HASH_TABLE_SIZE_MH1 = 256
HASH_TABLE_SIZE_MH2 = 256

def hash_function_pcy(items: list):
    s = 0
    p = 1
    for item in items:
        s += item
        p *= item
    res: int = (s + p)
    return res % HASH_TABLE_SIZE_PCY

def hash_function_ms1(items: list):
    s = 0
    p = 1
    for item in items:
        s += item
        p *= item
    res: int = (s + p)
    return res % HASH_TABLE_SIZE_MS1

def hash_function_ms2(items: list):
    s = 0
    p = 1
    for item in items:
        s += item
        p *= item
    res: int = (s * p)
    return res % HASH_TABLE_SIZE_MS2

def hash_function_mh1(items: list):
    s = 0
    p = 1
    for item in items:
        s += item
        p *= item
    res: int = (s + p)
    return res % HASH_TABLE_SIZE_MH1

def hash_function_mh2(items: list):
    s = 0
    p = 1
    for item in items:
        s += item
        p *= item
    res: int = (s * p)
    return res % HASH_TABLE_SIZE_MH2