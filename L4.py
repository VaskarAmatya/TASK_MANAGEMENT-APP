def main():
    try:
      n = int(input("Enter any number"))
      print(n)
      return

    except Exception as e:
       print("WE're in except")
       return

    finally:
        print("OH HII THERE")


main()



       
