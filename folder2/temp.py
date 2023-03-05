import sys

server_no = ["5", "9"]
max_assoc_time = 4800
max_disassoc_time = 4800
mac_pool_block_start = '00:25:B5:00:FF:30'
mac_pool_block_end = '00:25:B5:00:FF:9E'

# temp1 = ["hyhuyhyuh"]
sys.path.append("/home/gaurang")

downgrade_build_list = [
    {
        "A": {
            "build" : "4.2(2.77)A",
            "link" : "https://cspg-releng.cisco.com/ucs-b-series/kellerbeach_mr2-builds/221009-104039_4_2_2_d84_77A_56B_56C/Images.d84_77A_56B_56C/ucs-6300-k9-bundle-infra.4.2.2.77.A.gbin"
        },
        "C" : {
            "build" : "4.2(2.56)C",
            "link" : "https://cspg-releng.cisco.com/ucs-b-series/kellerbeach_mr2-builds/221009-104039_4_2_2_d84_77A_56B_56C/Images.d84_77A_56B_56C/ucs-k9-bundle-c-series.4.2.2.56.C.gbin"
        }
    },
    {
        "A": {
            "build" :  "4.2(2c)A",
            "link" : "https://cspg-releng.cisco.com/ucs-b-series/kellerbeach_mr1-builds/220918-003014_4_2_2_p103_cA_cB_cC/Images.p103_cA_cB_cC/ucs-6300-k9-bundle-infra.4.2.2c.A.gbin"
        },
        "C" : {
            "build" : "4.2(2c)C", 
            "link" : "https://cspg-releng.cisco.com/ucs-b-series/kellerbeach_mr1-builds/220918-003014_4_2_2_p103_cA_cB_cC/Images.p103_cA_cB_cC/ucs-k9-bundle-c-series.4.2.2c.C.bin"
        }
    }
]

upgrade_build_list = [
    {
        "A": {
            "build" : "4.2(2.77)A",
            "link" : "https://cspg-releng.cisco.com/ucs-b-series/kellerbeach_mr2-builds/221009-104039_4_2_2_d84_77A_56B_56C/Images.d84_77A_56B_56C/ucs-6300-k9-bundle-infra.4.2.2.77.A.gbin"
        },
        "C" : {
            "build" : "4.2(2.56)C", 
            "link" : "https://cspg-releng.cisco.com/ucs-b-series/kellerbeach_mr2-builds/221009-104039_4_2_2_d84_77A_56B_56C/Images.d84_77A_56B_56C/ucs-k9-bundle-c-series.4.2.2.56.C.gbin"
        }
    },
    {
        "A": {
            "build" :  "4.2(2c)A",
            "link" : "https://cspg-releng.cisco.com/ucs-b-series/kellerbeach_mr1-builds/220918-003014_4_2_2_p103_cA_cB_cC/Images.p103_cA_cB_cC/ucs-6300-k9-bundle-infra.4.2.2c.A.gbin"
        },
        "C" : {
            "build" : "4.2(2c)C", 
            "link" : "https://cspg-releng.cisco.com/ucs-b-series/kellerbeach_mr1-builds/220918-003014_4_2_2_p103_cA_cB_cC/Images.p103_cA_cB_cC/ucs-k9-bundle-c-series.4.2.2c.C.bin"
        }
    },
]

excluded_hfp_component = [
    # 'adapter',
    # 'board-controller',
    # 'cimc',
    'flexflash-controller',
    'graphics-card',
    'host-hba',
    'host-hba-optionrom',
    'host-nic',
    'host-nic-optionrom',
    'nvme-mswitch-firmware',
    'pci-switch-firmware',
    # 'local-disk',
    'persistent-memory-dimm-firmware',
    'psu',
    'sas-expander',
    'sas-expander-regular-firmware',
    # 'server-bios', 
    'storage-controller',
    'storage-controller-onboard-device',
    'storage-controller-onboard-device-cpld',
    'storage-device-bridge'
    ]

scp_ip = "10.126.79.141"
scp_username ="ucsmrack"
scp_password = "nbv12345"
scp_folder = "/home/ucsmrack/gsanjayn/3g/"

