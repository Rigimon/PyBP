	John the Ripper password cracker.

John the Ripper is a fast password cracker, currently available for
many flavors of Unix (11 are officially supported, not counting
different architectures), Windows, DOS, BeOS, and OpenVMS (the latter
requires a contributed patch).  Its primary purpose is to detect weak
Unix passwords.  Besides several crypt(3) password hash types most
commonly found on various Unix flavors, supported out of the box are
Kerberos/AFS and Windows LM hashes, as well as DES-based tripcodes, plus
many more hashes and ciphers in "community enhanced" -jumbo versions
and/or with other contributed patches.


	How to install.

See INSTALL for information on installing John on your system.


	How to use.

To run John, you need to supply it with some password files and
optionally specify a cracking mode, like this, using the default order
of modes and assuming that "passwd" is a copy of your password file:

	john passwd

or, to restrict it to the wordlist mode only, but permitting the use
of word mangling rules:

	john --wordlist=password.lst --rules passwd

Cracked passwords will be printed to the terminal and saved in the
file called $JOHN/john.pot (in the documentation and in the
configuration file for John, "$JOHN" refers to John's "home
directory"; which directory it really is depends on how you installed
John).  The $JOHN/john.pot file is also used to not load password
hashes that you already cracked when you run John the next time.

To retrieve the cracked passwords, run:

	john --show passwd

While cracking, you can press any key for status, or 'q' or Ctrl-C to
abort the session saving its state to a file ($JOHN/john.rec by
default).  If you press Ctrl-C for a second time before John had a
chance to complete handling of your first Ctrl-C, John will abort
immediately without saving.  By default, the state is also saved every
10 minutes to permit for recovery in case of a crash.

To continue an interrupted session, run:

	john --restore

These are just the most essential things you can do with John.  For
a complete list of command line options and for more complicated usage
examples you should refer to OPTIONS and EXAMPLES, respectively.

Please note that "binary" (pre-compiled) distributions of John may
include alternate executables instead of just "john".  You may need to
choose the executable that fits your system best, e.g. "john-omp" to
take advantage of multiple CPUs and/or CPU cores.


	Features and performance.

John the Ripper is designed to be both feature-rich and fast.  It
combines several cracking modes in one program and is fully
configurable for your particular needs (you can even define a custom
cracking mode using the built-in compiler supporting a subset of C).
Also, John is available for several different platforms which enables
you to use the same cracker everywhere (you can even continue a
cracking session which you started on another platform).

Out of the box, John supports (and autodetects) the following Unix
crypt(3) hash types: traditional DES-based, "bigcrypt", BSDI extended
DES-based, FreeBSD MD5-based (also used on Linux and in Cisco IOS), and
OpenBSD Blowfish-based (now also used on some Linux distributions and
supported by recent versions of Solaris).  Also supported out of the box
are Kerberos/AFS and Windows LM (DES-based) hashes, as well as DES-based
tripcodes.

When running on Linux distributions with glibc 2.7+, John 1.7.6+
additionally supports (and autodetects) SHA-crypt hashes (which are
actually used by recent versions of Fedora and Ubuntu), with optional
OpenMP parallelization (requires GCC 4.2+, needs to be explicitly
enabled at compile-time by uncommenting the proper OMPFLAGS line near
the beginning of the Makefile).

Similarly, when running on recent versions of Solaris, John 1.7.6+
supports and autodetects SHA-crypt and SunMD5 hashes, also with
optional OpenMP parallelization (requires GCC 4.2+ or recent Sun Studio,
needs to be explicitly enabled at compile-time by uncommenting the
proper OMPFLAGS line near the beginning of the Makefile and at runtime
by setting the OMP_NUM_THREADS environment variable to the desired
number of threads).

John the Ripper Pro adds support for Windows NTLM (MD4-based) and Mac
OS X 10.4+ salted SHA-1 hashes.

"Community enhanced" -jumbo versions add support for many more password
hash types, including Windows NTLM (MD4-based), Mac OS X 10.4-10.6
salted SHA-1 hashes, Mac OS X 10.7 salted SHA-512 hashes, raw MD5 and
SHA-1, arbitrary MD5-based "web application" password hash types, hashes
used by SQL database servers (MySQL, MS SQL, Oracle) and by some LDAP
servers, several hash types used on OpenVMS, password hashes of the
Eggdrop IRC bot, and lots of other hash types, as well as many
non-hashes such as OpenSSH private keys, S/Key skeykeys files, Kerberos
TGTs, PDF files, ZIP (classic PKZIP and WinZip/AES) and RAR archives.

Unlike older crackers, John normally does not use a crypt(3)-style
routine.  Instead, it has its own highly optimized modules for different
hash types and processor architectures.  Some of the algorithms used,
such as bitslice DES, couldn't have been implemented within the crypt(3)
API; they require a more powerful interface such as the one used in
John.  Additionally, there are assembly language routines for several
processor architectures, most importantly for x86-64 and x86 with SSE2.


        Graphical User Interface (GUI).

There is an official GUI for John the Ripper: Johnny.

Despite the fact that Johnny is oriented onto core john, all basic
functionality is supposed to work in all versions, even Jumbo. So,
password could be loaded from file and cracked with different
options.

Johnny is a separate program, therefore, you need to have John the
Ripper installed in order to use it.

You could find more info about releases and Johnny on the wiki:

  http://openwall.info/wiki/john/johnny


	Documentation.

The rest of documentation is located in separate files, listed here in
the recommended order of reading:

* INSTALL - installation instructions
* OPTIONS - command line options and additional utilities
* MODES - cracking modes: what they are
* CONFIG (*) - how to customize
* RULES (*) - wordlist rules syntax
* EXTERNAL (*) - defining an external mode
* EXAMPLES - usage examples - strongly recommended
* FAQ - guess
* CHANGES (*) - history of changes
* CONTACT (*) - how to contact the author or otherwise obtain support
* CREDITS (*) - credits
* LICENSE - copyrights and licensing terms
* COPYING - GNU GPL version 2, as referenced by LICENSE above

(*) most users can safely skip these.

Happy reading!

$Owl: Owl/packages/john/john/doc/README,v 1.25 2013/05/30 00:22:14 solar Exp $
