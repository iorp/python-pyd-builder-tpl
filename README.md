Create a wheel 

# Install wheel  
```shell 
# DEPRECATED: python setup.py build_ext --build-lib ./build
pip install wheel 
```

# Build library in dist folder
```shell 
# DEPRECATED: python setup.py build_ext --build-lib ./dist
pip wheel --no-deps -w dist . 

```