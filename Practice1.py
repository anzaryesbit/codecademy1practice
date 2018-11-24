def ground_shipping(weight):
  if weight <= 2:
    cost = 1.50*weight + 20.00
    return cost
  elif 2 < weight <= 6:
    cost = 3.00*weight + 20.00
    return cost
  elif 6 < weight <= 10:
    cost = 4.00*weight + 20.00
    return cost
  else:
    cost = 4.75*weight + 20.00
    return cost
premium_ground_shipping = 125.00
def drone_shipping(weight):
  if weight <= 2:
    cost = 4.50*weight
    return cost
  elif 2 < weight <= 6:
    cost = 9.00*weight
    return cost
  elif 6 < weight <= 10:
    cost = 12.00*weight
    return cost
  else:
    cost = 14.25*weight
    return cost
def greater_weight(weight):
  if ground_shipping(weight) < premium_ground_shipping and ground_shipping(weight) < drone_shipping(weight):
    return print("ground shipping is cheapest because it is $"+ str(ground_shipping(weight)))
  elif drone_shipping(weight) < premium_ground_shipping and ground_shipping(weight) > drone_shipping(weight):
    return print("drone shipping is cheapest because it is $" + str(drone_shipping(weight)))
  else:
    print("premium ground shipping is the cheapest because it is $" + str(premium_ground_shipping))
greater_weight()
