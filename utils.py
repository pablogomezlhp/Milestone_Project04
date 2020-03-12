import bcrypt


def is_password_valid(request, login_user, password) -> bool:
    hashed_password = bcrypt.hashpw(password=request.form['password'].encode('utf-8'), 
                                    salt=login_user['password'].encode('utf-8')) 
    return hashed_password == login_user['password'].encode('utf-8')
