# usage : ssh hpcgw
Host hpcgw
 HostName hpcgw.op.umcutrecht.nl
 User ejoly
 IdentityFile ~/.ssh/id_rsa_hpc
# usage : ssh gw2hpcs03
Host gw2hpcs03
 HostName hpcs03.op.umcutrecht.nl
 User ejoly
 ProxyCommand ssh -i ~/.ssh/id_rsa_hpc -l ejoly hpcgw.op.umcutrecht.nl nc %h %p 2>/dev/null
# usage : ssh gw2hpcs04
Host gw2hpcs04
 HostName hpcs04.op.umcutrecht.nl
 User ejoly
 ProxyCommand ssh -i ~/.ssh/id_rsa_hpc -l ejoly hpcgw.op.umcutrecht.nl nc %h %p 2>/dev/null
# usage : ssh gw2hpcs05
Host gw2hpcs05
 HostName hpcs05.op.umcutrecht.nl
 User ejoly
 ProxyCommand ssh -i ~/.ssh/id_rsa_hpc -l ejoly hpcgw.op.umcutrecht.nl nc %h %p 2>/dev/null
# usage : ssh gw2hpcs06
Host gw2hpcs06
 HostName hpcs06.op.umcutrecht.nl
 User ejoly
 ProxyCommand ssh -i ~/.ssh/id_rsa_hpc -l ejoly hpcgw.op.umcutrecht.nl nc %h %p 2>/dev/null
# usage : ssh gw2hpct01
Host gw2hpct01
 HostName hpct01.op.umcutrecht.nl
 User ejoly
 ProxyCommand ssh -i ~/.ssh/id_rsa_hpc -l ejoly hpcgw.op.umcutrecht.nl nc %h %p 2>/dev/null
# usage : ssh gw2hpct02
Host gw2hpct02
 HostName hpct02.op.umcutrecht.nl
 User ejoly
 ProxyCommand ssh -i ~/.ssh/id_rsa_hpc -l ejoly hpcgw.op.umcutrecht.nl nc %h %p 2>/dev/null
# usage : ssh gw2hpct03
Host gw2hpct03
 HostName hpct03.op.umcutrecht.nl
 User ejoly
 ProxyCommand ssh -i ~/.ssh/id_rsa_hpc -l ejoly hpcgw.op.umcutrecht.nl nc %h %p 2>/dev/null
# usage : ssh gw2hpct04
Host gw2hpct04
 HostName hpct04.op.umcutrecht.nl
 User ejoly
 ProxyCommand ssh -i ~/.ssh/id_rsa_hpc -l ejoly hpcgw.op.umcutrecht.nl nc %h %p 2>/dev/null
# usage : ssh hpcs03
Host hpcs03
 HostName hpcs03.op.umcutrecht.nl
 User ejoly
# usage : ssh hpcs03X
Host hpcs03X
 HostName hpcs03.op.umcutrecht.nl
 User ejoly
 ForwardX11 yes
# usage : ssh hpcs04
Host hpcs04
 HostName hpcs04.op.umcutrecht.nl
 User ejoly
# usage : ssh hpcs04X
Host hpcs04X
 HostName hpcs04.op.umcutrecht.nl
 User ejoly
 ForwardX11 yes
# usage : ssh hpct01
Host hpct01
 HostName hpct01.op.umcutrecht.nl
 User ejoly
# usage : ssh hpct02
Host hpct02
 HostName hpct02.op.umcutrecht.nl
 User ejoly
