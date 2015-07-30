s = "100 NORTH MAIN ROAD"
print s.replace("ROAD", 'RD.')
s= "100 NORTH BROAD ROAD"
print s.replace("ROAD", "RD.")

# import regex module
import re
re.sub("ROAD$", 'RD.', s) # the $ means the occurrence must be at the end of the string


s = "100 BROAD"
print re.sub("ROAD$", 'RD.',s)
print re.sub("\\bROAD$", 'RD.',s) # the \b means a boundary must occur here
print re.sub(r'\bROAD$', 'RD.',s) #the r doesn't allow anything to be escaped
s = "100 BROAD ROAD APT. 3"
print re.sub(r'\bROAD$', 'RD.', s)
print re.sub(r'\bROAD\b', 'RD.', s)


# roman numerals - checking for thousands
import re
pattern = '^M?M?M?$'
# the pattern has 3 parts,
# ^ match what follows only at the beginning of the string
# M? to optionally match a single M character; we try to search for up to 3 Ms
# $ to match what precedes only at the end of the string. When combined with the ^ character
# the pattern must match the entire string

print re.search(pattern, 'M')
print re.search(pattern, 'MM')
print re.search(pattern, 'MMM')
print re.search(pattern, 'MMMM')
print re.search(pattern, '')

# checking for hundreds
pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'
print re.search(pattern, "MCM")
print re.search(pattern, "MD")
print re.search(pattern, "MMMCCC")
print re.search(pattern, "MCMC")
print re.search(pattern, '')


# different syntax
pattern = 'M{0,3}$' # match 0 to 3 characters
print re.search(pattern, 'M')
print re.search(pattern, 'MM')
print re.search(pattern, 'MMM')
print re.search(pattern,'MMMM')

# checking for tens and ones
pattern = '^M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'
print re.search(pattern, 'MCMXL')
print re.search(pattern, 'MCML')
print re.search(pattern, 'MCMLX')
print re.search(pattern, 'MCMLXXX')
print re.search(pattern, 'MCMLXXXX')
print re.search(pattern, 'CMLXX')
# using alternate syntax
pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
print re.search(pattern, "MDLV")
print re.search(pattern, "MMDCLXVI")
print re.search(pattern, "MMMMDCCCLXXXVIII")
print re.search(pattern, "I")


# parsing phonenumbers
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$') 
# {3} means match exactly 3 numeric digits. \d means any digit between 0-9
print phonePattern.search('800-555-1212').groups()

# dealing with an extension
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
print phonePattern.search('800-444-1211-1234').groups()
# this won't match numbers without an extension

phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
# \D+ matches 1 or more characters that are not digits

phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d+)$')
# \D* matches 0 or more characters that are not digits
# final version
phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d+)$')
# not matching at the beginning of the string.
# regex will do the hard part of finding where the string starts
print phonePattern.search('work 1-(800) 555.1212 #1234').groups()        
print phonePattern.search('800-555-1212')                     
print phonePattern.search('80055512121234')
                  
