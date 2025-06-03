# cisco-wsa-to-fortigate-converter
Cisco Secure Web Appliance to FortiGate Converter

This is work in progress tested with on a Cisco Web Security Appliance/WSA config xml Version: 15.0

## Documentation

Relevant section on the Fortinet documentation


https://docs.fortinet.com/document/fortigate/7.4.8/cli-reference/333203621/config-webfilter-urlfilter

```
config webfilter urlfilter
    edit 1
        set name "webfilter-urlfilter_name"
        config entries
            edit 1
                set url "www.constoso.com"
                set action block
            next
        end
    next
end

## Not supported features

tunnel:// URLs are not supported on FortiGate and needs to be adjusted manually
