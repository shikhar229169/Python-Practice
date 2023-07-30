# User defined error
class healthFactorError(Exception):
    def __init__(self, message, healthFactor):
        self.message = message
        self.healthFactor = healthFactor

    def __str__(self):
        return f'\nMessage: {self.message}\nhealthFactor: {healthFactor}'
    


healthFactor = 7.4
if healthFactor >= 1:
    raise healthFactorError("Health Factor Is Good.", healthFactor)