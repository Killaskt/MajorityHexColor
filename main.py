hexMap = {
  'F': 15,
  'E': 14,
  'D': 13,
  'C': 12,
  'B': 11,
  'A': 10,
}

def hex_max(arr):

  # get the largest hex number
  
  a,b = arr
  
  a = (a if type(a) == int or float else hexMap[a])
  b = (b if type(b) == int or float else hexMap[b])

  return a + b;

def calc_hex_color(hex):

  # Get the color of the hex code

  names = {0: 'red', 1: 'green', 2:'blue'}

  cols = []
  
  cols.append(hex_max(hex[1:3]))
  cols.append(hex_max(hex[3:5]))
  cols.append(hex_max(hex[5:7]))
  
  max_idx = cols.index(max(cols))

  return names[max_idx]

ex = '#33ff55'
ex2 = '#1244e5'
  
# example usage
print(f"majority color for {ex} is {calc_hex_color(ex)}")
print(f"majority color for {ex2} is {calc_hex_color(ex2)}")
  