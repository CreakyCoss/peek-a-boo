from . import auth


@auth.route('/login', methods=['GET', 'POST'])
def login():
    return ''
