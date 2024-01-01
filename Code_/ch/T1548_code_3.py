import win32con
import win32com.shell.shell as shell

def abuse_elevation_control4():
    ASADMIN = 'asadmin'
    if sys.argv[-1] != ASADMIN:
        script = os.path.abspath(sys.argv[0])
        params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
        shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
        sys.exit(0)

abuse_elevation_control4()