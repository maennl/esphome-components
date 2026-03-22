import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import CONF_ID, CONF_PORT

CONF_SIMPLE_TCP_SERVER_ID = "simple_tcp_server_id"

ns = cg.esphome_ns.namespace('simple_tcp_server')
SimpleTcpServer = ns.class_('SimpleTcpServer', cg.Component)

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(SimpleTcpServer),
    cv.Optional(CONF_PORT, default=8888): cv.port,
    cv.GenerateID(CONF_SIMPLE_TCP_SERVER_ID): cv.use_id(SimpleTcpServer),

}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
    cg.add(var.set_port(config[CONF_PORT]))
    