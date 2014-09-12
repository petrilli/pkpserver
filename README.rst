===============================
PKP Server
===============================

.. image:: https://badge.fury.io/py/pkpserver.png
    :target: http://badge.fury.io/py/pkpserver

.. image:: https://travis-ci.org/petrilli/pkpserver.png?branch=master
        :target: https://travis-ci.org/petrilli/pkpserver

.. image:: https://pypip.in/d/pkpserver/badge.png
        :target: https://pypi.python.org/pypi/pkpserver


PKP Server to provide end-point collection of Public Key Pinning Extensions
for HTTP. `Public Key Pinning`_ is an Internet Engineering Taskforce (IETF)
proposed standard that allows an HTTP client to ensure that it is still
talking to the correct server. The working group describes the effort as:

  [...] an extension to the HTTP protocol allowing web host operators to
  instruct user agents to remember ("pin") the hosts' cryptographic
  identities for a given period of time.  During that time, UAs will require
  that the host present a certificate chain including at least one Subject
  Public Key Info structure whose fingerprint matches one of the pinned
  fingerprints for that host.  By effectively reducing the number of
  authorities who can authenticate the domain during the lifetime of the pin,
  pinning may reduce the incidence of man-in-the-middle attacks due to
  compromised Certification Authorities.

This project provides a server for reporting Pin Validation failures, tracking
them, and will eventually provide reporting as well.

* Free software: BSD license
* Documentation: https://pkpserver.readthedocs.org.

Features
--------

* TODO

.. _Public Key Pinning: https://datatracker.ietf.org/doc/draft-ietf-websec-key-pinning/
