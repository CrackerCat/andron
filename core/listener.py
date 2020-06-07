#!/usr/bin/env python3

#            ---------------------------------------------------
#                             Andron Framework                                
#            ---------------------------------------------------
#                  Copyright (C) <2020>  <Entynetproject>       
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

import core.helper as h

def start():
    lhost = input(h.info_general_raw("Local host: ")).strip(" ")
    while True:
        lport = input(h.info_general_raw("Local port: ")).strip(" ")
        if not lport:
            lport = 4444
        try:
            lport = int(lport)
        except ValueError:
            h.info_error("Invalid port, please enter a valid integer.")
            continue
        if lport < 1024:
            h.info_error("Invalid port, please enter a value >= 1024.")
            continue
        break
