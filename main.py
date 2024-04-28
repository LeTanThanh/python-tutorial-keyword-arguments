if __name__ == "__main__":
  # Introduction to the Python keyword arguments

  # def get_net_price(price, discount):
  #   return price * (1 - discount)

  # net_price = get_net_price(100, 0.1)
  # print(net_price)

  """
  fn(parameter1 = value1, parameter2 = value2)
  fn(parameter2 = value2, parameter1 = value1)
  """

  # print(get_net_price(price = 100, discount = 0.1))
  # print(get_net_price(discount = 0.1, price = 100))
  # print(get_net_price(100, discount = 0.1))

  # Keyword arguments and default parameters

  def get_net_price(price, tax = 0.07, discount = 0.05):
    return price * (1 + tax - discount)

  print(get_net_price(100))
  print(get_net_price(100, 0.06))
  print(get_net_price(price = 100, discount = 0.06))
  print(get_net_price(100, discount = 0.06))