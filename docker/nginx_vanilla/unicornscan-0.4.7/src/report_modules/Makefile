include ../../Makefile.inc

SUBDIRS=osdetect

all:
	@for g in $(SUBDIRS); do \
		cd $$g && /usr/bin/make all || exit 1 && cd ..; \
	done

clean:
	@for g in $(SUBDIRS); do \
		cd $$g && /usr/bin/make clean || exit 1 && cd ..; \
	done

distclean:
	@for g in $(SUBDIRS); do \
		cd $$g && /usr/bin/make distclean || exit 1 && cd ..; \
	done

install:
	@for g in $(SUBDIRS); do \
		cd $$g && /usr/bin/make install || exit 1 && cd ..; \
	done

uninstall:
	@for g in $(SUBDIRS); do \
		cd $$g && /usr/bin/make uninstall || exit 1 && cd ..; \
	done
