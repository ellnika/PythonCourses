'''
6.5 Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.

str = 'X-DSPAM-Confidence:0.8475'
'''

str = 'X-DSPAM-Confidence:0.8475'
colon=str.find(":")
print(colon)
end = len(str)
end_int=int(end)
print(end_int)

searched_string=str[colon+1: end_int]
print(searched_string)
searched_string_float=float(searched_string)
print(searched_string_float)