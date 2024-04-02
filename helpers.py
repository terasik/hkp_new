import secrets
import string

def gen_passwd(length=20):
  """ generiere passwort """
  p = ''.join((secrets.choice(string.ascii_letters + string.digits) for i in range(length)))
  return p

def gen_random_string(length=6):
  return gen_passwd(length)
  
