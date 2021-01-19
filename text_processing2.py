#######################
# Test Processing II  #
#######################
import re
def digits_to_words(input_string):
    num_dict={
        '0':'zero',
        '1':'one',
        '2':'two',
        '3':'three',
        '4':'four',
        '5':'five',
        '6':'six',
        '7':'seven',
        '8':'eight',
        '9':'nine'
    }
    digit_string=''
    for s in input_string:
        if s.isdigit():
            print(s)
            digit_string+=num_dict[s]
            digit_string+=' '
    return digit_string

def to_camel_case(underscore_str):
    res=re.split('[_?]',underscore_str)
    res=[ele.lower() for ele in res if ele!='']
    print(res)
    camelcase_str=''
    if res:
        camelcase_str+=res[0]
    for i in range(1,len(res)):
        res[i]=res[i].capitalize()
        camelcase_str+=res[i]
    return camelcase_str
