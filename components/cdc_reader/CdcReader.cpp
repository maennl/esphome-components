//
// Created by Marcel Schmidt on 22.03.26.
//

#include "CdcReader.h"
namespace esphome::cdc_reader
{
    static const char *const TAG = "cdc_reader";


    CdcReader::CdcReader()
    {
        // Constructor
    }

    void CdcReader::setup()
    {
        Component::setup();
    }

    void CdcReader::dump_config()
    {
        ESP_LOGCONFIG(TAG, "CDCReader:");

    }
}
