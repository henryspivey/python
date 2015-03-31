
"""
countries = [['China','Beijing',1350],
             ['India','Delhi',1210],
             ['Romania','Bucharest',21],
             ['United States','Washington',307]]

# Write code to print out the capital of India
# by accessing the array.
def find_capital(l):
    
    for i in range(0,len(l)):
        name = l[i][0]
        capital = l[i][1]
        pop = l[i][2]
        print name,capital,pop
        
        
    
print find_capital(countries)

"""
"""
def product_list(l):
    factorial = 1
    i = 0
    for i in l:  # move through the list
        factorial = factorial * i
    return factorial
        
        
p = [1,2,3,4,55,6,7,8,9]
print product_list(p)
"""
"""
usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(l):
    fees = 0
    studs = 0
    
    for i in range(0,len(l)):
    	fees =  l[i][1] * l[i][2] + fees
    	studs += l[i][1]
    return studs,fees
   
            
                
print total_enrollment(usa_univs)



add_to_index(index,keyword,url):

add_page_to_index(index,url,content):
"""
import time

def time_execution(code):
  start = time.clock()
  result = eval(code)
  run_time = time.clock() - start
  return result, run_time

def spin_loop(n):
  i =0
  while i < n:
    i += 1

print time_execution('spin_loop(10**9)')[1]