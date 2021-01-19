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
            digit_string+=num_dict[s]
            digit_string+=' '
    return digit_string[:-1]

def to_camel_case(underscore_str):
    res=re.split('[_?]',underscore_str)
    res=[ele for ele in res if ele!='']
    camelcase_str=''
    if res:
        if res[0].islower():
            camelcase_str+=res[0]
        else:
            camelcase_str+=res[0].lower()
    for i in range(1,len(res)):
        res[i]=res[i].lower().capitalize()
        camelcase_str+=res[i]
    return camelcase_str
