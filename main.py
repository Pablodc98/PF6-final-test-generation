import requests as rq

url = 'https://api-colombia.com/api/v1/TypicalDish'


def dish_fetch(num):
  response = rq.get(f"{url}/{num}")
  if response.status_code == 200:
    return response.json()
  else:
    print("Error fetching data:", response.status_code)


def main():
  print("Hello learners, you need to learn english to run this program.")
  while True:
    try:
      entry = input("Enter a number between 1 and 10 to fetch a typical dish (or type 'exit' to quit): ")
      if entry.lower() == 'exit' or entry.lower() == 'salir':
        print("Exiting the program. Goodbye!")
        break
      num = int(entry)
      result = dish_fetch(num)
      print(f"Typical Dish {num}: {result}")
    except ValueError:
      print("Invalid input. Please enter a valid number between 1 and 10 or type 'exit' to quit.")  



if __name__=="__main__":
  main()