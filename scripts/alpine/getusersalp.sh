#!bin/sh

#mymac:x:1000:1000:juggernaut,,,:/home/mymac:/bin/bash
#|     |  |    |    |             |             |
#|     |  |    |    |             |             Login shell
#|     |  |    |    |             Home directory
#|     |  |    |    GECOS fields (full name, etc.)
#|     |  |    Primary Group id
#|     |  User ID
#|     Encrypted password indicator
#Username


getent passwd
