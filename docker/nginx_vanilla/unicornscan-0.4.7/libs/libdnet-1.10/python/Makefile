# Makefile.in generated automatically by automake 1.4-p6 from Makefile.am

# Copyright (C) 1994, 1995-8, 1999, 2001 Free Software Foundation, Inc.
# This Makefile.in is free software; the Free Software Foundation
# gives unlimited permission to copy and/or distribute it,
# with or without modifications, as long as this notice is preserved.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY, to the extent permitted by law; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A
# PARTICULAR PURPOSE.



SHELL = /bin/sh

srcdir = .
top_srcdir = ..

prefix = /home/taran/Desktop/docker/nginx_vanilla/unicornscan-0.4.7/libs/libdnet-1.10/../fake
exec_prefix = ${prefix}

bindir = ${exec_prefix}/bin
sbindir = ${exec_prefix}/sbin
libexecdir = ${exec_prefix}/libexec
datadir = ${prefix}/share
sysconfdir = ${prefix}/etc
sharedstatedir = ${prefix}/com
localstatedir = ${prefix}/var
libdir = ${exec_prefix}/lib
infodir = ${prefix}/info
mandir = ${prefix}/man
includedir = ${prefix}/include
oldincludedir = /usr/include

DESTDIR =

pkgdatadir = $(datadir)/libdnet
pkglibdir = $(libdir)/libdnet
pkgincludedir = $(includedir)/libdnet

top_builddir = ..

ACLOCAL = /home/taran/Desktop/docker/nginx_vanilla/unicornscan-0.4.7/libs/libdnet-1.10/config/missing aclocal-1.4
AUTOCONF = /home/taran/Desktop/docker/nginx_vanilla/unicornscan-0.4.7/libs/libdnet-1.10/config/missing autoconf
AUTOMAKE = /home/taran/Desktop/docker/nginx_vanilla/unicornscan-0.4.7/libs/libdnet-1.10/config/missing automake-1.4
AUTOHEADER = /home/taran/Desktop/docker/nginx_vanilla/unicornscan-0.4.7/libs/libdnet-1.10/config/missing autoheader

INSTALL = /usr/bin/install -c
INSTALL_PROGRAM = ${INSTALL} $(AM_INSTALL_PROGRAM_FLAGS)
INSTALL_DATA = ${INSTALL} -m 644
INSTALL_SCRIPT = ${INSTALL}
transform = s,x,x,

NORMAL_INSTALL = :
PRE_INSTALL = :
POST_INSTALL = :
NORMAL_UNINSTALL = :
PRE_UNINSTALL = :
POST_UNINSTALL = :
host_alias = x86_64-unknown-linux-gnu
host_triplet = x86_64-unknown-linux-gnu
AR = ar
AS = @AS@
CC = gcc
CHECKINC = 
CHECKLIB = 
CXX = g++
CXXCPP = g++ -E
DLLTOOL = @DLLTOOL@
ECHO = printf %s\n
EGREP = grep -E
EXEEXT = 
F77 = 
GCJ = @GCJ@
GCJFLAGS = @GCJFLAGS@
LIBTOOL = $(SHELL) $(top_builddir)/libtool
LN_S = ln -s
LTLIBOBJS =  strlcat.lo strlcpy.lo arp-ioctl.lo eth-linux.lo fw-none.lo intf.lo ip.lo route-linux.lo tun-linux.lo
MAINT = #
MAKEINFO = /home/taran/Desktop/docker/nginx_vanilla/unicornscan-0.4.7/libs/libdnet-1.10/config/missing makeinfo
OBJDUMP = @OBJDUMP@
OBJEXT = o
PACKAGE = libdnet
PYTHON = 
RANLIB = ranlib
RC = @RC@
STRIP = strip
TCLINC = 
TCLLIB = 
VERSION = 1.10
ac_aux_dir = config

AUTOMAKE_OPTIONS = foreign no-dependencies

INCLUDES = -I$(top_srcdir)/include

DISTCLEANFILES = *~

# XXX - nasty automake fudging here...

#noinst_SCRIPTS = python-build

#TESTS = test.py

EXTRA_DIST = dnet.pyx dnet.c setup.py.in test.py
mkinstalldirs = $(SHELL) $(top_srcdir)/config/mkinstalldirs
CONFIG_HEADER = ../include/config.h
CONFIG_CLEAN_FILES =  setup.py
SCRIPTS =  $(noinst_SCRIPTS)

DIST_COMMON =  README Makefile.am Makefile.in setup.py.in


DISTFILES = $(DIST_COMMON) $(SOURCES) $(HEADERS) $(TEXINFOS) $(EXTRA_DIST)

