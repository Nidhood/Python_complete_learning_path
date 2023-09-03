print("\n<Errors>\n")
#  We are going to use the nex reserved words:
#  try: Test code since appears an error.
#  except: Code that will execute if the error appears in the try part.
#  finally: executes in the end of the program regardless of an error.
print("* Example #1 : ", end="")


def function_1(n1, n2):
    print(n1 + n2)


try:
    #  WANT TO ATTEMPT THIS CODE
    #  MAY HAVE AN ERROR
    result = 10 + 10
except:
    print("Hey it looks like you aren't adding correctly!")
else:
    print("Add went well! ", end="")
    print(result)

print("* Example #2 : ", end="")
try:
    f = open('testfile', 'r')
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS error!")
finally:
    print("I always run!")
print("* Example #2 : ", end="")


def function_2():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number!")
            continue
        else:
            print("Yes thank you!")
            break
        finally:
            print("End of try/except/finally")
            print("I will always run at the end!")


function_2()
