from setuptools import setup, find_packages

import wkhtmltoimage


setup(
    name='django-wkhtmltoimage',
    packages=find_packages(),
    include_package_data=True,
    version=wkhtmltoimage.__version__,
    description='Converts HTML to Image using wkhtmltoimage.',
    long_description=open('README.rst').read(),
    license='BSD-2-Clause',
    author=wkhtmltoimage.__author__,
    author_email='sanjumassal@gmail.com',
    url='https://github.com/sanjeevmassal/wkhtmltoimage',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    keywords='django wkhtmltoimage ',
)