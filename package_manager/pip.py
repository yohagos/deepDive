# Python PIP - Python Package Manager
import webbrowser

# PIP stands for Preferred installer program. We use pip to install different
# Python packages. Package is a Python module that can contain one or more modules
# or other packages. A module or modules that we can install to our application
# is a package. In programming, we do not have to write every utility program,
# instead we install packages and import them to our applications.


# import numpy
#
# print(numpy.version.version)
# lst = range(0,10)
# np_arr = numpy.array(lst)
# print(np_arr)
# print(len(np_arr))
#
# print(np_arr * 2)
# print(np_arr + 2)


# import pandas
#
# url_lists = [
#     'http://www.python.org',
#     'https://facebook.com',
#     'https://github.com/yohagos',
#     'https://google.com',
# ]
#
# for url in url_lists:
#     webbrowser.open_new_tab(url)

import requests # importing the request module

# url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt' # text from a website
#
# response = requests.get(url) # opening a network and fetching a data
# print(response)
# print(response.status_code) # status code, success:200
# print(response.headers)     # headers information
# print(response.text) # gives all the text from the page

# url = 'https://restcountries.eu/rest/v2/all'  # countries api
# response = requests.get(url)  # opening a network and fetching a data
# print(response) # response object
# print(response.status_code)  # status code, success:200
# countries = response.json()
# print(countries[:1])

from example import arithmetics


print(arithmetics.add_numbers(0,10,34,2,1234))
