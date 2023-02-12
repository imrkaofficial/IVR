from flask import Flask, request, url_for
from tiniyo.voice_response import VoiceResponse
from xmlhelp import tiniyoml
from config import *
from tiniyo.rest import Client

app = Flask(__name__)


@app.route('/ivr/tiniyo', methods=['GET', 'POST'])
def lan():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('menu1', _scheme='http', _external=True), method="POST"
    )as g:
        g.say(message="Welcome to Tiniyo Customer Care." +
                      "Press 1 for English." +
                      "Press 2 for French." +
                      "Press 3 for Spanish."
                      "To repeat Press 0.", loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu', methods=['POST'])
def menu1():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_lan_eng",
                      '2': "_lan_french",
                      '3': "_lan_spanish",
                      '0': "_repeat0"}

    if int(selected_options) == 1:
        response = welcome()
        return response
    elif int(selected_options) == 2:
        response = welcome_2()
        return response
    elif int(selected_options) == 3:
        response = welcome_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat0()
        return response
    else:
        return _redirect_welcome()


def _repeat0():
    response = VoiceResponse()
    response.redirect(url_for('lan', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/welcome', methods=['GET', 'POST'])
def welcome():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('menu', _scheme='http', _external=True), method="POST"
    )as g:
        g.say(message="Our menu have changed. Please listen carefully." +
                      "Press 1 for Special call rates and full time offers." +
                      "Press 2 for Hellotunes and other Values Added services." +
                      "Press 3 to Know your mobile Balance and Validity, Reason for Balance Deduction." +
                      "Press 4 for Tiniyo Money." +
                      "Press 5 for information on Data services like 3G,4G, Mobile internet, Dongle." +
                      "Press 6 for any question on MNP, DTH, Postpaid and telephone bills." +
                      "To repeat Press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/menu', methods=['POST'])
def menu():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_special_offers",
                      '2': "_hello_tunes",
                      '3': "_balance",
                      '4': "_tiniyo_money",
                      '5': "_data_services",
                      '6': "_any_question",
                      '0': "_repeat1"}

    if int(selected_options) == 1:
        response = _special_offers()
        return response
    elif int(selected_options) == 2:
        response = _hello_tunes()
        return response
    elif int(selected_options) == 3:
        response = _balance()
        return response
    elif int(selected_options) == 4:
        response = _tiniyo_money()
        return response
    elif int(selected_options) == 5:
        response = _data_services()
        return response
    elif int(selected_options) == 6:
        response = _any_question()
        return response
    elif int(selected_options) == 0:
        response = _repeat1()
        return response
    else:
        return _redirect_welcome()


# methods
def _redirect_welcome():
    response = VoiceResponse()
    response.say("You enter incorrect key. Call back again." +
                 "Thank you for calling.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option1', methods=['GET', 'POST'])
def _special_offers():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('_specialoffers', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Specialized  offer for you." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option2', methods=['GET', 'POST'])
def _hello_tunes():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_a', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for Hello Tune." +
              "Press 2 to start any other values added services." +
              "Press 3 to stop Value added services." +
              "Press 4 for receive  a text on how to start/stop a VAS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option3', methods=['GET', 'POST'])
def _balance():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_f', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 To know your mobile balance & Validity." +
              "Press 2 for details Balance deduction." +
              "Press 3 for information on special 5." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option4', methods=['GET', 'POST'])
def _tiniyo_money():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_n', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for information of tiniyo money." +
              "Press 2 If you are an tiniyo customer." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5', methods=['GET', 'POST'])
def _data_services():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_u', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 to start 3G." +
              "Press 2 to stop 3G." +
              "Press 3 to get setting of 3G." +
              "Press 4 for information of data card or dongle details." +
              "Press 5 for information on Pc connectivity procedure." +
              "Press 6 for question and technical help." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6', methods=['GET', 'POST'])
def _any_question():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ii', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for Roaming." +
              "Press 2 for question related to postpaid." +
              "Press 3 for change language." +
              "Press 4 for MNP." +
              "Press 5 for question related to fixed line." +
              "Press 6 for any question."
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


def _repeat1():
    response = VoiceResponse()
    response.redirect(url_for('welcome', _scheme='http', _external=True))
    return tiniyoml(response)


# options1specialoffers
@app.route('/ivr/lan_menu1/option1/option1', methods=['POST'])
def _specialoffers():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu1",
                      '8': "_main_menu1",
                      '0': "_repeat2"}

    if int(selected_options) == 7:
        response = _prev_menu1()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 0:
        response = _repeat2()
        return response
    else:
        return _redirect_welcome()


def _prev_menu1():
    response = VoiceResponse()
    response.redirect(url_for('welcome', _scheme='http', _external=True))
    return tiniyoml(response)


def _main_menu1():
    response = VoiceResponse()
    response.redirect(url_for('welcome', _scheme='http', _external=True))
    return tiniyoml(response)


def _repeat2():
    response = VoiceResponse()
    response.redirect(url_for('_special_offers', _scheme='http', _external=True))
    return tiniyoml(response)


# option2hellotunes

@app.route('/ivr/lan_menu1/hello_a', methods=['POST'])
def hello_a():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_hello_tun",
                      '2': "_start_value",
                      '3': "_stop_value",
                      '4': "_ss_vas",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat3"}

    if int(selected_options) == 1:
        response = _hello_tun()
        return response
    elif int(selected_options) == 2:
        response = _start_value()
        return response
    elif int(selected_options) == 3:
        response = _stop_value()
        return response
    elif int(selected_options) == 4:
        response = _ss_vas()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat3()
        return response
    else:
        return _redirect_welcome()


def _repeat3():
    response = VoiceResponse()
    response.redirect(url_for('_hello_tunes', _scheme='http', _external=True))
    return tiniyoml(response)


def _call_to_ex():
    response = VoiceResponse()
    response.say("We are transferring your call to Customer Executive." +
                 "Please wait!!! Our Executive are busy on other line", voice=female, language=uk)
    response.dial(number=executive_number, caller_id=cidin)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option2/option1', methods=['GET', 'POST'])
def _hello_tun():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_b', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 to start Hello tunes." +
              "Press 2 to stop hello tunes." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_b', methods=['POST'])
def hello_b():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_start_hello",
                      '2': "_stop_hello",
                      '7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat4"}

    if int(selected_options) == 1:
        response = _start_hello()
        return response
    elif int(selected_options) == 2:
        response = _stop_hello()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat4()
        return response
    else:
        return _redirect_welcome()


@app.route('/ivr/lan_menu1/option2/option1/option1', methods=['GET', 'POST'])
def _start_hello():
    response = VoiceResponse()
    response.say("Your Hello tune successfully activated." +
                 "Thank you for calling.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option2/option1/option2', methods=['GET', 'POST'])
def _stop_hello():
    response = VoiceResponse()
    response.say("Your activated Hello tune successfully deactivated." +
                 "Thank you for calling.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


def _prev_menu2():
    response = VoiceResponse()
    response.redirect(url_for('_hello_tunes', _scheme='http', _external=True))
    return tiniyoml(response)


def _repeat4():
    response = VoiceResponse()
    response.redirect(url_for('_hello_tun', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option2/option2', methods=['GET', 'POST'])
def _start_value():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_c', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for Astrology on demand." +
              "Press 2 for Tiniyo Talkies." +
              "Press 3 for Missed Call Aleart." +
              "Press 4 for Job Aleart." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_c', methods=['POST'])
def hello_c():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_astro_hello",
                      '2': "_talkies_hello",
                      '3': "_missed_hello",
                      '4': "_job_hello",
                      '7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat5"}

    if int(selected_options) == 1:
        response = _astro_hello()
        return response
    elif int(selected_options) == 2:
        response = _talkies_hello()
        return response
    elif int(selected_options) == 3:
        response = _missed_hello()
        return response
    elif int(selected_options) == 4:
        response = _job_hello()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat5()
        return response
    else:
        return _redirect_welcome()


@app.route('/ivr/lan_menu1/option2/option2/option1', methods=['GET', 'POST'])
def _astro_hello():
    response = VoiceResponse()
    response.say("Your services is successfully activated." +
                 "Thank you for calling.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option2/option2/option2', methods=['GET', 'POST'])
def _talkies_hello():
    response = VoiceResponse()
    response.say("Your services is successfully activated." +
                 "Thank you for calling.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option2/option2/option3', methods=['GET', 'POST'])
def _missed_hello():
    response = VoiceResponse()
    response.say("Your services is successfully activated." +
                 "Thank you for calling.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option2/option2/option4', methods=['GET', 'POST'])
def _job_hello():
    response = VoiceResponse()
    response.say("Your services is successfully activated." +
                 "Thank you for calling.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


def _repeat5():
    response = VoiceResponse()
    response.redirect(url_for('_start_value', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option2/option3', methods=['GET', 'POST'])
def _stop_value():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_d', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("No Value Added services has been started on your numbers." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_d', methods=['POST'])
def hello_d():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat6"}

    if int(selected_options) == 7:
        response = _prev_menu2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat6()
        return response
    else:
        return _redirect_welcome()


def _repeat6():
    response = VoiceResponse()
    response.redirect(url_for('_stop_value', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option2/option4', methods=['GET', 'POST'])
def _ss_vas():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_e', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Thank you detail will be shared with you soon via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_e', methods=['POST'])
def hello_e():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat7"}

    if int(selected_options) == 7:
        response = _prev_menu2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat7()
        return response
    else:
        return _redirect_welcome()


def _repeat7():
    response = VoiceResponse()
    response.redirect(url_for('_ss_vas', _scheme='http', _external=True))
    return tiniyoml(response)


# option3
@app.route('/ivr/lan_menu1/hello_f', methods=['POST'])
def hello_f():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_balance_val",
                      '2': "_balance_ded",
                      '3': "_special_five",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat8"}

    if int(selected_options) == 1:
        response = _balance_val()
        return response
    elif int(selected_options) == 2:
        response = _balance_ded()
        return response
    elif int(selected_options) == 3:
        response = _special_five()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat8()
        return response
    else:
        return _redirect_welcome()


def _repeat8():
    response = VoiceResponse()
    response.redirect(url_for('_balance', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option3/option1', methods=['GET', 'POST'])
def _balance_val():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_g', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your Balance and Validity information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_g', methods=['POST'])
def hello_g():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu3",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat9"}

    if int(selected_options) == 7:
        response = _prev_menu3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat9()
        return response
    else:
        return _redirect_welcome()


def _repeat9():
    response = VoiceResponse()
    response.redirect(url_for('_balance_val', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu3():
    response = VoiceResponse()
    response.redirect(url_for('_balance', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option3/option2', methods=['GET', 'POST'])
def _balance_ded():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_h', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your Balance and Validity information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_h', methods=['POST'])
def hello_h():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu3",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat10"}

    if int(selected_options) == 7:
        response = _prev_menu3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat10()
        return response
    else:
        return _redirect_welcome()


def _repeat10():
    response = VoiceResponse()
    response.redirect(url_for('_balance_ded', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option3/option3', methods=['GET', 'POST'])
def _special_five():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_i', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for Last 5 vas Debits." +
              "Press 2 for last 5 voice call debits." +
              "Press 3 for Last 5 outgoing sms/mms debits." +
              "Press 4 for last 5 internet usage details." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_i', methods=['POST'])
def hello_i():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_debit_five",
                      '2': "_debit_voice",
                      '3': "_debit_sms",
                      '4': "_debit_internet",
                      '7': "_prev_menu3",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat11"}

    if int(selected_options) == 1:
        response = _debit_five()
        return response
    elif int(selected_options) == 2:
        response = _debit_voice()
        return response
    elif int(selected_options) == 3:
        response = _debit_sms()
        return response
    elif int(selected_options) == 4:
        response = _debit_internet()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat11()
        return response
    else:
        return _redirect_welcome()


def _repeat11():
    response = VoiceResponse()
    response.redirect(url_for('_special_five', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option3/option3/option1', methods=['GET', 'POST'])
def _debit_five():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_j', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your last five debit information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_j', methods=['POST'])
def hello_j():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat12"}

    if int(selected_options) == 7:
        response = _prev_menu4()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat12()
        return response
    else:
        return _redirect_welcome()


def _repeat12():
    response = VoiceResponse()
    response.redirect(url_for('_debit_five', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu4():
    response = VoiceResponse()
    response.redirect(url_for('_special_five', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option3/option3/option2', methods=['GET', 'POST'])
def _debit_voice():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_k', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your last five Voice call debit information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_k', methods=['POST'])
def hello_k():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat13"}

    if int(selected_options) == 7:
        response = _prev_menu4()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat13()
        return response
    else:
        return _redirect_welcome()


def _repeat13():
    response = VoiceResponse()
    response.redirect(url_for('_debit_voice', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option3/option3/option3', methods=['GET', 'POST'])
def _debit_sms():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_l', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your last five debit SMS/MMS information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_l', methods=['POST'])
def hello_l():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat14"}

    if int(selected_options) == 7:
        response = _prev_menu4()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat14()
        return response
    else:
        return _redirect_welcome()


def _repeat14():
    response = VoiceResponse()
    response.redirect(url_for('_debit_sms', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option3/option3/option4', methods=['GET', 'POST'])
def _debit_internet():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_m', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your last five debit internet information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_m', methods=['POST'])
def hello_m():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat15"}

    if int(selected_options) == 7:
        response = _prev_menu4()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat15()
        return response
    else:
        return _redirect_welcome()


def _repeat15():
    response = VoiceResponse()
    response.redirect(url_for('_debit_internet', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_n', methods=['POST'])
def hello_n():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_info_money",
                      '2': "_info_customer",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat16"}

    if int(selected_options) == 1:
        response = _info_money()
        return response
    elif int(selected_options) == 2:
        response = _info_customer()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat16()
        return response
    else:
        return _redirect_welcome()


def _repeat16():
    response = VoiceResponse()
    response.redirect(url_for('_tiniyo_money', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option4/option1', methods=['GET', 'POST'])
def _info_money():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_0', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for Tiniyo money." +
              "Press 2 for information on how to become tiniyo customer." +
              "Press 3 to know about tiniyo money offers." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_o', methods=['POST'])
def hello_0():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_info_tm",
                      '2': "_info_tc",
                      '3': "_info_offers",
                      '7': "_prev_menu5",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat17"}

    if int(selected_options) == 1:
        response = _info_tm()
        return response
    elif int(selected_options) == 2:
        response = _info_tc()
        return response
    elif int(selected_options) == 3:
        response = _info_offers()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu5()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat17()
        return response
    else:
        return _redirect_welcome()


def _repeat17():
    response = VoiceResponse()
    response.redirect(url_for('_info_money', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu5():
    response = VoiceResponse()
    response.redirect(url_for('_tiniyo_money', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option4/option1/option1', methods=['GET', 'POST'])
def _info_tm():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_p', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Tiniyo information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_p', methods=['POST'])
def hello_p():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu6",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat18"}

    if int(selected_options) == 7:
        response = _prev_menu6()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat18()
        return response
    else:
        return _redirect_welcome()


def _repeat18():
    response = VoiceResponse()
    response.redirect(url_for('_info_tm', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu6():
    response = VoiceResponse()
    response.redirect(url_for('_info_money', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option4/option1/option2', methods=['GET', 'POST'])
def _info_tc():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_q', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Thank you. You have become a tiniyo customer." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_q', methods=['POST'])
def hello_q():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu6",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat19"}

    if int(selected_options) == 7:
        response = _prev_menu6()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat19()
        return response
    else:
        return _redirect_welcome()


def _repeat19():
    response = VoiceResponse()
    response.redirect(url_for('_info_tc', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option4/option1/option3', methods=['GET', 'POST'])
def _info_offers():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_r', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("To know about tiniyo money offers information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_r', methods=['POST'])
def hello_r():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu6",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat20"}

    if int(selected_options) == 7:
        response = _prev_menu6()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat20()
        return response
    else:
        return _redirect_welcome()


def _repeat20():
    response = VoiceResponse()
    response.redirect(url_for('_info_offers', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option4/option2', methods=['GET', 'POST'])
def _info_customer():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_s', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 if you know your MPIN." +
              "Press 2 for if you don't have MPIN." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_s', methods=['POST'])
def hello_s():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_your_mpin",
                      '2': "_not_mpin",
                      '7': "_prev_menu5",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat21"}

    if int(selected_options) == 1:
        response = _your_mpin()
        return response
    elif int(selected_options) == 2:
        response = _not_mpin()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu5()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat21()
        return response
    else:
        return _redirect_welcome()


def _repeat21():
    response = VoiceResponse()
    response.redirect(url_for('_info_customer', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option4/option2/option1', methods=['GET', 'POST'])
def _your_mpin():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_t', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 to Enter your MPIN." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_t', methods=['POST'])
def hello_t():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_mpin_no",
                      '7': "_prev_menu5",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat21"}

    if int(selected_options) == 1:
        response = _mpin_no()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu5()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat21()
        return response
    else:
        return _redirect_welcome()


@app.route('/ivr/lan_menu1/option4/option2/op1', methods=['GET', 'POST'])
def _mpin_no():
    response = VoiceResponse()
    response.say("You enter incorrect MPIN. Thank you for calling." +
                 "Call back again later.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option4/option2/option2', methods=['GET', 'POST'])
def _not_mpin():
    response = VoiceResponse()
    response.say("We are transferring your call to Customer Executive" +
                 "Please wait!!! Our Executives are busy on other lines.", voice=female, language=uk)
    response.dial(number=executive_number, caller_id=cidin)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_u', methods=['POST'])
def hello_u():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_start_3g",
                      '2': "_stop_3g",
                      '3': "_setting_3g",
                      '4': "_info_dt",
                      '5': "_info_pc",
                      '6': "_ques_3g",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat22"}

    if int(selected_options) == 1:
        response = _start_3g()
        return response
    elif int(selected_options) == 2:
        response = _stop_3g()
        return response
    elif int(selected_options) == 3:
        response = _setting_3g()
        return response
    elif int(selected_options) == 4:
        response = _info_dt()
        return response
    elif int(selected_options) == 5:
        response = _info_pc()
        return response
    elif int(selected_options) == 6:
        response = _ques_3g()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat22()
        return response
    else:
        return _redirect_welcome()


def _repeat22():
    response = VoiceResponse()
    response.redirect(url_for('_data_services', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option1', methods=['GET', 'POST'])
def _start_3g():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_v', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 to start 3G service." +
              "Press 2 to start internet service." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/lan_menu1/ivr/hello_v', methods=['POST'])
def hello_v():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_starts_3g",
                      '2': "_starts_internet",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat23"}

    if int(selected_options) == 1:
        response = _starts_3g()
        return response
    elif int(selected_options) == 2:
        response = _starts_internet()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat23()
        return response
    else:
        return _redirect_welcome()


def _repeat23():
    response = VoiceResponse()
    response.redirect(url_for('_start_3g', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu7():
    response = VoiceResponse()
    response.redirect(url_for('_data_services', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option1/option1', methods=['GET', 'POST'])
def _starts_3g():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_w', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your service information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_w', methods=['POST'])
def hello_w():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu8",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat24"}

    if int(selected_options) == 7:
        response = _prev_menu8()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat24()
        return response
    else:
        return _redirect_welcome()


def _repeat24():
    response = VoiceResponse()
    response.redirect(url_for('_starts_3g', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu8():
    response = VoiceResponse()
    response.redirect(url_for('_start_3g', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option1/option2', methods=['GET', 'POST'])
def _starts_internet():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_x', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your internet service information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_x', methods=['POST'])
def hello_x():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu8",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat25"}

    if int(selected_options) == 7:
        response = _prev_menu8()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat25()
        return response
    else:
        return _redirect_welcome()


def _repeat25():
    response = VoiceResponse()
    response.redirect(url_for('_starts_internet', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option2', methods=['GET', 'POST'])
def _stop_3g():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_y', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 to stop 3G service." +
              "Press 2 to stop internet service." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_y', methods=['GET', 'POST'])
def hello_y():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_stops_3g",
                      '2': "_stops_internet",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat26"}

    if int(selected_options) == 1:
        response = _stops_3g()
        return response
    elif int(selected_options) == 2:
        response = _stops_internet()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat26()
        return response
    else:
        return _redirect_welcome()


def _repeat26():
    response = VoiceResponse()
    response.redirect(url_for('_stop_3g', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option2/option1', methods=['GET', 'POST'])
def _stops_3g():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_z', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your service information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_z', methods=['POST'])
def hello_z():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu9",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat27"}

    if int(selected_options) == 7:
        response = _prev_menu9()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat27()
        return response
    else:
        return _redirect_welcome()


def _repeat27():
    response = VoiceResponse()
    response.redirect(url_for('_stops_3g', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu9():
    response = VoiceResponse()
    response.redirect(url_for('_stop_3g', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option2/option2', methods=['GET', 'POST'])
def _stops_internet():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_aa', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your internet service information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_aa', methods=['POST'])
def hello_aa():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu9",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat28"}

    if int(selected_options) == 7:
        response = _prev_menu9()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat28()
        return response
    else:
        return _redirect_welcome()


def _repeat28():
    response = VoiceResponse()
    response.redirect(url_for('_stops_internet', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option3', methods=['GET', 'POST'])
def _setting_3g():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_bb', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 to get setting for internet services." +
              "Press 2 to get setting for MMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_bb', methods=['POST'])
def hello_bb():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_setting_internet",
                      '2': "_setting_mms",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat29"}

    if int(selected_options) == 1:
        response = _setting_internet()
        return response
    elif int(selected_options) == 2:
        response = _setting_mms()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat29()
        return response
    else:
        return _redirect_welcome()


def _repeat29():
    response = VoiceResponse()
    response.redirect(url_for('_setting_3g', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option3/option1', methods=['GET', 'POST'])
def _setting_internet():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_cc', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Internet setting to get via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_cc', methods=['POST'])
def hello_cc():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu10",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat30"}

    if int(selected_options) == 7:
        response = _prev_menu10()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat30()
        return response
    else:
        return _redirect_welcome()


def _repeat30():
    response = VoiceResponse()
    response.redirect(url_for('_setting_internet', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu10():
    response = VoiceResponse()
    response.redirect(url_for('_setting_3g', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option3/option2', methods=['GET', 'POST'])
def _setting_mms():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_dd', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("MMS setting to get via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_dd', methods=['POST'])
def hello_dd():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu10",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat31"}

    if int(selected_options) == 7:
        response = _prev_menu10()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat31()
        return response
    else:
        return _redirect_welcome()


def _repeat31():
    response = VoiceResponse()
    response.redirect(url_for('_setting_mms', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option4', methods=['GET', 'POST'])
def _info_dt():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ee', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for information of installing procedure." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_ee', methods=['POST'])
def hello_ee():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_inf_install",
                      '2': "_setting_mms",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat32"}

    if int(selected_options) == 1:
        response = _inf_install()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat32()
        return response
    else:
        return _redirect_welcome()


def _repeat32():
    response = VoiceResponse()
    response.redirect(url_for('_info_dt', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option4/option1', methods=['GET', 'POST'])
def _inf_install():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ff', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("For information on how to install Data card or Dongle with." +
              "Press 1 for Windows Operating System." +
              "Press 2 for Linux Operating System." +
              "Press 3 for Mac book"
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_ff', methods=['POST'])
def hello_ff():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_system_os",
                      '2': "_system_linux",
                      '3': "_system_mac",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat33"}

    if int(selected_options) == 1:
        response = _system_os()
        return response
    elif int(selected_options) == 2:
        response = _system_linux()
        return response
    elif int(selected_options) == 3:
        response = _system_mac()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat33()
        return response
    else:
        return _redirect_welcome()


def _repeat33():
    response = VoiceResponse()
    response.redirect(url_for('_inf_install', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option4/option1_op1', methods=['GET', 'POST'])
def _system_os():
    response = VoiceResponse()
    response.say("Our executives are busy on other lines." +
                 "We will call back soon.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option4/option1_op2', methods=['GET', 'POST'])
def _system_linux():
    response = VoiceResponse()
    response.say("Our executives are busy on other lines." +
                 "We will call back soon.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option4/option1_op3', methods=['GET', 'POST'])
def _system_mac():
    response = VoiceResponse()
    response.say("Our executives are busy on other lines." +
                 "We will call back soon.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option5', methods=['GET', 'POST'])
def _info_pc():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_gg', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("For information how to connect." +
              "Press 1 for PC through bluetooth." +
              "Press 2 for PC through infrared." +
              "Press 3 for PC through Cable." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_gg', methods=['GET', 'POST'])
def hello_gg():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_bluetooth_pc",
                      '2': "_infrared_pc",
                      '3': "_cable_pc",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat34"}

    if int(selected_options) == 1:
        response = _bluetooth_pc()
        return response
    elif int(selected_options) == 2:
        response = _infrared_pc()
        return response
    elif int(selected_options) == 3:
        response = _cable_pc()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat34()
        return response
    else:
        return _redirect_welcome()


def _repeat34():
    response = VoiceResponse()
    response.redirect(url_for('_info_pc', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option5/option1', methods=['GET', 'POST'])
def _bluetooth_pc():
    response = VoiceResponse()
    response.say("Our executives are busy on other lines." +
                 "Please wait!!!", voice=female, language=uk)
    response.dial(number=executive_number, caller_id=cidin)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option5/option2', methods=['GET', 'POST'])
def _infrared_pc():
    response = VoiceResponse()
    response.say("Our executives are busy on other lines." +
                 "Please Wait!!!", voice=female, language=uk)
    response.dial(number=executive_number, caller_id=cidin)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option5/option3', methods=['GET', 'POST'])
def _cable_pc():
    response = VoiceResponse()
    response.say("Our executives are busy on other lines." +
                 "Please Wait!!!", voice=female, language=uk)
    response.dial(number=executive_number, caller_id=cidin)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option6', methods=['GET', 'POST'])
def _ques_3g():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_hh', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for any question." +
              "Press 2 for technical help." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_hh', methods=['POST'])
def hello_hh():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_ques_any",
                      '2': "_technical_help",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat35"}

    if int(selected_options) == 1:
        response = _ques_any()
        return response
    elif int(selected_options) == 2:
        response = _technical_help()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat35()
        return response
    else:
        return _redirect_welcome()


def _repeat35():
    response = VoiceResponse()
    response.redirect(url_for('_ques_3g', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option6/option1', methods=['GET', 'POST'])
def _ques_any():
    response = VoiceResponse()
    response.say("Our executives are busy on other lines." +
                 "Please Wait!!!" +
                 "Call again later.", voice=female, language=uk)
    response.dial(number=executive_number, caller_id=cidin)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option5/option6/option2', methods=['GET', 'POST'])
def _technical_help():
    response = VoiceResponse()
    response.say("Our tech teams are busy on other lines." +
                 "Please Wait!!!" +
                 "Call again later.", voice=female, language=uk)
    response.dial(number=technician_number, caller_id=cidin)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_ii', methods=['POST'])
def hello_ii():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_Roaming",
                      '2': "_postpaid",
                      '3': "_change",
                      '4': "_for_mnp",
                      '5': "_ques_fix",
                      '6': "_ques_any",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat36"}

    if int(selected_options) == 1:
        response = _Roaming()
        return response
    elif int(selected_options) == 2:
        response = _postpaid()
        return response
    elif int(selected_options) == 3:
        response = _change()
        return response
    elif int(selected_options) == 4:
        response = _for_mnp()
        return response
    elif int(selected_options) == 5:
        response = _ques_fix()
        return response
    elif int(selected_options) == 6:
        response = _ques_any()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat36()
        return response
    else:
        return _redirect_welcome()


def _repeat36():
    response = VoiceResponse()
    response.redirect(url_for('_any_question', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option1', methods=['GET', 'POST'])
def _Roaming():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_jj', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for National Roaming." +
              "Press 2 for information of international roaming." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_jj', methods=['GET', 'POST'])
def hello_jj():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_national_roaming",
                      '2': "_international_roaming",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat37"}

    if int(selected_options) == 1:
        response = _national_roaming()
        return response
    elif int(selected_options) == 2:
        response = _international_roaming()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat37()
        return response
    else:
        return _redirect_welcome()


def _repeat37():
    response = VoiceResponse()
    response.redirect(url_for('_Roaming', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu11():
    response = VoiceResponse()
    response.redirect(url_for('_any_question', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option1/option1', methods=['GET', 'POST'])
def _national_roaming():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ll', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your national roaming information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_ll', methods=['POST'])
def hello_ll():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu12",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat38"}

    if int(selected_options) == 7:
        response = _prev_menu12()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat38()
        return response
    else:
        return _redirect_welcome()


def _repeat38():
    response = VoiceResponse()
    response.redirect(url_for('_national_roaming', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu12():
    response = VoiceResponse()
    response.redirect(url_for('_Roaming', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option1/option2', methods=['GET', 'POST'])
def _international_roaming():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_kk', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your international roaming information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_kk', methods=['POST'])
def hello_kk():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu12",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat39"}

    if int(selected_options) == 7:
        response = _prev_menu12()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat39()
        return response
    else:
        return _redirect_welcome()


def _repeat39():
    response = VoiceResponse()
    response.redirect(url_for('_international_roaming', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option2', methods=['GET', 'POST'])
def _postpaid():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_mm', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for question related to postpaid." +
              "Press 2 for for question related to prepaid to postpaid." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_mm', methods=['POST'])
def hello_mm():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_question_postpaid",
                      '2': "_prepaid_postpaid",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat40"}

    if int(selected_options) == 1:
        response = _question_postpaid()
        return response
    elif int(selected_options) == 2:
        response = _prepaid_postpaid()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat40()
        return response
    else:
        return _redirect_welcome()


def _repeat40():
    response = VoiceResponse()
    response.redirect(url_for('_postpaid', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option2/option1', methods=['GET', 'POST'])
def _question_postpaid():
    response = VoiceResponse()
    response.say("We are transferring your call to Customer Executive." +
                 "Please wait!!! Our Executives are busy on other lines.", voice=female, language=uk)
    response.dial(number=executive_number, caller_id=cidin)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option2/option2', methods=['GET', 'POST'])
def _prepaid_postpaid():
    response = VoiceResponse()
    response.say("We are transferring your call to Customer Executive." +
                 "Please wait!!! Our Executives are busy on other lines.", voice=female, language=uk)
    response.dial(number=executive_number, caller_id=cidin)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option3', methods=['GET', 'POST'])
def _change():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_nn', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 to change your language." +
              "Press 2 to change TPIN." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_nn', methods=['POST'])
def hello_nn():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_change_language",
                      '2': "_change_tpin",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat41"}

    if int(selected_options) == 1:
        response = _change_language()
        return response
    elif int(selected_options) == 2:
        response = _change_tpin()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat41()
        return response
    else:
        return _redirect_welcome()


def _repeat41():
    response = VoiceResponse()
    response.redirect(url_for('_change', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option3/option1', methods=['GET', 'POST'])
def _change_language():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_oo', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Select your language." +
              "Press 1 for French." +
              "Press 2 for Spanish." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_oo', methods=['POST'])
def hello_oo():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_lan_fr",
                      '2': "_lan_spanish",
                      '7': "_prev_menu13",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat42"}

    if int(selected_options) == 1:
        response = _lan_fr_1()
        return response
    elif int(selected_options) == 2:
        response = _lan_spanish_1()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu13()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat42()
        return response
    else:
        return _redirect_welcome()


def _repeat42():
    response = VoiceResponse()
    response.redirect(url_for('_change_language', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu13():
    response = VoiceResponse()
    response.redirect(url_for('_change', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option3/option1_op1', methods=['GET', 'POST'])
def _lan_fr_1():
    response = VoiceResponse()
    response.say("Langue française mise à jour avec succès." +
                 "Merci de votre appel.", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option3/option1_op2', methods=['GET', 'POST'])
def _lan_spanish_1():
    response = VoiceResponse()
    response.say("Idioma español actualizado con éxito." +
                 "Gracias por llamar.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option3/option2', methods=['GET', 'POST'])
def _change_tpin():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_pp', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for Enter your TPIN." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_pp', methods=['POST'])
def hello_pp():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_enter_tpin",
                      '7': "_prev_menu12",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat43"}

    if int(selected_options) == 1:
        response = _enter_tpin()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu13()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat43()
        return response
    else:
        return _redirect_welcome()


def _repeat43():
    response = VoiceResponse()
    response.redirect(url_for('_change_tpin', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option3/option2_op1', methods=['GET', 'POST'])
def _enter_tpin():
    response = VoiceResponse()
    with response.gather(
            num_digits=4, action=url_for('hello_qq', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Enter your TPIN." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_qq', methods=['POST'])
def hello_qq():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu13",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat43"}

    if int(selected_options) == 7:
        response = _prev_menu13()
        return response
    elif int(selected_options) == 2580:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 1472:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat43()
        return response
    else:
        return _redirect_welcome()


@app.route('/ivr/lan_menu1/option6/option4', methods=['GET', 'POST'])
def _for_mnp():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_rr', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for MNP information." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_rr', methods=['POST'])
def hello_rr():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_info_mnp",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat44"}

    if int(selected_options) == 1:
        response = _info_mnp()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat44()
        return response
    else:
        return _redirect_welcome()


def _repeat44():
    response = VoiceResponse()
    response.redirect(url_for('_for_mnp', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option4/option1', methods=['GET', 'POST'])
def _info_mnp():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ss', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your MNP information to get this information via SMS." +
              "To go back to previous menu press 7." +
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_ss', methods=['POST'])
def hello_ss():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu14",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat45"}

    if int(selected_options) == 7:
        response = _prev_menu14()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat45()
        return response
    else:
        return _redirect_welcome()


def _repeat45():
    response = VoiceResponse()
    response.redirect(url_for('_info_mnp', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu14():
    response = VoiceResponse()
    response.redirect(url_for('_for_mnp', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option5', methods=['GET', 'POST'])
def _ques_fix():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_tt', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Press 1 for Tiniyo fixed line service." +
              "Press 2 for Tiniyo digital TV service." +
              "To go back to previous menu press 7."
              "To go back to main menu press 8." +
              "To Tiniyo Executive press 9." +
              "To repeat press 0.", voice=male, language=uk, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/hello_tt', methods=['POST'])
def hello_tt():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_line_fixed",
                      '2': "_digital_tv",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat46"}

    if int(selected_options) == 1:
        response = _line_fixed()
        return response
    elif int(selected_options) == 2:
        response = _digital_tv()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex()
        return response
    elif int(selected_options) == 0:
        response = _repeat46()
        return response
    else:
        return _redirect_welcome()


def _repeat46():
    response = VoiceResponse()
    response.redirect(url_for('_ques_fix', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option5/option1', methods=['GET', 'POST'])
def _line_fixed():
    response = VoiceResponse()
    response.say("Tiniyo fixed line services information to get via SMS." +
                 "Thank you for calling.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu1/option6/option5/option2', methods=['GET', 'POST'])
def _digital_tv():
    response = VoiceResponse()
    response.say("Tiniyo Digital tv information to get via SMS." +
                 "Thank you for calling.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/welcome', methods=['GET', 'POST'])
def welcome_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('menu_2', _scheme='http', _external=True), method="POST"
    )as g:
        g.say(message="Notre menu a changé. Veuillez écouter attentivement." +
                      "Appuyez sur le 1 pour les tarifs d'appels spéciaux et les offres à temps plein." +
                      "Appuyez sur 2 pour Hellotunes et d'autres services à valeur ajoutée." +
                      "Appuyez sur 3 pour connaître votre solde mobile et sa validité, motif de la déduction du solde." +
                      "Appuyez sur 4 pour l'argent Tiniyo." +
                      "Appuyez sur 5 pour obtenir des informations sur les services de données tels que 3G, 4G, Internet mobile, Dongle." +
                      "Appuyez sur le 6 pour toute question sur les factures MNP, DTH, Postpaid et de téléphone." +
                      "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/menu', methods=['POST'])
def menu_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_special_offers",
                      '2': "_hello_tunes",
                      '3': "_balance",
                      '4': "_tiniyo_money",
                      '5': "_data_services",
                      '6': "_any_question",
                      '0': "_repeat1"}

    if int(selected_options) == 1:
        response = _special_offers_2()
        return response
    elif int(selected_options) == 2:
        response = _hello_tunes_2()
        return response
    elif int(selected_options) == 3:
        response = _balance_2()
        return response
    elif int(selected_options) == 4:
        response = _tiniyo_money_2()
        return response
    elif int(selected_options) == 5:
        response = _data_services_2()
        return response
    elif int(selected_options) == 6:
        response = _any_question_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat1_2()
        return response
    else:
        return _redirect_welcome_2()


# methods
def _redirect_welcome_2():
    response = VoiceResponse()
    response.say("Vous entrez une clé incorrecte. Appelle encore une fois. "+
                 "Merci de votre appel", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option1', methods=['GET', 'POST'])
def _special_offers_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('_specialoffers_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Offre spéciale pour vous." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option2', methods=['GET', 'POST'])
def _hello_tunes_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_a_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour Hello Tune." +
              "Appuyez sur 2 pour démarrer tout autre service à valeur ajoutée." +
              "Appuyez sur 3 pour arrêter les services à valeur ajoutée." +
              "Appuyez sur 4 pour recevoir un SMS sur la façon de démarrer/arrêter un VAS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option3', methods=['GET', 'POST'])
def _balance_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_f_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 Pour connaître votre solde mobile & Validité." +
              "Appuyez sur 2 pour plus de détails Déduction du solde." +
              "Appuyez sur 3 pour obtenir des informations sur le spécial 5." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option4', methods=['GET', 'POST'])
def _tiniyo_money_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_n_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour obtenir des informations sur l'argent tiniyo." +
              "Appuyez sur 2 si vous êtes un client Tiniyo." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5', methods=['GET', 'POST'])
def _data_services_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_u_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour démarrer la 3G." +
              "Appuyez sur 2 pour arrêter la 3G." +
              "Appuyez sur 3 pour obtenir le réglage de la 3G." +
              "Appuyez sur 4 pour obtenir des informations sur les détails de la carte de données ou du dongle." +
              "Appuyez sur 5 pour obtenir des informations sur la procédure de connectivité PC." +
              "Appuyez sur 6 pour la question et l'aide technique." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6', methods=['GET', 'POST'])
def _any_question_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ii_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour l'itinérance." +
              "Appuyez sur 2 pour la question relative au postpayé." +
              "Appuyez sur 3 pour changer de langue." +
              "Appuyez sur 4 pour MNP." +
              "Appuyez sur 5 pour la question relative à la ligne fixe." +
              "Appuyez sur 6 pour toute question."
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


def _repeat1_2():
    response = VoiceResponse()
    response.redirect(url_for('welcome_2', _scheme='http', _external=True))
    return tiniyoml(response)


# options1specialoffers
@app.route('/ivr/lan_menu2/option1/option1', methods=['POST'])
def _specialoffers_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu1",
                      '8': "_main_menu1",
                      '0': "_repeat2"}

    if int(selected_options) == 7:
        response = _prev_menu1_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat2_2()
        return response
    else:
        return _redirect_welcome_2()


def _prev_menu1_2():
    response = VoiceResponse()
    response.redirect(url_for('welcome_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _main_menu1_2():
    response = VoiceResponse()
    response.redirect(url_for('welcome_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _repeat2_2():
    response = VoiceResponse()
    response.redirect(url_for('_special_offers_2', _scheme='http', _external=True))
    return tiniyoml(response)


# option2hellotunes

@app.route('/ivr/lan_menu2/hello_a', methods=['POST'])
def hello_a_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_hello_tun",
                      '2': "_start_value",
                      '3': "_stop_value",
                      '4': "_ss_vas",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat3"}

    if int(selected_options) == 1:
        response = _hello_tun_2()
        return response
    elif int(selected_options) == 2:
        response = _start_value_2()
        return response
    elif int(selected_options) == 3:
        response = _stop_value_2()
        return response
    elif int(selected_options) == 4:
        response = _ss_vas_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat3_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat3_2():
    response = VoiceResponse()
    response.redirect(url_for('_hello_tunes_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _call_to_ex_2():
    response = VoiceResponse()
    response.say("Nous transférons votre appel à Customer Executive." +
                 "S'il vous plaît, attendez!!! Nos cadres sont occupés sur une autre ligne.", voice=female, language=france)
    response.dial(number=executive_number, caller_id=cidfr)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option2/option1', methods=['GET', 'POST'])
def _hello_tun_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_b_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour lancer les mélodies Hello." +
              "Appuyez sur 2 pour arrêter les mélodies d'accueil." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_b', methods=['POST'])
def hello_b_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_start_hello",
                      '2': "_stop_hello",
                      '7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat4"}

    if int(selected_options) == 1:
        response = _start_hello_2()
        return response
    elif int(selected_options) == 2:
        response = _stop_hello_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu2_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat4_2()
        return response
    else:
        return _redirect_welcome_2()


@app.route('/ivr/lan_menu2/option2/option1/option1', methods=['GET', 'POST'])
def _start_hello_2():
    response = VoiceResponse()
    response.say("Votre mélodie Hello est activée avec succès." +
                 "Merci de votre appel.", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option2/option1/option2', methods=['GET', 'POST'])
def _stop_hello_2():
    response = VoiceResponse()
    response.say("Votre Hello tune activé a été désactivé avec succès." +
                 "Merci de votre appel.", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


def _prev_menu2_2():
    response = VoiceResponse()
    response.redirect(url_for('_hello_tunes_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _repeat4_2():
    response = VoiceResponse()
    response.redirect(url_for('_hello_tun_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option2/option2', methods=['GET', 'POST'])
def _start_value_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_c_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour l'Astrologie sur demande." +
              "Appuyez sur 2 pour Tiniyo Talkies." +
              "Appuyez sur 3 pour l'alerte d'appel manqué." +
              "Appuyez sur 4 pour l'alerte emploi." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_c', methods=['POST'])
def hello_c_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_astro_hello",
                      '2': "_talkies_hello",
                      '3': "_missed_hello",
                      '4': "_job_hello",
                      '7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat5"}

    if int(selected_options) == 1:
        response = _astro_hello_2()
        return response
    elif int(selected_options) == 2:
        response = _talkies_hello_2()
        return response
    elif int(selected_options) == 3:
        response = _missed_hello_2()
        return response
    elif int(selected_options) == 4:
        response = _job_hello_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu2_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat5_2()
        return response
    else:
        return _redirect_welcome_2()


@app.route('/ivr/lan_menu2/option2/option2/option1', methods=['GET', 'POST'])
def _astro_hello_2():
    response = VoiceResponse()
    response.say("Vos services d'astrologie sont activés avec succès." +
                 "Merci de votre appel.", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option2/option2/option2', methods=['GET', 'POST'])
def _talkies_hello_2():
    response = VoiceResponse()
    response.say("Vos services talkies sont activés avec succès." +
                 "Merci de votre appel.", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option2/option2/option3', methods=['GET', 'POST'])
def _missed_hello_2():
    response = VoiceResponse()
    response.say("Votre service d'appels manqués est activé avec succès." +
                 "Merci de votre appel.", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option2/option2/option4', methods=['GET', 'POST'])
def _job_hello_2():
    response = VoiceResponse()
    response.say("Vos services d'alerte emploi sont activés avec succès." +
                 "Merci de votre appel.", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


def _repeat5_2():
    response = VoiceResponse()
    response.redirect(url_for('_start_value_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option2/option3', methods=['GET', 'POST'])
def _stop_value_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_d_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Aucun service à valeur ajoutée n'a été lancé sur vos numéros." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_d', methods=['POST'])
def hello_d_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat6"}

    if int(selected_options) == 7:
        response = _prev_menu2_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat6_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat6_2():
    response = VoiceResponse()
    response.redirect(url_for('_stop_value_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option2/option4', methods=['GET', 'POST'])
def _ss_vas_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_e_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Merci, les détails seront bientôt partagés avec vous par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_e', methods=['POST'])
def hello_e_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat7"}

    if int(selected_options) == 7:
        response = _prev_menu2_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat7_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat7_2():
    response = VoiceResponse()
    response.redirect(url_for('_ss_vas_2', _scheme='http', _external=True))
    return tiniyoml(response)


# option3
@app.route('/ivr/lan_menu2/hello_f', methods=['POST'])
def hello_f_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_balance_val",
                      '2': "_balance_ded",
                      '3': "_special_five",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat8"}

    if int(selected_options) == 1:
        response = _balance_val_2()
        return response
    elif int(selected_options) == 2:
        response = _balance_ded_2()
        return response
    elif int(selected_options) == 3:
        response = _special_five_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat8_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat8_2():
    response = VoiceResponse()
    response.redirect(url_for('_balance_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option3/option1', methods=['GET', 'POST'])
def _balance_val_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_g_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos informations de solde et de validité pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_g', methods=['POST'])
def hello_g_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu3",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat9"}

    if int(selected_options) == 7:
        response = _prev_menu3_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat9_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat9_2():
    response = VoiceResponse()
    response.redirect(url_for('_balance_val_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu3_2():
    response = VoiceResponse()
    response.redirect(url_for('_balance_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option3/option2', methods=['GET', 'POST'])
def _balance_ded_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_h_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos informations de déduction de solde pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_h', methods=['POST'])
def hello_h_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu3",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat10"}

    if int(selected_options) == 7:
        response = _prev_menu3_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat10_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat10_2():
    response = VoiceResponse()
    response.redirect(url_for('_balance_ded_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option3/option3', methods=['GET', 'POST'])
def _special_five_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_i_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour les 5 derniers débits." +
              "Appuyez sur 2 pour les 5 derniers tarifs d'appels vocaux." +
              "Appuyez sur le 3 pour les 5 derniers tarifs SMS/mms sortants." +
              "Appuyez sur 4 pour les 5 derniers détails d'utilisation d'Internet." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_i', methods=['POST'])
def hello_i_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_debit_five",
                      '2': "_debit_voice",
                      '3': "_debit_sms",
                      '4': "_debit_internet",
                      '7': "_prev_menu3",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat11"}

    if int(selected_options) == 1:
        response = _debit_five_2()
        return response
    elif int(selected_options) == 2:
        response = _debit_voice_2()
        return response
    elif int(selected_options) == 3:
        response = _debit_sms_2()
        return response
    elif int(selected_options) == 4:
        response = _debit_internet_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu3_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat11_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat11_2():
    response = VoiceResponse()
    response.redirect(url_for('_special_five_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option3/option3/option1', methods=['GET', 'POST'])
def _debit_five_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_j_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos cinq dernières informations de débit pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_j', methods=['POST'])
def hello_j_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat12"}

    if int(selected_options) == 7:
        response = _prev_menu4_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat12_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat12_2():
    response = VoiceResponse()
    response.redirect(url_for('_debit_five_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu4_2():
    response = VoiceResponse()
    response.redirect(url_for('_special_five_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option3/option3/option2', methods=['GET', 'POST'])
def _debit_voice_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_k_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Your last five information on the rate of voice calls to get this information by SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_k', methods=['POST'])
def hello_k_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat13"}

    if int(selected_options) == 7:
        response = _prev_menu4_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat13_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat13_2():
    response = VoiceResponse()
    response.redirect(url_for('_debit_voice_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option3/option3/option3', methods=['GET', 'POST'])
def _debit_sms_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_l_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos cinq dernières informations SMS/MMS pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_l', methods=['POST'])
def hello_l_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat14"}

    if int(selected_options) == 7:
        response = _prev_menu4_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat14_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat14_2():
    response = VoiceResponse()
    response.redirect(url_for('_debit_sms_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option3/option3/option4', methods=['GET', 'POST'])
def _debit_internet_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_m_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos cinq dernières informations Internet de débit pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_m', methods=['POST'])
def hello_m_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat15"}

    if int(selected_options) == 7:
        response = _prev_menu4_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat15_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat15_2():
    response = VoiceResponse()
    response.redirect(url_for('_debit_internet_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_n', methods=['POST'])
def hello_n_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_info_money",
                      '2': "_info_customer",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat16"}

    if int(selected_options) == 1:
        response = _info_money_2()
        return response
    elif int(selected_options) == 2:
        response = _info_customer_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat16_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat16_2():
    response = VoiceResponse()
    response.redirect(url_for('_tiniyo_money_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option4/option1', methods=['GET', 'POST'])
def _info_money_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_0_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour l'argent Tiniyo." +
              "Appuyez sur 2 pour savoir comment devenir client Tiniyo." +
              "Appuyez sur 3 pour connaître les offres d'argent tiniyo." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_o', methods=['POST'])
def hello_0_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_info_tm",
                      '2': "_info_tc",
                      '3': "_info_offers",
                      '7': "_prev_menu5",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat17"}

    if int(selected_options) == 1:
        response = _info_tm_2()
        return response
    elif int(selected_options) == 2:
        response = _info_tc_2()
        return response
    elif int(selected_options) == 3:
        response = _info_offers_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu5_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat17_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat17_2():
    response = VoiceResponse()
    response.redirect(url_for('_info_money_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu5_2():
    response = VoiceResponse()
    response.redirect(url_for('_tiniyo_money_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option4/option1/option1', methods=['GET', 'POST'])
def _info_tm_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_p_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Informations Tiniyo pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_p', methods=['POST'])
def hello_p_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu6",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat18"}

    if int(selected_options) == 7:
        response = _prev_menu6_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat18_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat18_2():
    response = VoiceResponse()
    response.redirect(url_for('_info_tm_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu6_2():
    response = VoiceResponse()
    response.redirect(url_for('_info_money_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option4/option1/option2', methods=['GET', 'POST'])
def _info_tc_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_q_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Merci. Vous êtes devenu client Tiniyo." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_q', methods=['POST'])
def hello_q_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu6",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat19"}

    if int(selected_options) == 7:
        response = _prev_menu6_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat19_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat19_2():
    response = VoiceResponse()
    response.redirect(url_for('_info_tc_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option4/option1/option3', methods=['GET', 'POST'])
def _info_offers_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_r_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Connaître tiniyo money offre des informations pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_r', methods=['POST'])
def hello_r_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu6",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat20"}

    if int(selected_options) == 7:
        response = _prev_menu6_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat20_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat20_2():
    response = VoiceResponse()
    response.redirect(url_for('_info_offers_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option4/option2', methods=['GET', 'POST'])
def _info_customer_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_s_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 si vous connaissez votre MPIN." +
              "Appuyez sur 2 si vous n'avez pas MPIN." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_s', methods=['POST'])
def hello_s_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_your_mpin",
                      '2': "_not_mpin",
                      '7': "_prev_menu5",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat21"}

    if int(selected_options) == 1:
        response = _your_mpin_2()
        return response
    elif int(selected_options) == 2:
        response = _not_mpin_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu5_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat21_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat21_2():
    response = VoiceResponse()
    response.redirect(url_for('_info_customer_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option4/option2/option1', methods=['GET', 'POST'])
def _your_mpin_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_t_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour entrer votre MPIN." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_t', methods=['POST'])
def hello_t_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_mpin_no",
                      '7': "_prev_menu5",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat21"}

    if int(selected_options) == 1:
        response = _mpin_no_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu5_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat21_2()
        return response
    else:
        return _redirect_welcome_2()


@app.route('/ivr/lan_menu2/option4/option2/op1', methods=['GET', 'POST'])
def _mpin_no_2():
    response = VoiceResponse()
    response.say("Vous avez entré un MPIN incorrect. Merci d'avoir appelé." +
                 "Rappelez plus tard. Merci !!!", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option4/option2/option2', methods=['GET', 'POST'])
def _not_mpin_2():
    response = VoiceResponse()
    response.say("Nous transférons votre appel à Customer Executive" +
                 "Veuillez patienter !!! Notre exécutif est occupé sur une autre ligne", voice=female, language=france)
    response.dial(number=executive_number, caller_id=cidfr)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_u', methods=['POST'])
def hello_u_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_start_3g",
                      '2': "_stop_3g",
                      '3': "_setting_3g",
                      '4': "_info_dt",
                      '5': "_info_pc",
                      '6': "_ques_3g",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat22"}

    if int(selected_options) == 1:
        response = _start_3g_2()
        return response
    elif int(selected_options) == 2:
        response = _stop_3g_2()
        return response
    elif int(selected_options) == 3:
        response = _setting_3g_2()
        return response
    elif int(selected_options) == 4:
        response = _info_dt_2()
        return response
    elif int(selected_options) == 5:
        response = _info_pc_2()
        return response
    elif int(selected_options) == 6:
        response = _ques_3g_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat22_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat22_2():
    response = VoiceResponse()
    response.redirect(url_for('_data_services_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option1', methods=['GET', 'POST'])
def _start_3g_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_v_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour démarrer le service 3G." +
              "Appuyez sur 2 pour démarrer le service Internet." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/lan_menu2/ivr/hello_v', methods=['POST'])
def hello_v_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_starts_3g",
                      '2': "_starts_internet",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat23"}

    if int(selected_options) == 1:
        response = _starts_3g_2()
        return response
    elif int(selected_options) == 2:
        response = _starts_internet_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat23_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat23_2():
    response = VoiceResponse()
    response.redirect(url_for('_start_3g_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu7_2():
    response = VoiceResponse()
    response.redirect(url_for('_data_services_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option1/option1', methods=['GET', 'POST'])
def _starts_3g_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_w_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos informations de service pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_w', methods=['POST'])
def hello_w_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu8",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat24"}

    if int(selected_options) == 7:
        response = _prev_menu8_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat24_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat24_2():
    response = VoiceResponse()
    response.redirect(url_for('_starts_3g_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu8_2():
    response = VoiceResponse()
    response.redirect(url_for('_start_3g_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option1/option2', methods=['GET', 'POST'])
def _starts_internet_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_x_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos informations de service Internet pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_x', methods=['POST'])
def hello_x_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu8",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat25"}

    if int(selected_options) == 7:
        response = _prev_menu8_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat25_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat25_2():
    response = VoiceResponse()
    response.redirect(url_for('_starts_internet_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option2', methods=['GET', 'POST'])
def _stop_3g_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_y_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour arrêter le service 3G." +
              "Appuyez sur 2 pour arrêter le service Internet." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_y', methods=['GET', 'POST'])
def hello_y_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_stops_3g",
                      '2': "_stops_internet",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat26"}

    if int(selected_options) == 1:
        response = _stops_3g_2()
        return response
    elif int(selected_options) == 2:
        response = _stops_internet_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat26_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat26_2():
    response = VoiceResponse()
    response.redirect(url_for('_stop_3g_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option2/option1', methods=['GET', 'POST'])
def _stops_3g_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_z_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos informations de service pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_z', methods=['POST'])
def hello_z_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu9",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat27"}

    if int(selected_options) == 7:
        response = _prev_menu9_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat27_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat27_2():
    response = VoiceResponse()
    response.redirect(url_for('_stops_3g_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu9_2():
    response = VoiceResponse()
    response.redirect(url_for('_stop_3g_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option2/option2', methods=['GET', 'POST'])
def _stops_internet_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_aa_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos informations de service Internet pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_aa', methods=['POST'])
def hello_aa_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu9",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat28"}

    if int(selected_options) == 7:
        response = _prev_menu9_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat28_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat28_2():
    response = VoiceResponse()
    response.redirect(url_for('_stops_internet_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option3', methods=['GET', 'POST'])
def _setting_3g_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_bb_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour obtenir les paramètres des services Internet." +
              "Appuyez sur 2 pour obtenir les paramètres du MMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_bb', methods=['POST'])
def hello_bb_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_setting_internet",
                      '2': "_setting_mms",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat29"}

    if int(selected_options) == 1:
        response = _setting_internet_2()
        return response
    elif int(selected_options) == 2:
        response = _setting_mms_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat29_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat29_2():
    response = VoiceResponse()
    response.redirect(url_for('_setting_3g_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option3/option1', methods=['GET', 'POST'])
def _setting_internet_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_cc_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Paramètre Internet pour obtenir par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_cc', methods=['POST'])
def hello_cc_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu10",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat30"}

    if int(selected_options) == 7:
        response = _prev_menu10_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat30_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat30_2():
    response = VoiceResponse()
    response.redirect(url_for('_setting_internet_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu10_2():
    response = VoiceResponse()
    response.redirect(url_for('_setting_3g_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option3/option2', methods=['GET', 'POST'])
def _setting_mms_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_dd_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Paramètre MMS pour obtenir par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_dd', methods=['POST'])
def hello_dd_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu10",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat31"}

    if int(selected_options) == 7:
        response = _prev_menu10_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat31_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat31_2():
    response = VoiceResponse()
    response.redirect(url_for('_setting_mms_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option4', methods=['GET', 'POST'])
def _info_dt_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ee_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour obtenir des informations sur la procédure d'installation." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_ee', methods=['POST'])
def hello_ee_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_inf_install",
                      '2': "_setting_mms",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat32"}

    if int(selected_options) == 1:
        response = _inf_install_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat32_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat32_2():
    response = VoiceResponse()
    response.redirect(url_for('_info_dt_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option4/option1', methods=['GET', 'POST'])
def _inf_install_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ff_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Pour plus d'informations sur l'installation d'une carte de données ou d'un dongle avec." +
              "Appuyez sur 1 pour le système d'exploitation Windows." +
              "Appuyez sur 2 pour le système d'exploitation Linux." +
              "Appuyez sur 3 pour Macbook" +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_ff', methods=['POST'])
def hello_ff_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_system_os",
                      '2': "_system_linux",
                      '3': "_system_mac",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat33"}

    if int(selected_options) == 1:
        response = _system_os_2()
        return response
    elif int(selected_options) == 2:
        response = _system_linux_2()
        return response
    elif int(selected_options) == 3:
        response = _system_mac_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat33_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat33_2():
    response = VoiceResponse()
    response.redirect(url_for('_inf_install_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option4/option1_op1', methods=['GET', 'POST'])
def _system_os_2():
    response = VoiceResponse()
    response.say("Nos cadres sont occupés sur une autre ligne." +
                 "Nous rappellerons bientôt", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option4/option1_op2', methods=['GET', 'POST'])
def _system_linux_2():
    response = VoiceResponse()
    response.say("Nos cadres sont occupés sur une autre ligne." +
                 "Nous rappellerons bientôt", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option4/option1_op3', methods=['GET', 'POST'])
def _system_mac_2():
    response = VoiceResponse()
    response.say("Nos cadres sont occupés sur une autre ligne." +
                 "Nous rappellerons bientôt", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option5', methods=['GET', 'POST'])
def _info_pc_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_gg_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Pour plus d'informations sur la connexion." +
              "Appuyez sur 1 pour PC via Bluetooth." +
              "Appuyez sur 2 pour PC via infrarouge." +
              "Appuyez sur 3 pour PC via câble." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_gg', methods=['GET', 'POST'])
def hello_gg_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_bluetooth_pc",
                      '2': "_infrared_pc",
                      '3': "_cable_pc",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat34"}

    if int(selected_options) == 1:
        response = _bluetooth_pc_2()
        return response
    elif int(selected_options) == 2:
        response = _infrared_pc_2()
        return response
    elif int(selected_options) == 3:
        response = _cable_pc_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat34_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat34_2():
    response = VoiceResponse()
    response.redirect(url_for('_info_pc_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option5/option1', methods=['GET', 'POST'])
def _bluetooth_pc_2():
    response = VoiceResponse()
    response.say("Nos cadres sont occupés sur une autre ligne." +
                 "S'il vous plaît, attendez!!!", voice=female, language=france)
    response.dial(number=executive_number, caller_id=cidfr)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option5/option2', methods=['GET', 'POST'])
def _infrared_pc_2():
    response = VoiceResponse()
    response.say("Nos cadres sont occupés sur une autre ligne." +
                 "S'il vous plaît, attendez!!!", voice=female, language=france)
    response.dial(number=executive_number, caller_id=cidfr)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option5/option3', methods=['GET', 'POST'])
def _cable_pc_2():
    response = VoiceResponse()
    response.say("Nos cadres sont occupés sur une autre ligne." +
                 "S'il vous plaît, attendez!!!", voice=female, language=france)
    response.dial(number=executive_number, caller_id=cidfr)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option6', methods=['GET', 'POST'])
def _ques_3g_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_hh_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour toute question." +
              "Appuyez sur 2 pour obtenir de l'aide technique." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_hh', methods=['POST'])
def hello_hh_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_ques_any",
                      '2': "_technical_help",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat35"}

    if int(selected_options) == 1:
        response = _ques_any_2()
        return response
    elif int(selected_options) == 2:
        response = _technical_help_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat35_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat35_2():
    response = VoiceResponse()
    response.redirect(url_for('_ques_3g_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option6/option1', methods=['GET', 'POST'])
def _ques_any_2():
    response = VoiceResponse()
    response.say("Nos cadres sont occupés sur une autre ligne." +
                 "S'il vous plaît, attendez!!!" +
                 "Appelez à nouveau plus tard.", voice=female, language=france)
    response.dial(number=executive_number, caller_id=cidfr)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option5/option6/option2', methods=['GET', 'POST'])
def _technical_help_2():
    response = VoiceResponse()
    response.say("Notre équipe technique est occupée sur une autre ligne." +
                 "S'il vous plaît, attendez!!!" +
                 "Appelez à nouveau plus tard.", voice=female, language=france)
    response.dial(number=technician_number, caller_id=cidfr)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_ii', methods=['POST'])
def hello_ii_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_Roaming",
                      '2': "_postpaid",
                      '3': "_change",
                      '4': "_for_mnp",
                      '5': "_ques_fix",
                      '6': "_ques_any",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat36"}

    if int(selected_options) == 1:
        response = _Roaming_2()
        return response
    elif int(selected_options) == 2:
        response = _postpaid_2()
        return response
    elif int(selected_options) == 3:
        response = _change_2()
        return response
    elif int(selected_options) == 4:
        response = _for_mnp_2()
        return response
    elif int(selected_options) == 5:
        response = _ques_fix_2()
        return response
    elif int(selected_options) == 6:
        response = _ques_any_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat36_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat36_2():
    response = VoiceResponse()
    response.redirect(url_for('_any_question_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option1', methods=['GET', 'POST'])
def _Roaming_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_jj_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour l'itinérance nationale." +
              "Appuyez sur le 2 pour obtenir des informations sur l'itinérance internationale." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_jj', methods=['GET', 'POST'])
def hello_jj_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_national_roaming",
                      '2': "_international_roaming",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat37"}

    if int(selected_options) == 1:
        response = _national_roaming_2()
        return response
    elif int(selected_options) == 2:
        response = _international_roaming_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat37_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat37_2():
    response = VoiceResponse()
    response.redirect(url_for('_Roaming_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu11_2():
    response = VoiceResponse()
    response.redirect(url_for('_any_question_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option1/option1', methods=['GET', 'POST'])
def _national_roaming_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ll_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos informations d'itinérance nationale pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_ll', methods=['POST'])
def hello_ll_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu12",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat38"}

    if int(selected_options) == 7:
        response = _prev_menu12_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat38_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat38_2():
    response = VoiceResponse()
    response.redirect(url_for('_national_roaming_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu12_2():
    response = VoiceResponse()
    response.redirect(url_for('_Roaming_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option1/option2', methods=['GET', 'POST'])
def _international_roaming_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_kk_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos informations d'itinérance internationale pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_kk', methods=['POST'])
def hello_kk_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu12",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat39"}

    if int(selected_options) == 7:
        response = _prev_menu12_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat39_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat39_2():
    response = VoiceResponse()
    response.redirect(url_for('_international_roaming_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option2', methods=['GET', 'POST'])
def _postpaid_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_mm_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour la question liée au postpayé." +
              "Appuyez sur 2 pour la question relative au prépayé au postpayé." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_mm', methods=['POST'])
def hello_mm_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_question_postpaid",
                      '2': "_prepaid_postpaid",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat40"}

    if int(selected_options) == 1:
        response = _question_postpaid_2()
        return response
    elif int(selected_options) == 2:
        response = _prepaid_postpaid_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat40_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat40_2():
    response = VoiceResponse()
    response.redirect(url_for('_postpaid_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option2/option1', methods=['GET', 'POST'])
def _question_postpaid_2():
    response = VoiceResponse()
    response.say("Nous transférons votre appel à Customer Executive" +
                 "Veuillez patienter !!! Nos cadres sont occupés sur une autre ligne", voice=female, language=france)
    response.dial(number=executive_number, caller_id=cidfr)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option2/option2', methods=['GET', 'POST'])
def _prepaid_postpaid_2():
    response = VoiceResponse()
    response.say("Nous transférons votre appel à Customer Executive" +
                 "Veuillez patienter !!! Nos cadres sont occupés sur une autre ligne", voice=female, language=france)
    response.dial(number=executive_number, caller_id=cidfr)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option3', methods=['GET', 'POST'])
def _change_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_nn_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour changer votre langue." +
              "Appuyez sur 2 pour modifier le TPIN." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_nn', methods=['POST'])
def hello_nn_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_change_language",
                      '2': "_change_tpin",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat41"}

    if int(selected_options) == 1:
        response = _change_language_2()
        return response
    elif int(selected_options) == 2:
        response = _change_tpin_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat41_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat41_2():
    response = VoiceResponse()
    response.redirect(url_for('_change_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option3/option1', methods=['GET', 'POST'])
def _change_language_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_oo_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Choisissez votre langue." +
              "Appuyez sur 1 pour l'anglais." +
              "Appuyez sur 2 pour l'espagnol." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_oo', methods=['POST'])
def hello_oo_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_lan_en",
                      '2': "_lan_spanish",
                      '7': "_prev_menu13",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat42"}

    if int(selected_options) == 1:
        response = _lan_en_2()
        return response
    elif int(selected_options) == 2:
        response = _lan_spanish_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu13_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat42_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat42_2():
    response = VoiceResponse()
    response.redirect(url_for('_change_language_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu13_2():
    response = VoiceResponse()
    response.redirect(url_for('_change_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option3/option1_op1', methods=['GET', 'POST'])
def _lan_en_2():
    response = VoiceResponse()
    response.say("English Language successfully updated." +
                 "Thank you for calling", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option3/option1_op2', methods=['GET', 'POST'])
def _lan_spanish_2():
    response = VoiceResponse()
    response.say("Idioma español actualizado con éxito." +
                 "Gracias por llamar", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option3/option2', methods=['GET', 'POST'])
def _change_tpin_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_pp_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("appuyez sur 1 pour entrer votre TPIN." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_pp', methods=['POST'])
def hello_pp_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_enter_tpin",
                      '7': "_prev_menu12",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat43"}

    if int(selected_options) == 1:
        response = _enter_tpin_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu13_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat43_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat43_2():
    response = VoiceResponse()
    response.redirect(url_for('_change_tpin_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option3/option2_op1', methods=['GET', 'POST'])
def _enter_tpin_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=4, action=url_for('hello_qq_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Entrez votre TPIN." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_qq', methods=['POST'])
def hello_qq_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu13",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat43"}

    if int(selected_options) == 7:
        response = _prev_menu13_2()
        return response
    elif int(selected_options) == 2580:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 1472:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat43_2()
        return response
    else:
        return _redirect_welcome_2()


@app.route('/ivr/lan_menu2/option6/option4', methods=['GET', 'POST'])
def _for_mnp_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_rr_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour les informations MNP." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_rr', methods=['POST'])
def hello_rr_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_info_mnp",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat44"}

    if int(selected_options) == 1:
        response = _info_mnp_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat44_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat44_2():
    response = VoiceResponse()
    response.redirect(url_for('_for_mnp_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option4/option1', methods=['GET', 'POST'])
def _info_mnp_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ss_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Vos informations MNP pour obtenir ces informations par SMS." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_ss', methods=['POST'])
def hello_ss_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu14",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat45"}

    if int(selected_options) == 7:
        response = _prev_menu14_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat45_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat45_2():
    response = VoiceResponse()
    response.redirect(url_for('_info_mnp_2', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu14_2():
    response = VoiceResponse()
    response.redirect(url_for('_for_mnp_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option5', methods=['GET', 'POST'])
def _ques_fix_2():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_tt_2', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Appuyez sur 1 pour le service de ligne fixe Tiniyo." +
              "Appuyez sur 2 pour le service de télévision numérique Tiniyo." +
              "Pour revenir au menu précédent, appuyez sur 7." +
              "Pour revenir au menu principal, appuyez sur 8." +
              "Pour Tiniyo Executive, appuyez sur le 9." +
              "Pour répéter, appuyez sur 0.", voice=male, language=france, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/hello_tt', methods=['POST'])
def hello_tt_2():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_line_fixed",
                      '2': "_digital_tv",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat46"}

    if int(selected_options) == 1:
        response = _line_fixed_2()
        return response
    elif int(selected_options) == 2:
        response = _digital_tv_2()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11_2()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_2()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_2()
        return response
    elif int(selected_options) == 0:
        response = _repeat46_2()
        return response
    else:
        return _redirect_welcome_2()


def _repeat46_2():
    response = VoiceResponse()
    response.redirect(url_for('_ques_fix_2', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option5/option1', methods=['GET', 'POST'])
def _line_fixed_2():
    response = VoiceResponse()
    response.say("Informations sur les services de ligne fixe Tiniyo à obtenir par SMS." +
                 "Merci de votre appel.", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu2/option6/option5/option2', methods=['GET', 'POST'])
def _digital_tv_2():
    response = VoiceResponse()
    response.say("Tiniyo Informations sur la télévision numérique à obtenir par SMS." +
                 "Merci de votre appel.", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/welcome', methods=['GET', 'POST'])
def welcome_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('menu_3', _scheme='http', _external=True), method="POST"
    )as g:
        g.say(message="Nuestro menú ha cambiado. Por favor, escuche con atención." +
                      "Presione 1 para tarifas de llamadas especiales y ofertas de tiempo completo." +
                      "Presione 2 para Hello Tunes y otros servicios de valor agregado." +
                      "Presione 3 para conocer el saldo y la validez de su teléfono móvil, motivo de la deducción del saldo." +
                      "Presiona 4 para Tiniyo Money." +
                      "Presione 5 para obtener información sobre servicios de datos como 3G, 4G, Internet móvil, Dongle." +
                      "Presione 6 para cualquier pregunta sobre MNP, DTH, pospago y facturas telefónicas." +
                      "Para repetir Presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/menu', methods=['POST'])
def menu_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_special_offers",
                      '2': "_hello_tunes",
                      '3': "_balance",
                      '4': "_tiniyo_money",
                      '5': "_data_services",
                      '6': "_any_question",
                      '0': "_repeat1"}

    if int(selected_options) == 1:
        response = _special_offers_3()
        return response
    elif int(selected_options) == 2:
        response = _hello_tunes_3()
        return response
    elif int(selected_options) == 3:
        response = _balance_3()
        return response
    elif int(selected_options) == 4:
        response = _tiniyo_money_3()
        return response
    elif int(selected_options) == 5:
        response = _data_services_3()
        return response
    elif int(selected_options) == 6:
        response = _any_question_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat1_3()
        return response
    else:
        return _redirect_welcome_3()


# methods
def _redirect_welcome_3():
    response = VoiceResponse()
    response.say("Ingresa una clave incorrecta. Vuelve a llamar." +
                 "Gracias por llamar.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option1', methods=['GET', 'POST'])
def _special_offers_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('_specialoffers_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Oferta especializada para ti." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option2', methods=['GET', 'POST'])
def _hello_tunes_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_a_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para Hello Tune." +
              "Presione 2 para iniciar cualquier otro servicio de valores agregados." +
              "Presione 3 para detener los servicios de valor agregado." +
              "Presione 4 para recibir un mensaje de texto sobre cómo iniciar / detener un VAS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option3', methods=['GET', 'POST'])
def _balance_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_f_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para conocer el saldo y la validez de su teléfono móvil." +
              "Presione 2 para obtener información detallada sobre la deducción del saldo." +
              "Presione 3 para obtener información sobre el especial 5." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option4', methods=['GET', 'POST'])
def _tiniyo_money_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para obtener información sobre el dinero tiniyo." +
              "Presione 2 Si es cliente de tiniyo." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5', methods=['GET', 'POST'])
def _data_services_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_u_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para iniciar 3G." +
              "Presione 2 para detener 3G." +
              "Presione 3 para obtener la configuración de 3G." +
              "Presione 4 para obtener información sobre la tarjeta de datos o los detalles de la llave." +
              "Presione 5 para obtener información sobre el procedimiento de conectividad de la PC." +
              "Presione 6 para preguntas y ayuda técnica." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6', methods=['GET', 'POST'])
def _any_question_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ii_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para roaming." +
              "Presione 2 para preguntas relacionadas con pospago." +
              "Presione 3 para cambiar el idioma." +
              "Presione 4 para MNP." +
              "Presione 5 para preguntas relacionadas con la línea fija." +
              "Presione 6 para cualquier pregunta."
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


def _repeat1_3():
    response = VoiceResponse()
    response.redirect(url_for('welcome_3', _scheme='http', _external=True))
    return tiniyoml(response)


# options1specialoffers
@app.route('/ivr/lan_menu3/option1/option1', methods=['POST'])
def _specialoffers_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu1",
                      '8': "_main_menu1",
                      '0': "_repeat2"}

    if int(selected_options) == 7:
        response = _prev_menu1_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat2_3()
        return response
    else:
        return _redirect_welcome_3()


def _prev_menu1_3():
    response = VoiceResponse()
    response.redirect(url_for('welcome_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _main_menu1_3():
    response = VoiceResponse()
    response.redirect(url_for('welcome_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _repeat2_3():
    response = VoiceResponse()
    response.redirect(url_for('_special_offers_3', _scheme='http', _external=True))
    return tiniyoml(response)


# option2hellotunes

@app.route('/ivr/lan_menu3/hello_a', methods=['POST'])
def hello_a_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_hello_tun",
                      '2': "_start_value",
                      '3': "_stop_value",
                      '4': "_ss_vas",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat3"}

    if int(selected_options) == 1:
        response = _hello_tun_3()
        return response
    elif int(selected_options) == 2:
        response = _start_value_3()
        return response
    elif int(selected_options) == 3:
        response = _stop_value_3()
        return response
    elif int(selected_options) == 4:
        response = _ss_vas_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat3_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat3_3():
    response = VoiceResponse()
    response.redirect(url_for('_hello_tunes_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _call_to_ex_3():
    response = VoiceResponse()
    response.say("Estamos transfiriendo su llamada a Customer Executive." +
                 "¡¡¡Espere por favor!!! Nuestros ejecutivos están ocupados en otra línea.", voice=female, language=spaines)
    response.dial(number=executive_number, caller_id=cides)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option2/option1', methods=['GET', 'POST'])
def _hello_tun_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_b_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para iniciar Hello Tunes." +
              "Presione 2 para detener las melodías de saludo." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_b', methods=['POST'])
def hello_b_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_start_hello",
                      '2': "_stop_hello",
                      '7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat4"}

    if int(selected_options) == 1:
        response = _start_hello_3()
        return response
    elif int(selected_options) == 2:
        response = _stop_hello_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu2_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat4_3()
        return response
    else:
        return _redirect_welcome_3()


@app.route('/ivr/lan_menu3/option2/option1/option1', methods=['GET', 'POST'])
def _start_hello_3():
    response = VoiceResponse()
    response.say("Tu Hellotune activado con éxito." +
                 "Gracias por llamar.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option2/option1/option2', methods=['GET', 'POST'])
def _stop_hello_3():
    response = VoiceResponse()
    response.say("Tu activación Hello Tune se desactivó con éxito." +
                 "Gracias por llamar.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


def _prev_menu2_3():
    response = VoiceResponse()
    response.redirect(url_for('_hello_tunes_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _repeat4_3():
    response = VoiceResponse()
    response.redirect(url_for('_hello_tun_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option2/option2', methods=['GET', 'POST'])
def _start_value_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_c_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para Astrología a pedido." +
              "Presione 2 para Tiniyo Talkies." +
              "Presione 3 para Alerta de llamada perdida." +
              "Presione 4 para Alerta de trabajo." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_c', methods=['POST'])
def hello_c_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_astro_hello",
                      '2': "_talkies_hello",
                      '3': "_missed_hello",
                      '4': "_job_hello",
                      '7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat5"}

    if int(selected_options) == 1:
        response = _astro_hello_3()
        return response
    elif int(selected_options) == 2:
        response = _talkies_hello_3()
        return response
    elif int(selected_options) == 3:
        response = _missed_hello_3()
        return response
    elif int(selected_options) == 4:
        response = _job_hello_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu2_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat5_3()
        return response
    else:
        return _redirect_welcome_3()


@app.route('/ivr/lan_menu3/option2/option2/option1', methods=['GET', 'POST'])
def _astro_hello_3():
    response = VoiceResponse()
    response.say("Sus servicios de astrología se activaron con éxito." +
                 "Gracias por llamar.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option2/option2/option2', methods=['GET', 'POST'])
def _talkies_hello_3():
    response = VoiceResponse()
    response.say("Sus servicios de talkies se activaron con éxito." +
                 "Gracias por llamar.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option2/option2/option3', methods=['GET', 'POST'])
def _missed_hello_3():
    response = VoiceResponse()
    response.say("Su servicio de alerta de llamadas perdidas se activó con éxito." +
                 "Gracias por llamar.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option2/option2/option4', methods=['GET', 'POST'])
def _job_hello_3():
    response = VoiceResponse()
    response.say("Sus servicios de alerta de empleo se activaron con éxito." +
                 "Gracias por llamar.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


def _repeat5_3():
    response = VoiceResponse()
    response.redirect(url_for('_start_value_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option2/option3', methods=['GET', 'POST'])
def _stop_value_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_d_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("No se han iniciado servicios de valor agregado en sus números." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_d', methods=['POST'])
def hello_d_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat6"}

    if int(selected_options) == 7:
        response = _prev_menu2_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat6_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat6_3():
    response = VoiceResponse()
    response.redirect(url_for('_stop_value_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option2/option4', methods=['GET', 'POST'])
def _ss_vas_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_e_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Los detalles de agradecimiento se compartirán con usted pronto a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_e', methods=['POST'])
def hello_e_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu2",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat7"}

    if int(selected_options) == 7:
        response = _prev_menu2_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat7_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat7_3():
    response = VoiceResponse()
    response.redirect(url_for('_ss_vas_3', _scheme='http', _external=True))
    return tiniyoml(response)


# option3
@app.route('/ivr/lan_menu3/hello_f', methods=['POST'])
def hello_f_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_balance_val",
                      '2': "_balance_ded",
                      '3': "_special_five",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat8"}

    if int(selected_options) == 1:
        response = _balance_val_3()
        return response
    elif int(selected_options) == 2:
        response = _balance_ded_3()
        return response
    elif int(selected_options) == 3:
        response = _special_five_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat8_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat8_3():
    response = VoiceResponse()
    response.redirect(url_for('_balance_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option3/option1', methods=['GET', 'POST'])
def _balance_val_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_g_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Su información de saldo y validez para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_g', methods=['POST'])
def hello_g_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu3",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat9"}

    if int(selected_options) == 7:
        response = _prev_menu3_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat9_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat9_3():
    response = VoiceResponse()
    response.redirect(url_for('_balance_val_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu3_3():
    response = VoiceResponse()
    response.redirect(url_for('_balance_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option3/option2', methods=['GET', 'POST'])
def _balance_ded_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_h_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Su información de saldo y validez para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_h', methods=['POST'])
def hello_h_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu3",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat10"}

    if int(selected_options) == 7:
        response = _prev_menu3_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat10_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat10_3():
    response = VoiceResponse()
    response.redirect(url_for('_balance_ded_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option3/option3', methods=['GET', 'POST'])
def _special_five_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_i_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para los últimos 5 débitos vas." +
              "Presione 2 para los últimos 5 débitos de llamadas de voz." +
              "Presione 3 para los últimos 5 débitos sms / mms salientes." +
              "Presione 4 para ver los últimos 5 detalles del uso de Internet." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_i', methods=['POST'])
def hello_i_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_debit_five",
                      '2': "_debit_voice",
                      '3': "_debit_sms",
                      '4': "_debit_internet",
                      '7': "_prev_menu3",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat11"}

    if int(selected_options) == 1:
        response = _debit_five_3()
        return response
    elif int(selected_options) == 2:
        response = _debit_voice_3()
        return response
    elif int(selected_options) == 3:
        response = _debit_sms_3()
        return response
    elif int(selected_options) == 4:
        response = _debit_internet_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu3_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat11_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat11_3():
    response = VoiceResponse()
    response.redirect(url_for('_special_five_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option3/option3/option1', methods=['GET', 'POST'])
def _debit_five_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_j_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Sus últimos cinco datos de débito para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_j', methods=['POST'])
def hello_j_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat12"}

    if int(selected_options) == 7:
        response = _prev_menu4_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat12_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat12_3():
    response = VoiceResponse()
    response.redirect(url_for('_debit_five_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu4_3():
    response = VoiceResponse()
    response.redirect(url_for('_special_five_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option3/option3/option2', methods=['GET', 'POST'])
def _debit_voice_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_k_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Información de débito de sus últimas cinco llamadas de voz para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_k', methods=['POST'])
def hello_k_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat13"}

    if int(selected_options) == 7:
        response = _prev_menu4_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat13_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat13_3():
    response = VoiceResponse()
    response.redirect(url_for('_debit_voice_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option3/option3/option3', methods=['GET', 'POST'])
def _debit_sms_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_l_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Sus últimos cinco datos de débito SMS / MMS para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_l', methods=['POST'])
def hello_l_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat14"}

    if int(selected_options) == 7:
        response = _prev_menu4_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat14_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat14_3():
    response = VoiceResponse()
    response.redirect(url_for('_debit_sms_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option3/option3/option4', methods=['GET', 'POST'])
def _debit_internet_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_m_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Sus últimos cinco datos de Internet de débito para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_m', methods=['POST'])
def hello_m_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu4",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat15"}

    if int(selected_options) == 7:
        response = _prev_menu4_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat15_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat15_3():
    response = VoiceResponse()
    response.redirect(url_for('_debit_internet_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_n', methods=['POST'])
def hello_n_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_info_money",
                      '2': "_info_customer",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat16"}

    if int(selected_options) == 1:
        response = _info_money_3()
        return response
    elif int(selected_options) == 2:
        response = _info_customer_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat16_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat16_3():
    response = VoiceResponse()
    response.redirect(url_for('_tiniyo_money_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option4/option1', methods=['GET', 'POST'])
def _info_money_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_0_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para obtener dinero de Tiniyo." +
              "Presione 2 para obtener información sobre cómo convertirse en cliente de tiniyo." +
              "Presione 3 para conocer las ofertas de dinero de tiniyo." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_o', methods=['POST'])
def hello_0_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_info_tm",
                      '2': "_info_tc",
                      '3': "_info_offers",
                      '7': "_prev_menu5",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat17"}

    if int(selected_options) == 1:
        response = _info_tm_3()
        return response
    elif int(selected_options) == 2:
        response = _info_tc_3()
        return response
    elif int(selected_options) == 3:
        response = _info_offers_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu5_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat17_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat17_3():
    response = VoiceResponse()
    response.redirect(url_for('_info_money_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu5_3():
    response = VoiceResponse()
    response.redirect(url_for('_tiniyo_money_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option4/option1/option1', methods=['GET', 'POST'])
def _info_tm_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_p_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Información de Tiniyo para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_p', methods=['POST'])
def hello_p_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu6",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat18"}

    if int(selected_options) == 7:
        response = _prev_menu6_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat18_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat18_3():
    response = VoiceResponse()
    response.redirect(url_for('_info_tm_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu6_3():
    response = VoiceResponse()
    response.redirect(url_for('_info_money_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option4/option1/option2', methods=['GET', 'POST'])
def _info_tc_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_q_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Gracias. Te has convertido en cliente de tiniyo." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_q', methods=['POST'])
def hello_q_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu6",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat19"}

    if int(selected_options) == 7:
        response = _prev_menu6_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat19_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat19_3():
    response = VoiceResponse()
    response.redirect(url_for('_info_tc_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option4/option1/option3', methods=['GET', 'POST'])
def _info_offers_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_r_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Para conocer sobre tiniyo money ofrece información para obtener esta información vía SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_r', methods=['POST'])
def hello_r_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu6",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat20"}

    if int(selected_options) == 7:
        response = _prev_menu6_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat20_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat20_3():
    response = VoiceResponse()
    response.redirect(url_for('_info_offers_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option4/option2', methods=['GET', 'POST'])
def _info_customer_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_s_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 si conoce su MPIN." +
              "Presione 2 si no tiene MPIN." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_s', methods=['POST'])
def hello_s_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_your_mpin",
                      '2': "_not_mpin",
                      '7': "_prev_menu5",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat21"}

    if int(selected_options) == 1:
        response = _your_mpin_3()
        return response
    elif int(selected_options) == 2:
        response = _not_mpin_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu5_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat21_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat21_3():
    response = VoiceResponse()
    response.redirect(url_for('_info_customer_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option4/option2/option1', methods=['GET', 'POST'])
def _your_mpin_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_t_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para ingresar su MPIN." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_t', methods=['POST'])
def hello_t_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_mpin_no",
                      '7': "_prev_menu5",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat21"}

    if int(selected_options) == 1:
        response = _mpin_no_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu5_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat21_3()
        return response
    else:
        return _redirect_welcome_3()


@app.route('/ivr/lan_menu3/option4/option2/op1', methods=['GET', 'POST'])
def _mpin_no_3():
    response = VoiceResponse()
    response.say("Ingresa un MPIN incorrecto. Gracias por llamar." +
                 "Vuelve a llamar más tarde.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option4/option2/option2', methods=['GET', 'POST'])
def _not_mpin_3():
    response = VoiceResponse()
    response.say("Estamos transfiriendo su llamada a Customer Executive." +
                 "¡¡¡Espere por favor!!! Nuestros ejecutivos están ocupados en otra línea.", voice=female, language=spaines)
    response.dial(number=executive_number, caller_id=cides)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_u', methods=['POST'])
def hello_u_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_start_3g",
                      '2': "_stop_3g",
                      '3': "_setting_3g",
                      '4': "_info_dt",
                      '5': "_info_pc",
                      '6': "_ques_3g",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat22"}

    if int(selected_options) == 1:
        response = _start_3g_3()
        return response
    elif int(selected_options) == 2:
        response = _stop_3g_3()
        return response
    elif int(selected_options) == 3:
        response = _setting_3g_3()
        return response
    elif int(selected_options) == 4:
        response = _info_dt_3()
        return response
    elif int(selected_options) == 5:
        response = _info_pc_3()
        return response
    elif int(selected_options) == 6:
        response = _ques_3g_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat22_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat22_3():
    response = VoiceResponse()
    response.redirect(url_for('_data_services_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option1', methods=['GET', 'POST'])
def _start_3g_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_v_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para iniciar el servicio 3G." +
              "Presione 2 para iniciar el servicio de Internet." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/lan_menu3/ivr/hello_v', methods=['POST'])
def hello_v_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_starts_3g",
                      '2': "_starts_internet",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat23"}

    if int(selected_options) == 1:
        response = _starts_3g_3()
        return response
    elif int(selected_options) == 2:
        response = _starts_internet_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat23_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat23_3():
    response = VoiceResponse()
    response.redirect(url_for('_start_3g_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu7_3():
    response = VoiceResponse()
    response.redirect(url_for('_data_services_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option1/option1', methods=['GET', 'POST'])
def _starts_3g_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_w_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Su información de servicio para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_w', methods=['POST'])
def hello_w_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu8",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat24"}

    if int(selected_options) == 7:
        response = _prev_menu8_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat24_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat24_3():
    response = VoiceResponse()
    response.redirect(url_for('_starts_3g_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu8_3():
    response = VoiceResponse()
    response.redirect(url_for('_start_3g_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option1/option2', methods=['GET', 'POST'])
def _starts_internet_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_x_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Su información de servicio de Internet para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_x', methods=['POST'])
def hello_x_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu8",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat25"}

    if int(selected_options) == 7:
        response = _prev_menu8_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat25_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat25_3():
    response = VoiceResponse()
    response.redirect(url_for('_starts_internet_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option2', methods=['GET', 'POST'])
def _stop_3g_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_y_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para detener el servicio 3G." +
              "Presione 2 para detener el servicio de Internet." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_y', methods=['GET', 'POST'])
def hello_y_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_stops_3g",
                      '2': "_stops_internet",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat26"}

    if int(selected_options) == 1:
        response = _stops_3g_3()
        return response
    elif int(selected_options) == 2:
        response = _stops_internet_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat26_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat26_3():
    response = VoiceResponse()
    response.redirect(url_for('_stop_3g_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option2/option1', methods=['GET', 'POST'])
def _stops_3g_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_z_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Su información de servicio para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_z', methods=['POST'])
def hello_z_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu9",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat27"}

    if int(selected_options) == 7:
        response = _prev_menu9_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat27_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat27_3():
    response = VoiceResponse()
    response.redirect(url_for('_stops_3g_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu9_3():
    response = VoiceResponse()
    response.redirect(url_for('_stop_3g_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option2/option2', methods=['GET', 'POST'])
def _stops_internet_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_aa_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Su información de servicio de Internet para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_aa', methods=['POST'])
def hello_aa_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu9",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat28"}

    if int(selected_options) == 7:
        response = _prev_menu9_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat28_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat28_3():
    response = VoiceResponse()
    response.redirect(url_for('_stops_internet_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option3', methods=['GET', 'POST'])
def _setting_3g_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_bb_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para configurar los servicios de Internet." +
              "Presione 2 para obtener la configuración de MMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_bb', methods=['POST'])
def hello_bb_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_setting_internet",
                      '2': "_setting_mms",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat29"}

    if int(selected_options) == 1:
        response = _setting_internet_3()
        return response
    elif int(selected_options) == 2:
        response = _setting_mms_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat29_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat29_3():
    response = VoiceResponse()
    response.redirect(url_for('_setting_3g_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option3/option1', methods=['GET', 'POST'])
def _setting_internet_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_cc_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Configuración de Internet para recibir a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_cc', methods=['POST'])
def hello_cc_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu10",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat30"}

    if int(selected_options) == 7:
        response = _prev_menu10_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat30_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat30_3():
    response = VoiceResponse()
    response.redirect(url_for('_setting_internet_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu10_3():
    response = VoiceResponse()
    response.redirect(url_for('_setting_3g_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option3/option2', methods=['GET', 'POST'])
def _setting_mms_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_dd_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Configuración de MMS para recibir a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_dd', methods=['POST'])
def hello_dd_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu10",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat31"}

    if int(selected_options) == 7:
        response = _prev_menu10_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat31_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat31_3():
    response = VoiceResponse()
    response.redirect(url_for('_setting_mms_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option4', methods=['GET', 'POST'])
def _info_dt_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ee_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para obtener información sobre el procedimiento de instalación." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_ee', methods=['POST'])
def hello_ee_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_inf_install",
                      '2': "_setting_mms",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat32"}

    if int(selected_options) == 1:
        response = _inf_install_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat32_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat32_3():
    response = VoiceResponse()
    response.redirect(url_for('_info_dt_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option4/option1', methods=['GET', 'POST'])
def _inf_install_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ff_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Para obtener información sobre cómo instalar la tarjeta de datos o Dongle con." +
              "Presione 1 para el sistema operativo Windows." +
              "Presione 2 para el sistema operativo Linux." +
              "Presione 3 para Macbook"
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_ff', methods=['POST'])
def hello_ff_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_system_os",
                      '2': "_system_linux",
                      '3': "_system_mac",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat33"}

    if int(selected_options) == 1:
        response = _system_os_3()
        return response
    elif int(selected_options) == 2:
        response = _system_linux_3()
        return response
    elif int(selected_options) == 3:
        response = _system_mac_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat33_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat33_3():
    response = VoiceResponse()
    response.redirect(url_for('_inf_install_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option4/option1_op1', methods=['GET', 'POST'])
def _system_os_3():
    response = VoiceResponse()
    response.say("Nuestros ejecutivos están ocupados en otra línea." +
                 "Lo llamaremos pronto.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option4/option1_op2', methods=['GET', 'POST'])
def _system_linux_3():
    response = VoiceResponse()
    response.say("Nuestros ejecutivos están ocupados en otra línea." +
                 "Lo llamaremos pronto.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option4/option1_op3', methods=['GET', 'POST'])
def _system_mac_3():
    response = VoiceResponse()
    response.say("Nuestros ejecutivos están ocupados en otra línea." +
                 "Lo llamaremos pronto.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option5', methods=['GET', 'POST'])
def _info_pc_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_gg_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Para obtener información sobre cómo conectarse." +
              "Presione 1 para PC a través de bluetooth." +
              "Presione 2 para PC a través de infrarrojos." +
              "Presione 3 para PC a través de Cable." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_gg', methods=['GET', 'POST'])
def hello_gg_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_bluetooth_pc",
                      '2': "_infrared_pc",
                      '3': "_cable_pc",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat34"}

    if int(selected_options) == 1:
        response = _bluetooth_pc_3()
        return response
    elif int(selected_options) == 2:
        response = _infrared_pc_3()
        return response
    elif int(selected_options) == 3:
        response = _cable_pc_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat34_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat34_3():
    response = VoiceResponse()
    response.redirect(url_for('_info_pc_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option5/option1', methods=['GET', 'POST'])
def _bluetooth_pc_3():
    response = VoiceResponse()
    response.say("Nuestros ejecutivos están ocupados en otra línea." +
                 "¡¡¡Espere por favor!!!", voice=female, language=spaines)
    response.dial(number=executive_number, caller_id=cides)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option5/option2', methods=['GET', 'POST'])
def _infrared_pc_3():
    response = VoiceResponse()
    response.say("Nuestros ejecutivos están ocupados en otra línea." +
                 "¡¡¡Espere por favor!!!", voice=female, language=spaines)
    response.dial(number=executive_number, caller_id=cides)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option5/option3', methods=['GET', 'POST'])
def _cable_pc_3():
    response = VoiceResponse()
    response.say("Nuestros ejecutivos están ocupados en otra línea." +
                 "¡¡¡Espere por favor!!!", voice=female, language=spaines)
    response.dial(number=executive_number, caller_id=cides)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option6', methods=['GET', 'POST'])
def _ques_3g_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_hh_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para cualquier pregunta." +
              "Presione 2 para obtener ayuda técnica." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_hh', methods=['POST'])
def hello_hh_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_ques_any",
                      '2': "_technical_help",
                      '7': "_prev_menu7",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat35"}

    if int(selected_options) == 1:
        response = _ques_any_3()
        return response
    elif int(selected_options) == 2:
        response = _technical_help_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu7_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat35_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat35_3():
    response = VoiceResponse()
    response.redirect(url_for('_ques_3g_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option6/option1', methods=['GET', 'POST'])
def _ques_any_3():
    response = VoiceResponse()
    response.say("Nuestros ejecutivos están ocupados en otra línea." +
                 "¡¡¡Espere por favor!!!" +
                 "Llame de nuevo más tarde.", voice=female, language=spaines)
    response.dial(number=executive_number, caller_id=cides)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option5/option6/option2', methods=['GET', 'POST'])
def _technical_help_3():
    response = VoiceResponse()
    response.say("Nuestro equipo técnico está ocupado en otra línea." +
                 "¡¡¡Espere por favor!!!" +
                 "Llame de nuevo más tarde.", voice=female, language=spaines)
    response.dial(number=technician_number, caller_id=cides)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_ii', methods=['POST'])
def hello_ii_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_Roaming",
                      '2': "_postpaid",
                      '3': "_change",
                      '4': "_for_mnp",
                      '5': "_ques_fix",
                      '6': "_ques_any",
                      '7': "_prev_menu1",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat36"}

    if int(selected_options) == 1:
        response = _Roaming_3()
        return response
    elif int(selected_options) == 2:
        response = _postpaid_3()
        return response
    elif int(selected_options) == 3:
        response = _change_3()
        return response
    elif int(selected_options) == 4:
        response = _for_mnp_3()
        return response
    elif int(selected_options) == 5:
        response = _ques_fix_3()
        return response
    elif int(selected_options) == 6:
        response = _ques_any_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu1_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat36_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat36_3():
    response = VoiceResponse()
    response.redirect(url_for('_any_question_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option1', methods=['GET', 'POST'])
def _Roaming_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_jj_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para Roaming nacional." +
              "Presione 2 para obtener información sobre roaming internacional." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_jj', methods=['GET', 'POST'])
def hello_jj_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_national_roaming",
                      '2': "_international_roaming",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat37"}

    if int(selected_options) == 1:
        response = _national_roaming_3()
        return response
    elif int(selected_options) == 2:
        response = _international_roaming_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat37_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat37_3():
    response = VoiceResponse()
    response.redirect(url_for('_Roaming_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu11_3():
    response = VoiceResponse()
    response.redirect(url_for('_any_question_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option1/option1', methods=['GET', 'POST'])
def _national_roaming_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ll_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Su información de roaming nacional para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_ll', methods=['POST'])
def hello_ll_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu12",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat38"}

    if int(selected_options) == 7:
        response = _prev_menu12_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat38_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat38_3():
    response = VoiceResponse()
    response.redirect(url_for('_national_roaming_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu12_3():
    response = VoiceResponse()
    response.redirect(url_for('_Roaming_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option1/option2', methods=['GET', 'POST'])
def _international_roaming_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_kk_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Su información de roaming internacional para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_kk', methods=['POST'])
def hello_kk_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu12",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat39"}

    if int(selected_options) == 7:
        response = _prev_menu12_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat39_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat39_3():
    response = VoiceResponse()
    response.redirect(url_for('_international_roaming_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option2', methods=['GET', 'POST'])
def _postpaid_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_mm_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para preguntas relacionadas con pospago." +
              "Presione 2 para preguntas relacionadas con prepago a pospago." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_mm', methods=['POST'])
def hello_mm_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_question_postpaid",
                      '2': "_prepaid_postpaid",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat40"}

    if int(selected_options) == 1:
        response = _question_postpaid_3()
        return response
    elif int(selected_options) == 2:
        response = _prepaid_postpaid_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat40_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat40_3():
    response = VoiceResponse()
    response.redirect(url_for('_postpaid_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option2/option1', methods=['GET', 'POST'])
def _question_postpaid_3():
    response = VoiceResponse()
    response.say("Estamos transfiriendo su llamada a Customer Executive." +
                 "¡¡¡Espere por favor!!! Nuestros ejecutivos están ocupados en otra línea.", voice=female, language=spaines)
    response.dial(number=executive_number, caller_id=cides)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option2/option2', methods=['GET', 'POST'])
def _prepaid_postpaid_3():
    response = VoiceResponse()
    response.say("Estamos transfiriendo su llamada a Customer Executive." +
                 "¡¡¡Espere por favor!!! Nuestros ejecutivos están ocupados en otra línea.", voice=female, language=spaines)
    response.dial(number=executive_number, caller_id=cides)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option3', methods=['GET', 'POST'])
def _change_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_nn_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para cambiar su idioma." +
              "Presione 2 para cambiar TPIN." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_nn', methods=['POST'])
def hello_nn_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_change_language",
                      '2': "_change_tpin",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat41"}

    if int(selected_options) == 1:
        response = _change_language_3()
        return response
    elif int(selected_options) == 2:
        response = _change_tpin_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat41_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat41_3():
    response = VoiceResponse()
    response.redirect(url_for('_change_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option3/option1', methods=['GET', 'POST'])
def _change_language_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_oo_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Elige tu idioma." +
              "Presione 1 para inglés." +
              "Presione 2 para francés." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_oo', methods=['POST'])
def hello_oo_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_lan_en",
                      '2': "_lan_french",
                      '7': "_prev_menu13",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat42"}

    if int(selected_options) == 1:
        response = _lan_en_3()
        return response
    elif int(selected_options) == 2:
        response = _lan_french_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu13_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat42_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat42_3():
    response = VoiceResponse()
    response.redirect(url_for('_change_language_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu13_3():
    response = VoiceResponse()
    response.redirect(url_for('_change_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option3/option1_op1', methods=['GET', 'POST'])
def _lan_en_3():
    response = VoiceResponse()
    response.say("English Language successfully updated." +
                 "Thank you for calling.", voice=female, language=uk)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option3/option1_op2', methods=['GET', 'POST'])
def _lan_french_3():
    response = VoiceResponse()
    response.say("Langue française mise à jour avec succès." +
                 "Merci de votre appel.", voice=female, language=france)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option3/option2', methods=['GET', 'POST'])
def _change_tpin_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_pp_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para ingresar su TPIN." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_pp', methods=['POST'])
def hello_pp_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_enter_tpin",
                      '7': "_prev_menu12",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat43"}

    if int(selected_options) == 1:
        response = _enter_tpin_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu13_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat43_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat43_3():
    response = VoiceResponse()
    response.redirect(url_for('_change_tpin_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option3/option2_op1', methods=['GET', 'POST'])
def _enter_tpin_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=4, action=url_for('hello_qq_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Ingrese su TPIN." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_qq', methods=['POST'])
def hello_qq_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu13",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat43"}

    if int(selected_options) == 7:
        response = _prev_menu13_3()
        return response
    elif int(selected_options) == 2580:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 1472:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat43_3()
        return response
    else:
        return _redirect_welcome_3()


@app.route('/ivr/lan_menu3/option6/option4', methods=['GET', 'POST'])
def _for_mnp_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_rr_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para obtener información sobre MNP." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_rr', methods=['POST'])
def hello_rr_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_info_mnp",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat44"}

    if int(selected_options) == 1:
        response = _info_mnp_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat44_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat44_3():
    response = VoiceResponse()
    response.redirect(url_for('_for_mnp_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option4/option1', methods=['GET', 'POST'])
def _info_mnp_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_ss_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Su información de MNP para obtener esta información a través de SMS." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_ss', methods=['POST'])
def hello_ss_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'7': "_prev_menu14",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat45"}

    if int(selected_options) == 7:
        response = _prev_menu14_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat45_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat45_3():
    response = VoiceResponse()
    response.redirect(url_for('_info_mnp_3', _scheme='http', _external=True))
    return tiniyoml(response)


def _prev_menu14_3():
    response = VoiceResponse()
    response.redirect(url_for('_for_mnp_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option5', methods=['GET', 'POST'])
def _ques_fix_3():
    response = VoiceResponse()
    with response.gather(
            num_digits=1, action=url_for('hello_tt_3', _scheme='http', _external=True), method="POST"
    ) as g:
        g.say("Presione 1 para el servicio de línea fija Tiniyo." +
              "Presione 2 para el servicio de TV digital Tiniyo." +
              "Para volver al menú anterior presione 7." +
              "Para volver al menú principal presione 8." +
              "Para Tiniyo Executive presione 9." +
              "Para repetir presione 0.", voice=male, language=spaines, loop=3)
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/hello_tt', methods=['POST'])
def hello_tt_3():
    app.logger.error("DTMFGathertime response = %s" % request.get_json())
    selected_options = 0
    if request.get_json() is not None:
        if 'Digits' in request.get_json():
            selected_options = request.json.get('Digits')
    # selected_options = request.form['digits']
    option_actions = {'1': "_line_fixed",
                      '2': "_digital_tv",
                      '7': "_prev_menu11",
                      '8': "_main_menu1",
                      '9': "_call_to_ex",
                      '0': "_repeat46"}

    if int(selected_options) == 1:
        response = _line_fixed_3()
        return response
    elif int(selected_options) == 2:
        response = _digital_tv_3()
        return response
    elif int(selected_options) == 7:
        response = _prev_menu11_3()
        return response
    elif int(selected_options) == 8:
        response = _main_menu1_3()
        return response
    elif int(selected_options) == 9:
        response = _call_to_ex_3()
        return response
    elif int(selected_options) == 0:
        response = _repeat46_3()
        return response
    else:
        return _redirect_welcome_3()


def _repeat46_3():
    response = VoiceResponse()
    response.redirect(url_for('_ques_fix_3', _scheme='http', _external=True))
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option5/option1', methods=['GET', 'POST'])
def _line_fixed_3():
    response = VoiceResponse()
    response.say("Información de los servicios de línea fija de Tiniyo para obtener a través de SMS." +
                 "Gracias por llamar.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


@app.route('/ivr/lan_menu3/option6/option5/option2', methods=['GET', 'POST'])
def _digital_tv_3():
    response = VoiceResponse()
    response.say("Tiniyo Información de televisión digital para recibir a través de SMS." +
                 "Gracias por llamar.", voice=female, language=spaines)
    response.hangup()
    return tiniyoml(response)


if __name__ == '__main__':
    app.run()
