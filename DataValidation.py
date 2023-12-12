class DataValidator:
    def __init__(self):
        self.valid_integers = []

    def validate_inputs(self, user_inputs):

        if not isinstance(user_inputs, list):
            raise ValueError('Input must be strings')

        for user_input in user_inputs:
            try:
                value = int(user_input)
                if value > 0:
                    self.valid_integers.append(value)
            except ValueError:
                pass  # Ignore non-integer strings

        return self.valid_integers


if __name__ == '__main__':
    validator = DataValidator()
    user_inputs = ['12', '34', '56', 'abc', '-7', '89', '22', '27']

    valid_inputs = validator.validate_inputs(user_inputs)
    print('Valid Positive Integers:', valid_inputs)