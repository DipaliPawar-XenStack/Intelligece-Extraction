import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='Iel',  
     version='0.1',
     scripts=['Iel'] ,
     author="Dipali Pawar",
     author_email="dipalip182@gmail.com",
     description="package",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )