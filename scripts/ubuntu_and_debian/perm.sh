#!/bin/bash

arr=(/etc/bash.bashrc /etc/hostname /etc/hosts /etc/init.d /etc/resolv.conf /etc/apt/sources.list /etc/security/ /proc/filesystems /proc/interrupts /proc/ioports /proc/modules /proc/stat /proc/swaps /etc/passwd /etc/group /sbin /usr/sbin)

for item in ${arr[*]}
do
    stat $item

done
