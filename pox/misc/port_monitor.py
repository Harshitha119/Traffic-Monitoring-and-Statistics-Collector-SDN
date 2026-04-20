from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_PortStatus(event):
    port = event.ofp.desc.port_no
    reason = event.ofp.reason

    if reason == 0:
        status = "ADDED"
    elif reason == 1:
        status = "REMOVED"
    elif reason == 2:
        status = "MODIFIED"
    else:
        status = "UNKNOWN"

    log.info("Switch %s | Port %s changed status: %s",
             event.dpid, port, status)

def launch():
    core.openflow.addListenerByName("PortStatus", _handle_PortStatus)
    log.info("Port Status Monitoring Tool Started")