TAR = tar
GZIP_ENV = --best
all: all-redirect
.SUFFIXES:
$(srcdir)/Makefile.in: # Makefile.am $(top_srcdir)/configure.in $(ACLOCAL_M4) $(top_srcdir)/Makefile.am.common
	cd $(top_srcdir) && $(AUTOMAKE) --foreign python/Makefile

Makefile: $(srcdir)/Makefile.in  $(top_builddir)/config.status
	cd $(top_builddir) \
	  && CONFIG_FILES=$(subdir)/$@ CONFIG_HEADERS= $(SHELL) ./config.status

setup.py: $(top_builddir)/config.status setup.py.in
	cd $(top_builddir) && CONFIG_FILES=$(subdir)/$@ CONFIG_HEADERS= $(SHELL) ./config.status
tags: TAGS
TAGS:


distdir = $(top_builddir)/$(PACKAGE)-$(VERSION)/$(subdir)

subdir = python

distdir: $(DISTFILES)
	@for file in $(DISTFILES); do \
	  d=$(srcdir); \
	  if test -d $$d/$$file; then \
	    cp -pr $$d/$$file $(distdir)/$$file; \
	  else \
	    test -f $(distdir)/$$file \
	    || ln $$d/$$file $(distdir)/$$file 2> /dev/null \
	    || cp -p $$d/$$file $(distdir)/$$file || :; \
	  fi; \
	done
check-TESTS: $(TESTS)
	@failed=0; all=0; \
	srcdir=$(srcdir); export srcdir; \
	for tst in $(TESTS); do \
	  if test -f $$tst; then dir=.; \
	  else dir="$(srcdir)"; fi; \
	  if $(TESTS_ENVIRONMENT) $$dir/$$tst; then \
	    all=`expr $$all + 1`; \
	    echo "PASS: $$tst"; \
	  elif test $$? -ne 77; then \
	    all=`expr $$all + 1`; \
	    failed=`expr $$failed + 1`; \
	    echo "FAIL: $$tst"; \
	  fi; \
	done; \
	if test "$$failed" -eq 0; then \
	  banner="All $$all tests passed"; \
	else \
	  banner="$$failed of $$all tests failed"; \
	fi; \
	dashes=`echo "$$banner" | sed s/./=/g`; \
	echo "$$dashes"; \
	echo "$$banner"; \
	echo "$$dashes"; \
	test "$$failed" -eq 0
info-am:
info: info-am
dvi-am:
dvi: dvi-am
check-am: all-am
	$(MAKE) $(AM_MAKEFLAGS) check-TESTS
check: check-am
installcheck-am:
installcheck: installcheck-am
install-exec-am: install-exec-local
install-exec: install-exec-am

install-data-am:
install-data: install-data-am

install-am: all-am
	@$(MAKE) $(AM_MAKEFLAGS) install-exec-am install-data-am
install: install-am
uninstall-am:
uninstall: uninstall-am
all-am: Makefile $(SCRIPTS)
all-redirect: all-am
install-strip:
	$(MAKE) $(AM_MAKEFLAGS) AM_INSTALL_PROGRAM_FLAGS=-s install
installdirs:


mostlyclean-generic:

clean-generic:

distclean-generic:
	-rm -f Makefile $(CONFIG_CLEAN_FILES)
	-rm -f config.cache config.log stamp-h stamp-h[0-9]*
	-test -z "$(DISTCLEANFILES)" || rm -f $(DISTCLEANFILES)

maintainer-clean-generic:
mostlyclean-am:  mostlyclean-generic

mostlyclean: mostlyclean-am

clean-am:  clean-generic mostlyclean-am

clean: clean-am

distclean-am:  distclean-generic clean-am
	-rm -f libtool

distclean: distclean-am

maintainer-clean-am:  maintainer-clean-generic distclean-am
	@echo "This command is intended for maintainers to use;"
	@echo "it deletes files that may require special tools to rebuild."

maintainer-clean: maintainer-clean-am

.PHONY: tags distdir check-TESTS info-am info dvi-am dvi check check-am \
installcheck-am installcheck install-exec-local install-exec-am \
install-exec install-data-am install-data install-am install \
uninstall-am uninstall all-redirect all-am all installdirs \
mostlyclean-generic distclean-generic clean-generic \
maintainer-clean-generic clean mostlyclean distclean maintainer-clean


#$(srcdir)/dnet.c: $(srcdir)/dnet.pyx
#	pyrexc $(srcdir)/dnet.pyx

#python-build: $(srcdir)/dnet.c
#	$(PYTHON) setup.py build
#	touch python-build

#python-clean:
#	rm -rf *build

#clean: python-clean

#distclean: clean

#python-install:
#	$(PYTHON) setup.py install --prefix=$(DESTDIR)$(prefix)

#install-exec-local: python-install

install-exec-local:

# Tell versions [3.59,3.63) of GNU make to not export all variables.
# Otherwise a system limit (for SysV at least) may be exceeded.
.NOEXPORT:
