
# I can Create use Define Exception by Extending to Exception Class

class WrongDivisionException(Exception):
    """Exception raised for errors in case division is invalid """
    def __init__(self, message=None):
        self.message = message
        # super().__init__(self.message)


class DBConnectionException(Exception):
    """Exception raised for errors in case DB connection is poor"""
    def __init__(self, message=None):
        self.message = message
        # super().__init__(self.message)
