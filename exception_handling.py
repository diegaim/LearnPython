myData = "23 asd"
message = str()
try:
    convData = int(myData)
    message = "Success convData to integer"
except Exception as e:
    message = "Failed convert myData to integer value.\n" + str(e)
finally:
    print("%s" % message)