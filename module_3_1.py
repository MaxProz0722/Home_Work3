calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    tuple = (len(string), string.upper(), string.lower())
    global calls
    calls += 1
    return tuple

def is_contains(string, list_to_search):
    new_li = [x.upper() for x in list_to_search]
    upstring = string.upper()
    print(upstring in new_li)
    global calls
    calls += 1


call = string_info('chupacabra')
call_2 = string_info('bibika')
print(call)
print(call_2)
is_contains('BaLaLika', ['kukushkA', 'BaLalaika', 'vodka', 'seledka'])
is_contains('VoDkA', ['kukushkA', 'BaLalaika', 'vodka', 'seledka'])
print(calls)