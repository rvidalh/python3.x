from .validate import validate_val, validate_tiny_int
from .error import TinyIntError


def tiny_int(valor, call_back = None):
	try:
		if validate_val(valor) and validate_tiny_int(valor):
			return True
		else:
			raise TinyIntError()
	except TinyIntError as error:
		if call_back is not None:
			call_back()
		else:
			print(error)