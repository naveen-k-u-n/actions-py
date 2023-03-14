import os

my_env_var = os.environ.get('MY_ENV_VAR')
my_number_var = os.environ.get('MY_NUMBER_VAR')

print(f'MY_ENV_VAR = {my_env_var}')
print(f'MY_NUMBER_VAR = {my_number_var}')