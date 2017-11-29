from owslib.wms import WebMapService

testsPassed = []
testsFailed = []


def assert_equal(a, b, name="A test"):
    if a == b:
        testsPassed.append(name)
    else:
        testsFailed.append(name)


def web_map_service():
    wms = WebMapService('http://webmap.ornl.gov/ogcbroker/wms', version='1.1.1')
    assert_equal(wms.identification.type, 'OGC:WMS', "WMS Type Is Correct")
    assert_equal(wms.identification.title, 'ORNL DAAC WMS Server', "WMS Title is Correct")

def gtopo_is_10003_1():
    wms = WebMapService('http://webmap.ornl.gov/ogcbroker/wms', version='1.1.1')
    for name in list(wms.contents):
        if name == '10003_1':
            print(wms[name].title)
            assert_equal(wms[name].title, 'GLOBAL 30 ARC-SECOND ELEVATION (GTOPO30)', "gtopo_is_10003_1")

def main():
    web_map_service()
    gtopo_is_10003_1()
    print(str(len(testsPassed)) + " tests passed.")
    print(str(len(testsFailed)) + " tests failed.")
    print("Tests failed: ")
    for test in testsFailed:
        print(test)

main()