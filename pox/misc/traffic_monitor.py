from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.util import dpid_to_str
from pox.lib.recoco import Timer

log = core.getLogger()

# MAC learning table
mac_to_port = {}

def _handle_ConnectionUp(event):
    log.info("Switch %s connected", dpid_to_str(event.dpid))
    mac_to_port[event.dpid] = {}

    # Start periodic stats request
    Timer(5, request_stats, recurring=True)

def request_stats():
    for connection in core.openflow._connections.values():
        connection.send(of.ofp_stats_request(
            body=of.ofp_flow_stats_request()
        ))

def _handle_PacketIn(event):
    packet = event.parsed
    dpid = event.connection.dpid
    in_port = event.port

    if not packet.parsed:
        return

    # Learn MAC address
    mac_to_port[dpid][packet.src] = in_port

    if packet.dst in mac_to_port[dpid]:
        out_port = mac_to_port[dpid][packet.dst]
    else:
        out_port = of.OFPP_FLOOD

    # Install flow rule
    msg = of.ofp_flow_mod()
    msg.match = of.ofp_match.from_packet(packet)
    msg.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(msg)

    # Send packet
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=out_port))
    event.connection.send(msg)

def _handle_FlowStatsReceived(event):
    log.info("Flow stats from %s", dpid_to_str(event.connection.dpid))
    for flow in event.stats:
        log.info("Packets: %d | Bytes: %d",
                 flow.packet_count,
                 flow.byte_count)

def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    core.openflow.addListenerByName("FlowStatsReceived", _handle_FlowStatsReceived)
