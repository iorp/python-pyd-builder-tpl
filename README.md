python setup.py build_ext --build-lib ./build


# MyLibrary

MyLibrary is a Python library that contains Cython modules organized into packages.

## Installation

You can install MyLibrary using pip:

```bash
pip install mylibrary
```

## Compilation

To compile the Cython modules, follow these steps:

1. Ensure you have the required dependencies installed, including Cython.

2. Navigate to the `mylibrary` directory where this README file is located.

3. Run the following command to compile the Cython modules and create the library:

```bash
python setup.py build_ext --inplace
```

4. After running the above command, the Cython modules will be compiled and placed in the `mylibrary` directory. You can import the modules as follows:

```python
from mylibrary import mymodule1, mymodule2
```

That's it! You have successfully compiled the Cython modules and can now use them within your Python projects.

## Usage

You can use the compiled Cython modules in your Python code as follows:

```python
from mylibrary import mymodule1, mymodule2

# Use mymodule1 and mymodule2 in your code
```

## License

This library is provided under the XYZ License. See the LICENSE file for more details.
```
You should replace "MyLibrary" with your library's name and customize the installation, compilation, and usage instructions as needed. Additionally, make sure to include any specific licensing information in the "License" section and create a LICENSE file in your project if necessary.


Create a wheel 

# Install wheel  
```shell  
pip install wheel 
```

# Build library in dist folder
```shell 
# DEPRECATED: python setup.py build_ext --build-lib ./dist
pip wheel --no-deps -w dist . 

```
