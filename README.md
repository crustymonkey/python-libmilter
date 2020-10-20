# python-libmilter #

## NO LONGER SUPPORTING
I'm no longer supporting this module at this time.  I will accept pull requests for fixes, but I'm no longer actively working on this project (and haven't for quite some time).  I haven't maintained mail servers in about 8 years (at the time of this addition), and therefore I don't have a great way of testing this module.  Again, I will continue to take pull requests for changes for this.

## INSTALL ##

1. If you have a .tar.gz, extract that first.

    tar -xvzf python-libmilter*.tar.gz

2. Now, just cd into the directory and install it

    cd python-libmilter*
    python setup.py install

That's it, that will install the the libmilter.py file into its proper place.
Do note that you can just drop libmilter.py into your project folder and use it that way too.  The whole point of this project is to maximize portability.

You can also install libmilter (python 2 version) using *pip* or *easy_install*

    pip install python-libmilter

## EXAMPLES ##
See the basic ForkFactory example in the "examples" directory.

## DOCUMENTATION ##

Please see [my wiki site](http://stuffivelearned.org/doku.php?id=programming:python:python-libmilter) for all the documentation on this library.

## POSTFIX INTEGRATION ##

Edit the `main.cf` [configuration file](https://www.postfix.org/postconf.5.html) with the following parameters and values:

```
milter_default_action = accept
smtpd_milters = inet:127.0.0.1:5000
non_smtpd_milters = inet:127.0.0.1:5000
milter_protocol = 6
milter_mail_macros = i {mail_addr} {client_addr} {client_name} {auth_authen} {auth_type}
```

## ISSUES ##
Please open a ticket on [github](https://github.com/crustymonkey/python-libmilter) if you encounter any issues or you have feature requests.

## CODE CONTRIBUTIONS ##
Please use the the "fork" and "pull request" mechanisms built into Github if
you wish to contribute code to the project.
