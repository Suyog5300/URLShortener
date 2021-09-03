import string
import random


def b62Encode(num):
    s = string.ascii_uppercase+string.ascii_lowercase+string.digits
    if num == 0:
        return '0'
    mycode = ""
    while num > 0:
        mycode = s[int(num%62)] + mycode
        num = num//62
    return mycode


def Shortened_Code(ref):
    instance = ref.__class__
    new_code = ""
    try:
        last_obj = instance.objects.latest('id')
        last_id = last_obj.id
        print(last_id)
        new_code = b62Encode(last_id)
    except:
        last_id = 0
        new_code = b62Encode(last_id)
    return new_code