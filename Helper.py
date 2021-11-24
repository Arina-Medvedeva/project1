class Helper:
    @staticmethod
    def format_phone(phone):
        if len(phone) <= 7:
            return Helper.format_home_phone(phone)
        else:
            return Helper.format_mobile_phone(phone)

    @staticmethod
    def format_mobile_phone(phone):
        return phone[1:1] + '8 (' + phone[1:4] + ') ' + phone[4:7] + '-' + phone[7:9] + '-' + phone[9:]

    @staticmethod
    def format_home_phone(phone):
        return phone[:3] + '-' + phone[3:5] + '-' + phone[5:]

    @staticmethod
    def correct_print(item):
        return print('ФИО:', item.name,'\n Дата рождения - возраст:', item.birthday_age,',\n Телефоны:', item.formatted_phones, '\n\n')