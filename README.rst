django-wkhtmltoimage
==================

Converts HTML to PDF
--------------------

Provides Django views to wrap the HTML to Image conversion of the `wkhtmltoimage <http://wkhtmltopdf.org>`_ binary.

Requirements
------------

Install the `wkhtmltopdf static binary <http://wkhtmltopdf.org/downloads.html>`_.

This requires libfontconfig (on Ubuntu: ``sudo aptitude install libfontconfig``).

Python 2.6+ and 3.3+ are supported.


Installation
------------

Run ``pip install django-wkhtmltoimage``.

Add ``'wkhtmltoimage'`` to ``INSTALLED_APPS`` in your ``settings.py``.

By default it will execute the first ``wkhtmltoimage`` command found on your ``PATH``.

If you can't add wkhtmltoimage to your ``PATH``, you can set ``WKHTMLTOIMAGE_CMD`` to a
specific executable:

e.g. in ``settings.py``: ::

    WKHTMLTOIMAGE_CMD = '/path/to/my/wkhtmltoimage'

or alternatively as env variable: ::

    export WKHTMLTOPDF_CMD=/path/to/my/wkhtmltoimage

You may also set ``WKHTMLTOIMAGE_OPTIONS`` in ``settings.py`` to a dictionary
of default command-line options.

The default is: ::

    WKHTMLTOIMAGE_OPTIONS = {
        'quiet': True,
        'quiet': True,
    	'format': 'png'
    }
    
 
 You may set font path for missing font files
    
 WKHTMLTOIMAGE_ENV = {'FONTCONFIG_PATH': '/path/to/my/fonts'}

 You can also set Debug option for detail errors
 
 WKHTMLTOIMAGE_DEBUG = (True/False)
 
 The default is: :: settings.DEBUg

Usage
-------
  
  from wkhtmltoimage.views import ImageTemplateView
 
  class ProfileImageView(ImageTemplateView):
  	 filename = 'text.png'
  	 template_name = 'template_image.html'
 

License
-------

MIT licensed. 
