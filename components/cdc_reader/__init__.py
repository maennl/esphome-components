import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID, CONF_PORT, CONF_BAUD_RATE

DEPENDENCIES = ['uart']

CONF_CDC_SERVER_ID = "cdc_server_id"

ns = cg.esphome_ns.namespace('cdc_reader')
CdcReader = ns.class_('CdcReader', cg.Component)

uart_ns = cg.esphome_ns.namespace("uart")


CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(CdcReader)
}).extend(cv.COMPONENT_SCHEMA)

def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)
