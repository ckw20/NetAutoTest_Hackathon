#!/bin/sh
# -*- tcl -*-
# The next line is executed by /bin/sh, but not tcl \
exec tclsh "$0" ${1+"$@"}

package require http 2.0
package require base64
package require tls

#enable TLS
tls::init -tls1 true -ssl2 false -ssl3 false

#enable HTTPS
::http::register https 443 ::tls::socket

set host "192.168.41.99"
set port "8000"

set username "admin"
set password "admin"

#set authentication header
set auth "Basic [base64::encode $username:$password]"
set auth_header [list Authorization $auth]

set base_url https://$host:$port
set url $base_url/api/filters

set tok [::http::geturl $url -headers $auth_header]

set result_code [ ::http::code $tok]
puts "Result code = $result_code"
puts [::http::data $tok]
http::cleanup $tok