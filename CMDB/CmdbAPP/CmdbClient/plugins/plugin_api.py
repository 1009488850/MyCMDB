
from CmdbAPP.CmdbClient.plugins.linux import sysinfo




def LinuxSysInfo():
    #print __file__
    return  sysinfo.collect()


def WindowsSysInfo():
    from CmdbAPP.CmdbClient.plugins.windows import sysinfo as win_sysinfo
    return win_sysinfo.collect()
