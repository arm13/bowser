import sys
from datetime import datetime


try:
    from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice
    print('[%s] MonkeyRunner and MonkeyDevice Import Success' % datetime.now())
except ImportError:
    print('[%s] Android SDK Is Not Located In Your Path' % datetime.now())
    sys.exit(1)


def component(browser, packages, activities):

    """
    Build the target component

    """

    try:
        if browser and packages and activities:
            print('[%s] Target Browser: %s' % (datetime.now(), browser))
            package = getattr(packages, browser)
            activity = getattr(activities, browser)
            return "".join((package, '/', activity))
        else:
            print('[%s] Argument Error' % datetime.now())
    except Exception:
        print('[%s] Error!')
        raise


def harness(target_component, browser, check):

    """
    Harness the power of monkeyrunner

    """
    flask = ""

    if check == 'check':
        try:
            f = open('config', 'r+')
            address = f.readline()
            flask = "".join(('http://', address, ':5000', '/intent'))
        except IOError:
            print("[%s] Could Not Open File" % datetime.now())
    elif check == 'nocheck':
        try:
            # Apparently Jython doesn't support 'with' *shrugs*
            f = open('config', 'r+')
            address = f.readline()
            flask = "".join(('http://', address, ':5000', '/%s' % browser))
        except IOError:
            print("[%s] Could Not Open File" % datetime.now())

    # Should attempt to connect to your emulator or device
    device = MonkeyRunner.waitForConnection()

    if device:
        print('[%s] Device Successfully Connected' % datetime.now())
        try:
            print("[%s] Launching Component %s" % (datetime.now(), target_component))
            device.startActivity(uri=flask, component=target_component)
        except Exception:
            print('[*] Not Sure What Happened' % datetime.now())
            raise
        else:
            return True
    else:
        print("[%s] Could Not Connect To The device" % datetime.now())


def main(browser, check):

    """
    Handle all of bowser's main operations

    """

    # Attempt to import Packages and Activities
    try:
        from enums.packages import Packages
        from enums.activities import Activities
        packages = Packages()
        activities = Activities()
        target_component = component(browser, packages, activities)
        print('[%s] Target Component: %s' % (datetime.now(), target_component))
        if target_component:
            if harness(target_component, browser, check):
                print('[%s} Returned Successfully' % datetime.now())
    except ImportError:
        print('[%s] Could Not Import Packages' % datetime.now())
        sys.exit(1)


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print("[%s] Not Enough Arguments")
        print("[%s] Usage: monkeyrunner bowser.py mercury [nocheck, check]")
        sys.exit(1)
    else:
        try:
            # Call main()
            main(sys.argv[1], sys.argv[2])
            print("[%s] Running Bowser!" % datetime.now())
        except KeyboardInterrupt:
            sys.exit(0)