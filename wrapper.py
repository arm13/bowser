
import datetime as datetime
import zipfile

# Configure path
import sys
sys.path.append("/Users/rotlogix/Tools/mobile/android/androguard")

# Configure terminal colors
from blessings import Terminal
t = Terminal()

# Attempt Androguard import
try:
    from androguard.core.analysis import analysis
    from androguard.core.bytecodes.apk import APK as APK
    from androguard.core.bytecodes import dvm as DVM
    from androguard.core.androgen import AndroguardS
except ImportError as e:
    print(t.yellow("[{0}] Unable to import Androguard!".format(datetime.datetime.now())))
else:
    print(t.yellow("[{0}] Androguard imported successfully!".format(datetime.datetime.now())))


def search(apks, dx):

    """
    Search for implementations
    """

    # Important methods for searching
    methods = {'parse': 'parseUri', 'load': 'loadUrl', 'js': 'addJavascriptInterface'}

    print(t.yellow("[{0}] Searching for parseUri implementation ...".format(datetime.datetime.now())))
    parse_uri = dx.get_tainted_packages().search_methods("Landroid/content/Intent", methods["parse"], ".")

    # Check to see if the list is populated
    if parse_uri:
        print(t.yellow("[{0}] Found parseUri() implementation! ...".format(datetime.datetime.now())))
        for location in parse_uri:
            analysis.show_Path(apks, location)

    print(t.yellow("[{0}] Searching for loadUrl...".format(datetime.datetime.now())))
    load_url = dx.get_tainted_packages().search_methods("Landroid/webkit/WebView", methods["load"], ".")

    # Check to see if the list is populated
    if load_url:
        print(t.yellow("[{0}] Found loadUrl() implementation! ...".format(datetime.datetime.now())))
        for location in load_url:
            analysis.show_Path(apks, location)

    print(t.yellow("[{0}] Searching for addJavascriptInterface() ...".format(datetime.datetime.now())))
    add_js = dx.get_tainted_packages().search_methods(".", methods["js"], ".")

    # Check to see if the list is populated
    if add_js:
        print(t.yellow("[{0}] Found addJavascriptInterface() implementation! ...".format(datetime.datetime.now())))
        for location in load_url:
            analysis.show_Path(apks, location)


def main(apk):

    """
    Handle APK analysis
    """

    try:
        # Perform analysis on target APK
        print(t.yellow("[{0}] Performing analysis ...".format(datetime.datetime.now())))
        a, apks, dx = APK(apk), AndroguardS(apk), analysis.uVMAnalysis(DVM.DalvikVMFormat(APK(apk).get_dex()))

        # Validate the returned objects
        if a and apks and dx:
            print(t.yellow("[{0}] Analysis successful!".format(datetime.datetime.now())))
            # Call search function
            search(apks, dx)
        else:
            print(t.yellow("[{0}] Analysis failed!".format(datetime.datetime.now())))
    except zipfile.BadZipfile:
        print(t.yellow("[{0}] Bad APK file!".format(datetime.datetime.now())))


if __name__ == '__main__':

    # import argparse
    import argparse

    # Create argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--apk', dest='apk', help='Target APK')
    args = parser.parse_args()

    if args.apk:
        try:
            # Call main function
            main(args.apk)
        except KeyboardInterrupt:
            print(t.yellow("[{0}] Shutting down ...".format(datetime.datetime.now())))


