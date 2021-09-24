import re


def test_phones_on_home_page(app):
    user_from_home_page = app.user.get_user_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)


def test_all_data_on_home_page(app):
    user_from_home_page = app.user.get_user_list()[0]
    user_from_edit_page = app.user.get_user_info_from_edit_page(0)
    assert user_from_home_page.id == user_from_edit_page.id
    assert user_from_home_page.lastname == user_from_edit_page.lastname
    assert user_from_home_page.firstname == user_from_edit_page.firstname
    assert user_from_home_page.address == user_from_edit_page.address
    assert user_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(user_from_edit_page)
    assert user_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(user_from_edit_page)


def merge_address_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [user.address]))))


def merge_emails_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear_email(x),
                                filter(lambda x: x is not None,
                                [user.email, user.email2, user.email3]))))


def merge_phones_like_on_home_page(user):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                [user.home, user.mobile, user.work, user.phone2]))))


def clear(s):
    return re.sub("[() -]", "", s)


def clear_email(s):
    return re.sub("[ ]", "", s)


# def test_phones_on_user_view_page(app):
#     user_from_view_page = app.user.get_user_from_view_page(0)
#     user_from_edit_page = app.user.get_user_info_from_edit_page(0)
#     assert user_from_view_page.merge_phones_like_on_view_page == merge_phones_like_on_home_page(user_from_edit_page)


# def merge_phones_like_on_view_page(user):
#     return "\n".join(filter(lambda x: x != "",
#                             map(lambda x: clear(x),
#                                 filter(lambda x: x is not None,
#                                 [user.home, user.mobile, user.work, user.phone2]))))
