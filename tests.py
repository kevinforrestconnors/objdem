from owslib.wms import WebMapService

testsPassed = []
testsFailed = []


def assert_equal(a, b, name="A test"):
    if a == b:
        testsPassed.append(name)
    else:
        testsFailed.append(name)



def main():

    print(str(len(testsPassed)) + " tests passed.")
    print(str(len(testsFailed)) + " tests failed.")
    print("Tests failed: ")
    for test in testsFailed:
        print(test)

main()